## Structure du répo : 

- note d'intention premier rendu : []()
- introduction au travail final : []()
- les trois éditions finale : ici ici et ici
- comment regarder le proto 

## cheatsheet des commandes : 

Produire le PDF note d'intention

`pandoc note_intention.md --bibliography=biblio.bib --citeproc --metadata link-citations=true -o note_intention.pdf --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue`

Sortir le tex de l'introduction explicative : 

```
```

Regex pour nettoyer les fichiers (enlever les retours chariot inutiles) : `(?<!\n)\n(?!\n)` penser à remplacer par un espace !

Faire le diff avec wdiff 

`wdiff <V1> <V2> > comparaison.txt`
