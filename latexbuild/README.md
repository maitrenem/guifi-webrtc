The workflow (compilation of documentation process) is in the Makefile: clean, emacs batch export to latex, quit the bad emacs orgmode inserted header, put bibliography, open pdf, clean again.

# Files
- *tesi_upf.cls*: official latex class file from university
- *tesi_upf.el*: specification of the export for emacs orgmode to latex
- *removeHeaderFooter*: python script that removes the bad header inserted by orgmode and last line, that is a fake end of document
- *rfc.bib* obtained from http://tm.uka.de/~bless/rfc.bib
- Other latex support files (crop.sty, geometry.sty, vancouver.bst) were obtained from http://www.upf.edu/bibtic/guiesiajudes/eines/tesis/b5LaTex.zip

Extra info por people that wants to follow this workflow: Emacs 24.4.1 (Org mode 8.2.10)