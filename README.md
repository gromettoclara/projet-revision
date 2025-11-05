Produire le PDF 

`pandoc note_intention.md --bibliography=biblio.bib --citeproc --metadata link-citations=true -o note_intention.pdf --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue`

Faire un venv 

`python 3.10 -m venv venv`

Activer le venv 

installer les dépendances 

`pip install -r requirements.txt`