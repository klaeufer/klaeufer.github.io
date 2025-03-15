#!/bin/bash

PATH=/opt/homebrew/opt/ruby/bin:$PATH
. .venv/bin/activate

./tools/get-zotero-bibtex.sh
bundle exec jekyll serve
