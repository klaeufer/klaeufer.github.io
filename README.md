[![Deploy site](https://github.com/klaeufer/klaeufer.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/klaeufer/klaeufer.github.io/actions/workflows/deploy.yml)

# Konstantin Läufer's personal website

Based on the amazing [al-folio](https://github.com/alshedivat/al-folio) theme.

Deployed at [laufer.cs.luc.edu](https://laufer.cs.luc.edu/). 
See also [klaeufer/cv](https://github.com/klaeufer/cv).

## Customizations and fixes

- Own site content (obviously) focusing on academic activities
- Direct integration with Zotero (see [tools](../../tree/main/tools) and [_data/zotero-bibs.txt](../../tree/main/_data/zotero-bibs.txt))
- Fixed link to YouTube channel in [_includes](../../tree/main/_includes)
- Fixed RSS parsing by adding `User-Agent` header in [_plugins/external-posts.rb](../../tree/main/_plugins/external-posts.rb)
