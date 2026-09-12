# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - Unreleased

### Added
- Constructor accepts a bare dictionary name (e.g. `"en_US"`) in addition to a `.dic` path, resolving it under `/usr/share/hunspell/`. Contributed by @PanderMusubi in #11.
- `raw()` is now cached with `functools.lru_cache` (maxsize 8192) to avoid repeated subprocess round-trips. Contributed by @PanderMusubi in #8.

### Fixed
- `spell()` and `suggest()` no longer return incorrect results for inputs prefixed with `*`/`+`/`-` hunspell markers. Contributed by @PanderMusubi in #6.

## [0.2.1] - 2024-XX-XX

### Fixed
- Strip first entry of `suggest()` output (the `&` marker line). #3

## [0.2.0] - 2024-XX-XX

### Added
- Initial public release. `HunSpell` class with `spell`, `suggest`, `stem`, `analyze`, and `raw` methods.
- `CLIRunner` for persistent subprocess interaction.
- `hunspell2` Python package on PyPI.

[0.3.0]: https://github.com/Alex23rodriguez/pyhunspell2/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/Alex23rodriguez/pyhunspell2/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Alex23rodriguez/pyhunspell2/releases/tag/v0.2.0
