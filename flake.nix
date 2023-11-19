{
  description = "A flake to manage and build my website.";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python_packages = pkgs.python3.withPackages(ps: with ps;[
          pelican
          black
          blinker
          click
          commonmark
          docutils
          feedgenerator
          jinja2
          markdown
          markupsafe
          mypy-extensions
          pathspec
          platformdirs
          pygments
          python-dateutil
          pytz
          rich
          six
          tomli
          unidecode
        ]);
      in
        {
          packages.website = pkgs.stdenv.mkDerivation rec {
            pname = "static-website";
            version = "2022-11-18";
            src = ./.;
            nativeBuildInputs = [ python_packages ];
            buildPhase = "make html";
            installPhase = "cp -r output $out";
          };
          defaultPackage = self.packages.${system}.website;
          devShell = pkgs.mkShell {
            packages = with pkgs; [
              python_packages
            ];
          };
        }
    );
}
