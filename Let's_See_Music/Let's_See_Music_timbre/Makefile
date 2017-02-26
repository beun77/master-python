# This makefile will automatically build the tex/latex documents present in the
# current directory
# Author: Thibault Porteboeuf <thibault.porteboeuf@free.fr>

# Directory(ies) containing svg figures
FIGDIRS=figs

# Tool to be used for compilation
TEXTOOL=pdflatex
BIBTOOL=bibtex
SVGTOOL=inkscape
VIEWER=evince

#Main compilation targets
MAINTEX?=$(shell grep -l "^[^%]*\\documentclass" *.tex)
MAINPDF=$(MAINTEX:.tex=.pdf)
MAIN=$(MAINTEX:.tex=)

BIB=$(wildcard *.bib)

FIGS=$(foreach FIGDIR, $(FIGDIRS), $(wildcard $(FIGDIR)/*.svg))

TEX=$(wildcard *.tex)
PDFFIGS=$(FIGS:.svg=.pdf)
OTHERS=$(wildcard c/*.h) $(wildcard logos/*.png) $(wildcard *.cls)

# If USEBIB is empty, then no call to $(BIBTOOL) is made.
# If USEBIB contains '\bibliography{' then $(BIBTOOL) is called.
USEBIB=$(shell grep -o '^[^%]*\\bibliography' $(MAIN).tex)


# Build all documents in current directory
all:
	@bash -c 'grep -l "^[^%]*\\documentclass" *.tex | while read ligne; do make pdf MAINTEX="$$ligne"; done'

pdf: $(MAIN).pdf

$(MAIN).pdf: $(PDFFIGS) $(TEX) $(BIB) $(OTHERS)
	@echo "Makefile run for main tex document $(MAIN).tex"
	@echo "First $(TEXTOOL) run..."
	@$(TEXTOOL) $(MAIN).tex
	@if [ "$(USEBIB)" != "" ]; then echo ""; echo "Running $(BIBTOOL)..."; $(BIBTOOL) $(MAIN); fi
	@echo ""
	@echo "Running $(TEXTOOL) for cross-reference checking..."
	@$(TEXTOOL) -halt-on-error $(MAIN).tex > /dev/null
	@$(TEXTOOL) -halt-on-error $(MAIN).tex > /dev/null
	@$(TEXTOOL) -halt-on-error $(MAIN).tex > /dev/null
	@echo "Done."

%.pdf: %.svg
	@echo "Exporting svg $< -> $@..."
	@$(SVGTOOL) $< --export-pdf $@

view: $(MAINPDF)
	@echo ""
	@echo "Opening the main document(s) in the viewer:"
	$(VIEWER) $^
	@echo ""

clean:
	rm -f $(PDFFIGS)
	rm -f *.log
	rm -f *.aux
	rm -f *.toc
	rm -f *.lof
	rm -f *.blg
	rm -f *.bbl
	rm -f *.out
	rm -f *.nav
	rm -f *.snm
	rm -f $(MAINPDF)

.PHONY: clean view all pdf
