all:  clean org bib

clean:
#from a list of files, remove thesis.* except thesis.org and thesis.pdf
	ls | grep -P thesis.'(?!org)(?!pdf)' | tr "\n" "\0" | xargs -0 rm -rf
#http://stackoverflow.com/questions/1240275/how-to-negate-specific-word-in-regex
#http://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
#http://stackoverflow.com/questions/20307299/linux-why-cant-i-pipe-find-result-to-rm

org:
#export from orgmode to latex
	emacs thesis.org --batch -l tesi_upf.el -f org-latex-export-to-latex --kill
#headless
	python removeHeaderFooter.py

bib:
#put bibliography
	pdflatex thesis.tex
	bibtex thesis
	pdflatex thesis.tex
	pdflatex thesis.tex
pdf:
	evince thesis.pdf &disown
