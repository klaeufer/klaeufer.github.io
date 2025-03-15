#!/usr/bin/env python

import argparse
import bibtexparser
from bibtexparser.bparser import BibTexParser
import re

def expand_tex_fields(entry):
    """
    Extracts tex.* fields from the note field and promotes them to top-level fields.
    Only replaces `\\_` with `_` in keys but leaves other characters like `+` untouched.
    """
    if 'note' in entry:
        note_entry = entry['note']
        del entry['note']

        new_fields = {}
        new_note_lines = []
        
        for line in note_entry.splitlines():
            tex_match = re.match(r"tex\.([\w\+\_\\]+):\s*(.*)", line)  # Allow underscores, plus, and letters
            if tex_match:
                key, value = tex_match.groups()
                # Convert \_ to _ but leave + intact
                key = key.replace("\\_", "_")
                new_fields[key] = value.strip()
            else:
                new_note_lines.append(line)

        # Merge extracted fields into the entry
        entry.update(new_fields)

        # Retain the modified note field (excluding extracted tex.* fields)
        if new_note_lines:
            entry['extra'] = "\n".join(new_note_lines)

    if 'type' in entry:
        entry['note'] = entry['type']

    return entry

def add_year_if_missing(entry):
    """
    Adds a year field based on date.
    jekyll-scholar will break without year.
    """
    if not 'year' in entry:
        match = re.match(r"(\d{4})", entry['date'])
        if match:
            entry['year'] = match.group(1)

def add_jekyll_scholar_fields(entry):
    """
    Adds any missing fields required by or beneficial to jekyll-scholar as
    described at https://github.com/alshedivat/al-folio/blob/main/CUSTOMIZE.md.
    """
    if 'arxiv' in entry:
        arxiv = entry['arxiv']
        if not 'pdf' in entry:
            entry['pdf'] = 'https://arxiv.org/pdf/' + arxiv

    if 'url' in entry:
        if 'ecommons.luc.edu' in entry['url']:
            if not 'pdf' in entry:
                entry['pdf'] = entry['url']
        elif not ('arxiv' in entry['url']
                or '.pdf' in entry['url']
                or 'website' in entry):
            entry['website'] = entry['url']


def process_bibtex_file(input_bib, output_bib):
    """
    Reads a BibTeX file, expands tex.* fields, and writes the updated BibTeX file.
    """
    with open(input_bib, 'r', encoding='utf-8') as bib_file:
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.load(bib_file, parser)

    # Expand tex.* fields for each entry
    for entry in bib_database.entries:
        expand_tex_fields(entry)
        add_year_if_missing(entry)
        add_jekyll_scholar_fields(entry)

    # Write the transformed BibTeX back to a file
    with open(output_bib, 'w', encoding='utf-8') as bib_file:
        bibtexparser.dump(bib_database, bib_file)

    print(f"Transformed BibTeX saved to {output_bib}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expand tex.* fields in a BibTeX file.")
    parser.add_argument("input_bib", help="Path to the input BibTeX file")
    parser.add_argument("output_bib", help="Path to the output BibTeX file")
    args = parser.parse_args()

    process_bibtex_file(args.input_bib, args.output_bib)
