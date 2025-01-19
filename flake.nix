# in flake.nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        tex = pkgs.texlive.combine {
          inherit (pkgs.texlive) scheme-minimal latex-bin latexmk;
        };
      in with pkgs; {
        devShells.default = mkShell { buildInputs = [ uv ]; };
        packages.default = pkgs.stdenv.mkDerivation rec {
          pname = "static-website";
          version = "2025-01-19";
          src = ./.;
          nativeBuildInputs = [ uv ];
          buildPhase =
            "uv run -- make html"; # This needs to be fixed by updating the venv path
          installPhase = "cp -r output $out";
        };
      });
}
