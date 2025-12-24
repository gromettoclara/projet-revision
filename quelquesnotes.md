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

Ce travail une expérimentation-réflexion autour de la modélisation de la révision éditoriale, notamment dans le cadre de l'édition scientifique. Il s'agit non seulement de modéliser les types de correction mais aussi le processus dialogique qui s'engage entre les divers acteur·ices. Nous voudrions dépasser une approche strictement typologique des révision pour les intégrer la dynamique de leur réception et leur discussion, s'inspirant des gestes et des pratiques des éditeur·ices. 

Un premier entretien avec <!-- Florence de HN --> montre que la classification des révisions peut peut être pensée indépendamment des métiers et des expertise mobilisés. La première distinction qui paraîtrait aidante relève du degré d’« importance » des corrections. C'est le terme de Florence, mais on va employer un autre terme car on ne veut pas hiérarchiser en terme de niveau mais plutôt de domaine d'expértise mobilisé.

Les corrections orthotypographiques et grammaticales relèvent du domaine des correcteur·ices et éditeur·ices. Ils ne sont pas moins importants et ils participent également à la production du sens, d'ailleurs les auteur·ices doivent en prendre connaissance, mais ils doivent les recevoir comme des améliorations de la parts d'experts de la langue. Les reformulations plus substantielles — déplacements de segments, suppressions de redondances, reformulations visant la clarté ou la correction syntaxique — engagent davantage le sens et la structure du texte, et prennent alors la forme de suggestions ou de questions adressées à l’auteur·ice.

<!-- Ajouter la ref à chicago. 
 -->
Aujourd'hui Stylo (mais pas seulement Stylo car c'est le cas de tous les outils actuels sauf le track changes de word) a un manque important : l'invisibilisation du travail éditorial sur le texte. Faute d’un dispositif permettant de rendre ces interventions visibles et discutables, le dialogue entre éditeur·ice et auteur·ice se déplace vers des outils externes (dans Stylo pas totalement car intégration de Hypothesis, mais moyen détourné), souvent multiplication de fichiers et de mails. 

C'est la grande qualité du track changes de word : il rend le travail des correcteur.ices visible. 

Mieux structurer l'échange entre auteur et correcteur, visibiliser le travail de ces derniers, sans renoncer à une modélisation fine des types d'intreventions. 

Ce que je propose 

Ce que je propose c'est la modélisation d'un workflow en TEI. XML n'est peut-être pas le langage le plus adapté mais il a l'avantage d'être sémantiquement très riche. Acteur 1 fait des révision / acteur 2 prend connaissance de ces révisions. 


Mais la personne qui prend connaissance des révisions veut pouvoir donner son opinion uniquemnt sur ce qui le concerne. L'auteur n'a pas besoin de donner son avis sur des corrections éditoriales ou là où la réviseureuse a une meilleure expertise que lui. 


Voici donc la catégorisation appliquée


1. Corrections mécaniques : mécanique de la langue, mécanique du code, mécanique de la pipeline, fluidité de la lecture

- orthographe -- rectifications d’erreurs d'orthographe, harmonisation des graphies.
- Casse, capitalisation, abréviations, ponctuation, faces -- questions d'uniformisation des majuscules/minuscules, dés abréviations, des signes de ponctuation, espaces insécables. Ces changement peuvent se faire en masse.
- Numérotation, listes, dates, chiffres -- correction ou cohérence des éléments numériques.
- Grammaire et Syntaxe -- accord, conjugaison, structure de phrases, impropriétés syntaxiques.
- Code markdown -- harmonisation et correction pour rentrer sans frottement dans la chaîne de conversion. 

2. Modifications substantives : rhétoriques, stylistique 

- ponctuation -- virgules, points, tirets, guillemets, usage des italiques avec une incidence sur le sens ou le style.
- Substitutions lexicales / de genre / de nombre non mécaniques.
- Ajouts ou suppressions de mots/phrases.
- Déplacements de mot/phrases.
- Réécriture ponctuelle de segments.

3. Autour du texte -- interventions sur les références et paratexte éditorial

- Ajouts de notes de bas de page éditoriale.
- Correction de citations.
- Vérification de fond sur la bibliographie.



<!-- en quoi ça répondrait au besoin. Expliquer. 
 -->
Le workflow permettant de passer de deux markdown à xml tei riche et avec toutes les métadonnées dans le header est un peu artisanale et mériterait d'être rafiné. 

La première étape, à partir de l'export du markdown dans Stylo, est le nettoyage des sources brutes. Essentiellement cela consiste à supprimer les retours charriot qui ne correspondent pas à la création d'un nouveau paragraphe en markdown, pour supprimer des sources de différences non significatives entre les deux versions et faciliter le passage de l'algorithme de diff. Cette étape est Les doubles retours, qui eux marquent des paragraphe en markdow, sont remplacés directement par les balises `<milestone unit="tei:p"/><lb/>`, encore une fois pour mieux aligner les textes. Ces deux premières étapes sont effectuées grâce à des chercher-remplacer. 

