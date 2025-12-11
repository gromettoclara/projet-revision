Jeveux modéliser non seulement les types de révision mais aussi le processus de révision. Acteur 1 fait des révision / acteur 2 prend connaissance de ces révisions. 

Vu que sur Stylo c'est difficile de tracer qui fait quoi : j'ai déduis depuis le titre des version qui était responsable de quels changements 

les problèmes rencontrés 

entretien avec Florence : 

ce qui est pertinent c'est de commencer la classification par le degré d'"importance" des corrections. Ou plutôt c'est une question d'expertise et de métier. 
- ortho-typo / grammaire => c'est les correcteurices qui sont spécialistes, certains auteurs ne veulent même pas en entendre parler mais pour d'autres c'est important. 
- des reformulations importantes qui deviennent alors des query ou suggestions.
    - déplacement
    - redondances => suppression 
    - reformulation pour des questions de clarté ou pb de syntaxe


importance de visibiliser le travail des éditeurices dans stylo

importance de pouvoir brancher antidote

Le pb c'est qu'on ne voit pas le travail des correcteurices pour engager le dialogue avec l'auteur. Pour le moment, Florence corrige les fautes ortho typo mais pour des reformulations importantes, elle passe par hypothesis. 



Granularité 

les principales corrections effectuées par Arilys et Adrien sont des corrections typo => apostrophe courbe + espace fine insécables avant les ponctuations concernées. des chercher remplacer. du coup il y en a partout. le diff n'a pas une granularité suffisante. au mot près : sur plusieurs mots on a plusieurs modifications. Donc il va y avoir, pour des groupes de mots, plusieurs modifs par bloc de texte. Cependant, c'est très lourd comme encodage. 

Problématique => visibiliser le travail du texte par les différents acteurs de l'édition. 



Pb de quand on a de la ponctuation collée au mot elle va direct dans l'app 

mais il y a des fois où c'est pertinent : 

<app>
               <lem wit="#V1">vie .</lem>
               <rdg wit="#V2">vie.</rdg>
            </app>


Dans le snauwert par exemple toutes les citations qui sont mises en italique est-ce que on veut considérer tout le groupe de texte qui est mis en italique ? Si oui comment on automatise le changement d'échelle ? 


Le script est basé sur des regex il marche sauf 

- les suppressions (où il y a pas d'ajout dans le rdg)
- les citations dans le nom que c'est la même syntaxe (par exemple [-@machin])
- des fois les milestones ça reste des balises et des fois 

Choisir de travailler sur la syntaxe markdown parce que c'est là dessus que travaillent les éditeurices de sens public. Et une partie de leur travail c'est de corriger le markdown. Même si ce n'est pas une pratique courante d'encoder du code en TEI, ici ça fait du sens. 



Idées de catégorisation : 

1. Corrections mécaniques : mécanique de la langue, mécanique du code, mécanique de la pipeline, fluidité de la lecture

- orthographe -- rectifications d’erreurs d'orthographe, harmonisation des graphies.
- Casse, capitalisation, abréviations, ponctuation, faces -- questions d'uniformisation des majuscules/minuscules, dés abréviations, des signes de ponctuation, espaces insécables. Des changement qui peuvent se faire en masse.
- Numérotation, listes, dates, chiffres -- correction ou cohérence des éléments numériques.
- Grammaire et Syntaxe -- accord, conjugaison, structure de phrases, impropriétés syntaxiques.
- Code markdown -- harmonisation et correction pour rentrer sans frottement dans la chaîne de conversion. 

2. Modifications substantives : sémantiques ou rhétoriques

- ponctuation -- virgules, points, tirets, guillemets, usage des italiques avec une incidence sur le sens ou le style.
- Substitutions lexicales / de genre / de nombre non mécaniques.
- Ajouts ou suppressions de mots/phrases.
- Déplacements de mot/phrases.
- Réécriture ponctuelle de segments.

3. Autour du texte -- interventions sur les références et paratexte éditorial

- Ajouts de notes de bas de page éditoriale.
- Correction de citations.
- Vérification de fond sur la bibliographie.





Milligan & Tinkle, Literary Editing in the Digital Age (2022).
Peter Shillingsburg, From Gutenberg to Google
Fredson Bowers, Textual and Literary Criticism (1959).


Des trucs à checker : 

- les espaces autour de milestone et app 
- est-ce qu'on laisse des lem ou des rdg vides ? 
- dans snauwaert les citations chelous avec plein de > 
- reprendre les textes nettoyés et refaire le wdiff pour que ce soit bien propre