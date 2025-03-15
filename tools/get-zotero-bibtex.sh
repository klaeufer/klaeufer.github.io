#!/bin/bash

# https://www.zotero.org/groups/5882358/laufer-incollection


BIB_DIR=_bibliography
ZOTERO_BIB_URLS=_data/zotero-bibs.txt
ZOTERO_API=https://api.zotero.org

rm -rf $BIB_DIR
mkdir -p $BIB_DIR

for u in $(cut -d/ -f 5-6 $ZOTERO_BIB_URLS) ; do

  GROUP_ID="${u%/*}"
  OUTPUT_FILE="$BIB_DIR/${u#*/}.bib"

  curl -L "$ZOTERO_API/groups/$GROUP_ID/items/top?format=bibtex&limit=100" -o "$OUTPUT_FILE"

  echo "BibTeX file downloaded: $OUTPUT_FILE"

done

echo "Sanitizing downloaded bib files"
for bibfile in $BIB_DIR/*.bib
do
    bibfile_raw=${bibfile%.bib}-raw.bib
    mv "$bibfile" "$bibfile_raw"
    tools/sanitize-zotero-bib.py "$bibfile_raw" "$bibfile"
done
rm -f $BIB_DIR/*-raw.bib

echo "Collating downloaded bibs"
cat $BIB_DIR/*.bib > $BIB_DIR/papers.bib