Ensuite, un diff est généré grâce à l'algorithme wdiff, qui a un niveau de granularité au mot près. Le résultat est stocké dans un fihier nommé comparaison.txt. Le script en python comparaison.py traite ce fichier. Il repère les segments supprimés et ajoutés balisés sous la forme [- … -] {+ … +} grâce à des regex, et réinjecte le contenu dans des éléments `<app>`, `<lem>` et `<rdg>`, échappe les caractères XML sensibles et nettoie les espaces superflus (<!-- ceux qui existent dans les deux version, restent d'un mauvais nettoyage et ne sont pas des erreurs -->). Le résultat est intégré dans un squelette TEI comprenant la base d'un header. 

Le fichier XML obtenu est ensuite repris manuellement. Cette étape permet de vérifier tout le texte. Le script en python s'avérait en effet efficace jusqu'aux cas particuliers (par exemple ouverture d'un élément app quand il y a une syntaxe md de type [-@machin]). Ce script mériterait donc d'être amélioré (avec par exemple des regex plus solide), ou changer complètement l'approche, mais il était satisfaisant car de toute manière dans le cadre de ce premier projet il fallait relire tout. Aussi c'est l'occasion de compléter et vérifier le header, en remplissant les métadonnées propres à chaque document. On en profite pour ajouter un attribut corresp à chaque élément app. Une transformation XSLT est ensuite appliquée pour ajouter les identifiants à chaque élément `<app>` et ses enfants. 

Grâce à ces ids, un prototype Xform permet la consultation et la validation des corrections en deux étapes. Un premier onglet dédié seulement à la visualisation des changements mécaniques, sans possibilité d'action, seulement pour en prendre connaissance. Un deuxième onglet permet de prendre connaissance des modification substantielles et de les accepter ou les refuser (choisir le lem dans le XML). 

<!-- A cette étape on pourrait faire que ça rajoute un resp et le nom dans le tei mais c'est complexe -->

Un troisième onglet donne accès à la lecture de la version modifiée du texte, avec une mise en avant des changements acceptés ou refusés. 



<!-- Vu que sur Stylo c'est difficile de tracer qui fait quoi : j'ai déduis depuis le titre des version qui était responsable de quels changements. Donc j'ai abandonné l'idée de mettre un attribut resp. Mais ça souligne un besoin.  -->


Comme relevé plus haut, dans Stylo, l’identification précise de qui fait quoi au sein du processus de révision est difficile. J’ai donc décidé de déduire la responsabilité des changements à partir des titres de versions. Cette contrainte m’a conduite à abandonner l’idée d’introduire un attribut resp à chaque modification. Ce renoncement ne résout toutefois pas le problème ; au contraire, il met en évidence une question : jusqu'à quel point il faut attribuer les interventions aux différents acteurs ? avec quel niveau de granularité ? Plutôt raisonner en terme d'atapes significtaives dans le processus de révision et une attribution. Là je me contredis car c'est un peu ce qui est déjà dans Stylo. 


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


**Limites de la démarche**

CHoix de xml paraît un peu lourd. Le json par exemple est plus facilement traitable. 



Le script est basé sur des regex il marche sauf 

- les suppressions (où il y a pas d'ajout dans le rdg)
- les citations dans le nom que c'est la même syntaxe (par exemple [-@machin])
- des fois les milestones ça reste des balises et des fois pas

Choisir de travailler sur la syntaxe markdown parce que c'est là dessus que travaillent les éditeurices de sens public. Et une partie de leur travail c'est de corriger le markdown. Même si ce n'est pas une pratique courante d'encoder du code en TEI, ici ça fait du sens. 








Milligan & Tinkle, Literary Editing in the Digital Age (2022).
Peter Shillingsburg, From Gutenberg to Google
Fredson Bowers, Textual and Literary Criticism (1959).


**Des trucs à checker :** 

- [x] les espaces autour de milestone et app 
- [ ] dans snauwaert les citations chelous avec plein de > il faut vérifier
- [x] laisser des rdg ou des lem vides ? Oui
- [x] reprendre les textes nettoyés et refaire le wdiff pour que ce soit bien propre
- [ ] on peut essayer d'améliorer le css du formulaire html
- [x] est-ce que je mets les resp ? Non je justifie
- [ ] bien vérifier que tout le header est complété avec cette histoire de revision desc et de timeline
- [ ] enlever les commentaires dans les xml
- [x] truc des espaces insécables

**Mes bugs :**

- [x] Attributs multi-valués je crois qu'il faut faire un for-each-group sa grand-mere
- [x] la xslt add-ids ramène des identifiants que je veux pas sur les ab c'est peut-être pas gênant 
- [x] gestion de méca dans review il faut seulement le rdg

**Reste à faire**

- [ ] déployer une github page
- [ ] améliorer le css et la xsl pour affichage du texte ? 
- [ ] écrire l'intro explicative du projet
- [ ] xml propres 
- [ ] transformation vers édition finale
- [ ] choisir le meilleur xml pour exemple dans le proto
- [ ] essayer d'ajouter un trux de resp
