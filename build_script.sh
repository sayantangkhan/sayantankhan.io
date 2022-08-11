#!/bin/bash

# Generating pdf CV
cd CV_data
latexmk -pdflatex=lualatex -pdf main.tex
cp build/main.pdf ../content/pages/pdfs/cv/cv.pdf
cd ..

# Generating markdown CV
/home/sayantan/Sync/websites/sayantankhan.io/source/.pelican-virtualenv/bin/python CV_data/generate_cv.py

# Rendering markdown using pelican
make html
