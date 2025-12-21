---
title: "Titre bien pour un workflow de révision -- introduction explicative"
subtitle: FRA 6730
author: Clara Grometto
date: décembre 2025
bibliography: biblio.bib
nocite: |
  @*
header-includes:
  - \usepackage{setspace}
  - \usepackage[left=2.2cm, right=2.2cm, top=2cm, bottom=2.3cm]{geometry}
  - \setlength{\skip\footins}{0.7cm}
  - \usepackage{nowidow}
  - |
    \widowpenalty=10000
    \clubpenalty=10000
  - |
    \makeatletter
    \renewcommand{\footnoterule}{%
      \kern -3pt
      \hrule width 0.35\linewidth
      \kern 8pt
    }
    \makeatother
---

```{=latex}
\doublespacing
```

Ce travail s'inscrit dans une réflexion autour de la modélisation de la révision éditoriale, notamment dans le cadre de l'édition scientifique. Il s'agit non seulement de modéliser les types de correction mais aussi le processus dialogique qui s'engage entre les divers acteur·ices. Nous voudrions dépasser une approche strictement typologique des révision pour les intégrer la dynamique de leur réception et leur discussion, s'inspirant des gestes et des pratiques des éditeur·ices. 

Un premier entretien avec <!-- Florence de HN --> montre que la classification des révisions peut peut être pensée indépendamment des métiers et des niveaux d'expertise mobilisés. La première distinction qui paraîtrait aidante relève du degré d’« importance » des corrections. C'est le terme de Florence, mais on va employer un autre terme car on ne veut pas hiérarchiser en terme de niveau mais plutôt de domaine d'expértise mobilisé.

Les corrections orthotypographiques et grammaticales relèvent du domaine des correcteur·ices et éditeur·ices. Ils ne sont pas moins importants et ils participent également à la production du sens, d'ailleurs les auteur·ices doivent en prendre connaissance, mais ils doivent les recevoir comme des améliorations de la parts d'experts de la langue. Les reformulations plus substantielles — déplacements de segments, suppressions de redondances, reformulations visant la clarté ou la correction syntaxique — engagent davantage le sens et la structure du texte, et prennent alors la forme de suggestions ou de questions adressées à l’auteur·ice.

Aujourd'hui Stylo (mais pas seulement Stylo car c'est le cas de tous les outils actuels) a un manque important : l'invisibilisation du travail éditorial sur le texte. Faute d’un dispositif permettant de rendre ces interventions visibles et discutables, le dialogue entre éditeur·ice et auteur·ice se déplace vers des outils externes (dans Stylo pas totalement car intégration de Hypothesis, mais moyen détourné), souvent multiplication de fichiers et de mails. 

C'est la grande qualité du track changes de word : il rend le travail des correcteur.ices visible. 

Mieux structurer l'échange entre auteur et correcteur, visibiliser le travail de ces derniers, sans renoncer à une modélisation fine des types d'intreventions. 

Ce que je propose 





Ce que je propose c'est la modélisation d'un workflow en TEI. XML n'est peut-être pas le langage le plus adapté mais il a l'avantage d'être sémantiquement très riche. 







Je veux modéliser non seulement les types de révision mais aussi le processus de révision. Acteur 1 fait des révision / acteur 2 prend connaissance de ces révisions. 



description des besoins

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



Catégorisation appliquée : 

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


description de la chaîne

Workflow : 

- nettoyage des textes : enlever les saut de ligne qui ne font pas des paragraphes
- remplacer les doubles retour (donc ça fait des paragraphes) par une balise milestone et lb (chercher-remplacer) 
- Faire le wdiff et l'écrire dans comparaison.txt
- on passe le script comparaison.py qui fait aussi un nettoyage des doubles espaces
- on repasse sur le xml à la main et on remplit le header
- passage d'une xslt pour ajout des identifiants
- prototype de xform 
  - un onglet pour juste regarder les changements mécaniques
  - un onglet pour choisir le lem donc accepter oou refuser les changements substantiels
  - un onglet pour lire la version modifiée

en quoi ça répondrait au besoin. Expliquer. 




<!-- Vu que sur Stylo c'est difficile de tracer qui fait quoi : j'ai déduis depuis le titre des version qui était responsable de quels changements. Donc j'ai abandonné l'idée de mettre un attribut resp. Mais ça souligne un besoin.  -->


