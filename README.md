# sayantankhan.io
Source code for my personal website hosted at www.sayantankhan.io.

## Requirements

The website is built via Nix.

1. Enter the nix shell via `nix develop .`.
2. The website can be tested out via `uv run -- make devserver`.
3. Once it's tested run `uv run -- make html` to generate the final output, or any of the other build targets in the Makefil.
4. The CV generation needs additional packages in the Nix buildInputs (TODO: need to add this).

Run `build_script.sh` to build the CVs, and the website.
