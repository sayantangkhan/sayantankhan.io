#!/bin/bash

# Generating pdf CV
cd CV_data
latexmk -pdflatex=lualatex -pdf main.tex
cp build/main.pdf ../content/pages/pdfs/cv/cv.pdf
cd ..

# Generating markdown CV
uv run -- CV_data/generate_cv.py

# Rendering markdown using pelican
make html
