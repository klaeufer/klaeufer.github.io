---
# An instance of the Portfolio widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 65

title: Research
subtitle: ''

content:
  # Page type to display. E.g. project.
  page_type: project

  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
    - name: All
      tag: '*'
#    - name: Deep Learning
#      tag: Deep Learning
#    - name: Other
#      tag: Demo

design:
  # Choose how many columns the section has. Valid values: '1' or '2'.
  columns: '2'

  # Toggle between the various page layout types.
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   5 = Showcase
  view: 2

  # For Showcase view, flip alternate rows?
  flip_alt_rows: false
---

##  Active projects

- [UnoAPI](https://unoapi.cs.luc.edu): Curricular modules for high-performance computing using data-parallel C++ with Intel's OneAPI.
- [Metrics Project](https://ssl.cs.luc.edu/projects/metricsDashboard): Longitudinal process quality metrics for software development, including
  - [SparkBadge](https://github.com/klaeufer/sparkbadge): Longitudinal project status badges.
- [DriveAware](https://ecommons.luc.edu/csrs/ay2021-2022/techreport/1): Generating actionable data on social justice issues through vehicle-based citizen science. 
- Doyle Living Systems Lab (incubation): Smart spaces using open-source software and hardware.
- [Loyola42ndParallel](https://loyola42ndparallel.github.io) (incubation): A data-driven view of sustainability and other social justice challenges along the 42nd parallel, which runs not only through Chicago but also through Loyola University Chicago's main campus.
