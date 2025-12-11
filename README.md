Produire le PDF 

`pandoc note_intention.md --bibliography=biblio.bib --citeproc --metadata link-citations=true -o note_intention.pdf --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue`

Regex pour nettoyer les fichiers (enlever les retours chariot inutiles) : `(?<!\n)\n(?!\n)` penser à remplacer par un espace !

Workflow : 

- nettoyage des textes 
- remplacer les retour par une balise milestone (chercher-remplacer) 
- `wdiff <V1> <V2> > comparaison.txt`
- on passe le script comparaison.py 
- on repasse sur le xml

