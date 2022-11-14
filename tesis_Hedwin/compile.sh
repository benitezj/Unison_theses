#!/bin/bash

thesis="thesis";

if [ $1 = "clean" ]
then
	echo "Cleaning please wait ..."
	rm -f *~
	rm -rf *.aux
	rm -rf ./*/*.aux
	rm -rf *.bbl
	rm -rf *.blg
	rm -rf *.d
	rm -rf *.fls
	rm -rf *.ilg
	rm -rf *.ind
	rm -rf *.toc*
	rm -rf *.lot*
	rm -rf *.lof*
	rm -rf *.log
	rm -rf *.idx
	rm -rf *.out*
	rm -rf *.nlo
	rm -rf *.nls
	rm -rf $thesis.pdf
	rm -rf $thesis.ps
	rm -rf $thesis.dvi
	rm -rf $thesis.spl
	rm -rf *#* 
	echo "Cleaning complete!"
else
	echo "Compiling ...!"
	pdflatex -interaction=nonstopmode $thesis.tex
	bibtex $thesis.aux 	
	makeindex $thesis.aux
	makeindex $thesis.idx
	makeindex $thesis.nlo -s nomencl.ist -o $thesis.nls
	pdflatex -interaction=nonstopmode $thesis.tex
	makeindex $thesis.nlo -s nomencl.ist -o $thesis.nls
	pdflatex -interaction=nonstopmode $thesis.tex
	echo "Success!"
fi