Comme relevé plus haut, dans Stylo, l’identification précise de qui fait quoi au sein du processus de révision est difficile. J’ai donc décidé de déduire la responsabilité des changements à partir des titres de versions. Cette contrainte m’a conduite à abandonner l’idée d’introduire un attribut formel de type resp à chaque modification. Ce renoncement ne résout toutefois pas le problème ; au contraire, il met en évidence une question : jusqu'à quel point il faut attribuer les interventions aux différents acteurs ? avec quel niveau de granularité ? Plutôt raisonner en terme d'atapes significtaives dans le processus de révision et une attribution. Là je me contredis car c'est un peu ce qui est déjà dans Stylo. 


**Corrections pas pertinentes**

Les principales corrections effectuées par Arilys et Adrien relèvent de la correction typographique : remplacement d’apostrophes droites par des apostrophes courbes, ajout d’espaces fines insécables avant certaines ponctuations, des opérations de type « chercher–remplacer ». Ces interventions sont donc massives et diffuses. Il faudrait pouvoir les signaler sans les pointer systématiquement. 

j’ai fait le choix de m’appuyer sur des versions ultérieures du texte, produites après ces stades de corrections typographiques (versions identifiées "CQ" pour contrôle qualité).


**Pb de granularité**


Pour le moment on a une granularité qui concerne le mot. 

On a un problème de granularité et de changement d'échelle. Voici une illustration du problème. Lorsque la ponctuation est directement accolée au mot, elle est intégrée telle quelle dans l’apparat de variantes. Des fois ce n'est pas très pertinent car la correction ne concerne pas la ponctuation. 

```xml
<app>
    <lem wit="#V1">vie .</lem>
    <rdg wit="#V2">vie.</rdg>
</app>

```

Dans ce cas précis, l’encodage rend compte de manière pertinente de la correction typographique. Le niveau de granularité adopté (le mot assorti de sa ponctuation) semble adéquat.

Dans certains contextes, la variation ne concerne plus un signe ou un mot isolé, mais un ensemble textuel cohérent. C’est le cas, par exemple, dans Snauwert, où l’ensemble des citations est mis en italique. La question se pose alors de savoir si l’on souhaite considérer chaque occurrence de balise italique comme une micro-variation, ou bien si l’on doit traiter l’ensemble du passage concerné, ce qui améliorerait la lisibilité

comment automatiser ce changement d’échelle ? 

soit une sur-fragmentation du texte, au risque de rendre le track changes illisible, soit à une agrégation trop grossière, qui efface la nature précise des interventions réalisées.

Cette tension entre précision locale et cohérence globale constitue selon nous le prinicipal problème dans l'entreprise de modélisation et automatisation d'un track changes qui prend en compte cette modélisation. 




Le script est basé sur des regex il marche sauf 

- les suppressions (où il y a pas d'ajout dans le rdg)
- les citations dans le nom que c'est la même syntaxe (par exemple [-@machin])
- des fois les milestones ça reste des balises et des fois 

Choisir de travailler sur la syntaxe markdown parce que c'est là dessus que travaillent les éditeurices de sens public. Et une partie de leur travail c'est de corriger le markdown. Même si ce n'est pas une pratique courante d'encoder du code en TEI, ici ça fait du sens. 








Milligan & Tinkle, Literary Editing in the Digital Age (2022).
Peter Shillingsburg, From Gutenberg to Google
Fredson Bowers, Textual and Literary Criticism (1959).


**Des trucs à checker :** 

- [x] les espaces autour de milestone et app 
- [ ] dans snauwaert les citations chelous avec plein de > 
- [x] laisser des rdg ou des lem vides ? Oui
- [x] reprendre les textes nettoyés et refaire le wdiff pour que ce soit bien propre
- [ ] on peut essayer d'améliorer le css du formulaire html
- [ ] que faire entre profiledesc et interaction timeline ? 
- [x] est-ce que je mets les resp ? Non je justifie
- [ ] bien vérifier que tout le header est complété avec cette histoire de revision desc et de timeline
- [ ] enlever les commentaires dans les xml
- [x] truc des espaces insécables

**Mes bugs :**

- [x] Attributs multi-valués je crois qu'il faut faire un for-each-group sa grand-mere
- [x] la xslt add-ids ramène des identifiants que je veux pas sur les ab c'est peut-être pas gênant 
- [x] gestion de méca dans review il faut seulement le rdg
