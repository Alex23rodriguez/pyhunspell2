# myhunspell

A modern, lightweight Python interface to **Hunspell**, designed to work with **current Hunspell versions** and to be **easy to install across platforms**, including macOS.

This project was created as a maintained alternative to [`pyhunspell`](https://github.com/pyhunspell/pyhunspell), which is no longer actively maintained and does not support newer releases of Hunspell.

---

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

---

## Requirements

- Python 3.11+
- **Hunspell must be installed and available on your `PATH`**

You can verify Hunspell is available by running:

```bash
hunspell -v
