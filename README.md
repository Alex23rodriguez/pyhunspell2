# PyHunspell2

A modern, lightweight Python interface to **Hunspell**, designed to work with **current Hunspell versions** and to be **easy to install across platforms**, including macOS.

This project was created as a maintained alternative to [`pyhunspell`](https://github.com/pyhunspell/pyhunspell), which is no longer actively maintained and does not support newer releases of Hunspell.

---
## Installation

using pip:
`pip install hunspell2`

or, if using uv:
`uv add hunspell2`

### Additional requirements:
- **[hunspell](https://github.com/hunspell/hunspell) must be installed and available on your `PATH`**. (check by running `hunspell -v`)

- Provide your own `.dic` and `.aff` files
    - many languages are available [here](https://github.com/elastic/hunspell/tree/master/dicts)
    - note that few languages provide stem and morphological analysis


## Usage
```python
from hunspell2 import HunSpell

# Load a dictionary
hs = HunSpell("../dicts/fr/fr.dic")

# Check spelling
hs.spell("asdf")
# False

hs.spell("salut")
# True

# Get spelling suggestions
hs.suggest("garcon")
# ['garçon', 'gardon', 'gascon']

# Get raw line by line output from the hunspell subprocess
hs.raw("garcon")
# ['& garcon 3 0: garçon, gardon, gascon\n', '\n']

# Get stems
hs.stem("suis")
# ['suivre', 'être']

# Morphological analysis
hs.analyze("est")
# [
#   ['st:est', 'po:nom', 'is:mas', 'is:sg'],
#   ['st:être', 'po:v0ei_____a', 'po:ipre', 'po:3sg']
# ]

# Optional: close after no longer needed
hs.close()
```

## Motivation

Hunspell is widely used for spell checking, but existing Python bindings—most notably `pyhunspell`—have fallen behind:

- `pyhunspell` is no longer actively maintained
- It does not support modern Hunspell versions (≥ 1.7)
- Installation often fails on newer systems, or requires manual tinkering, especially macOS

This library aims to provide:

- ✅ Compatibility with **current Hunspell versions**
- ✅ Simple installation on **macOS, Linux, and other platforms**
- ✅ A clean, Pythonic API
- ✅ Minimal build complexity

---

## Design

Instead of tightly coupling to Hunspell’s internal C++ headers and build layout, this library relies on the **system-installed `hunspell` command-line tool**.

This design choice provides several benefits:

- No fragile dependency on Hunspell’s internal header structure
- Works with any Hunspell version available on the system
- Simplifies installation, especially on macOS
- Avoids compiler and ABI issues common with native Python extensions
