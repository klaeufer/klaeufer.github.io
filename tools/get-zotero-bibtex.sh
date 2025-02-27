#!/bin/bash

# https://www.zotero.org/groups/5882358/laufer-incollection


BIB_DIR=_bibliography
TBIB_DIR=$TMPDIR/$BIB_DIR
ZOTERO_BIB_URLS=_data/zotero-bibs.txt
ZOTERO_API=https://api.zotero.org

mkdir -p $BIB_DIR
mkdir -p $TBIB_DIR

echo "BIB_DIR=$BIB_DIR"
echo "TBIB_DIR=$TBIB_DIR"

for u in $(cut -d/ -f 5-6 $ZOTERO_BIB_URLS) ; do

  GROUP_ID="${u%/*}"
  OUTPUT_FILE="$TBIB_DIR/${u#*/}.bib"

  # To ensure correct export of TechReport and PhDThesis entries, 
  # use format=bibtex, NOT biblatex
  curl -L "$ZOTERO_API/groups/$GROUP_ID/items?format=bibtex&limit=100" -o "$OUTPUT_FILE"

  echo "BibTeX file downloaded: $OUTPUT_FILE"

done

echo "Sanitizing downloaded bib files"
for bibfile in $TBIB_DIR/*.bib
do
    bibfile_raw=${bibfile%.bib}-raw.bib
    mv "$bibfile" "$bibfile_raw"
    tools/sanitize-zotero-bib.py "$bibfile_raw" "$bibfile"
done
rm -f $TBIB_DIR/*-raw.bib

echo "Collating downloaded bibs"
cat $TBIB_DIR/*.bib > $BIB_DIR/papers.bib
