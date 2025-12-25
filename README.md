## Structure du répo

- [note d'intention](02note_intention/note_intention.pdf), premier rendu
- [introduction explicative](01introduction/claraintro.pdf) du travail final
- les trois éditions finale : dans le dossier [00editionFinale](00editionFinale)
- consulter le prototype XForm : à [ce lien](https://gromettoclara.github.io/projet-revision/) 

## Pour appliquer le reviewer à d'autres documents 

1. Modifier [cette ligne](https://github.com/gromettoclara/projet-revision/blob/5deda68a716c5284c5adc0dccd89d69a80228acb/proto/index.xml#L20) et remplacer vers un chemin relatif vers les XML du dossier 00editionFinale

2. Lancer un serveur local 

3. Ouvrir proto/index.html

## cheatsheet des commandes : 

### Produire le PDF note d'intention

`pandoc note_intention.md --bibliography=biblio.bib --citeproc --metadata link-citations=true -o note_intention.pdf --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue`

### Sortir le tex de l'introduction explicative : 

`pandoc intro.md   --bibliography=biblio-travail-final.bib   --csl=sciences-po-ecole-doctorale-note-french.csl   --citeproc   --metadata link-citations=true   --standalone   -o claraintro.tex   -V colorlinks=true   -V linkcolor=blue   -V citecolor=blue   -V urlcolor=blue`

### Regex pour nettoyer les fichiers (enlever les retours chariot inutiles) : 

`(?<!\n)\n(?!\n)` penser à remplacer par un espace !

### Faire le diff avec `wdiff` 

`wdiff <V1> <V2> > comparaison.txt`