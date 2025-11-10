---
title: projet-révision
subtitle: note d'intention
author: GROMETTO Clara
date: 20 Novembre 2025
bibliography: biblio.bib
nocite: |
  @*
---


La pratique actuelle de l’édition hérite de siècles de réflexions, souvent implicites, s’incarnant dans des protocoles, des outils et des savoir-faire cependant dénués de charge symbolique. Parmi eux, la révision de texte, thématique peu abordée dans la littérature, pratique peu valorisée et déléguée aux « petites mains » [@melletPetitesMainsLedition2023], plus récemment à des algorithmes, est une zone aveugle de la médiation éditoriale. C'est pourtant un impensé que le passage à un autre espace de pratique questionne à l'aune de la redéfinition du texte désormais numérique. Écrire, c'est avant tout réécrire, d'autant plus clairement dans le paradigme numérique [@kirschenbaumTrackChangesLiterary2016]. Au fil des siècles, la révision s’est institutionnalisée dans un protocole rigoureux avec des étapes successives d’épreuves et l'usage de signes typographiques normalisés pour catégoriser suppressions, ajouts, déplacements ou mise en page [@andrePetiteHistoireSignes1998]. Ces pratiques témoignent d’un savoir-faire éditorial riche. Le passage au numérique entraîne une double perte : celle des annotations manuscrites et celle de la maîtrise des versions, fragilisée par leur prolifération potentiellement infinie (Vitali-Rosati 2024). Par ailleurs, la transposition des techniques de conception itérative et de publication Web à l'édition scientifique ou littéraire [@vitalirosatiSavoirfaireRevisionDepreuves2024] fait muter la mythologie entourant l'écriture. Le concept de texte même se trouve alors bouleversé par son existence numérique, sa dimension matérielle s'y trouve réinvestie, soulignant sa fabrique collective et multi-agentielle [@monjourPourGitteratureLautorite2021; @fauchieFabriquerEditionsEditer2024; @baradPosthumanistPerformativityUnderstanding2003]. 

De la plume et de l’encre rouge des scriptoria médiévaux aux fonctions de suivi des modifications des traitements de texte, la révision et l’annotation accompagnent la production du savoir depuis les débuts de l’ère typographique. Or, les pratiques de révision dans l’environnement numérique ont été pensées à partir du modèle proposé par Microsoft Word, qui présente de nombreuses limites : allers-retours par mail, multiplication des fichiers, écrasement des versions et de la richesse du travail d'annotation. Dans le système de commentaires et suggestions du traitement de texte, les modifications sont toutes au même niveau. Le format propriétaire docx constitue aujourd'hui, si ce n'est la seule alternative, du moins la plus utilisée et celle considérée par défaut par les éditeur·ices pour travailler avec les auteur·ices. Cela dit, le système présente un avantage certain : celui d'autoriser le dialogue entre l'éditeur·ice et les auteur·ices. 

Nous proposons ici une alternative aux formats propriétaires, en expérimentant un prototype d'instrument de suivi éditorial. L'explicitation des transformations, le suivi des modifications et l'arrimage à un système de versionnage rationnel, dans le respect des pratiques éditoriales concrètes, en constituent les critères.

## Présentation du corpus à éditer

Cette expérimentation prend appui sur un corpus d'articles (cinq environ, à ajuster) issus de la revue Sens public, une publication francophone qui se distingue par sa réflexion sur les enjeux épistémologiques des pratiques éditoriales, ce dont témoigne son adoption de l'éditeur·ice de texte sémantique Stylo à la base de son workflow. Cela qui permet de capturer et de conserver plusieurs versions d'un même article, offrant ainsi une fenêtre sur le travail collaboratif qui s'opère entre auteur·ices, éditeur·ices et réviseur·euses. 

Le corpus que je souhaite éditer se compose donc de plusieurs versions d'articles qui montrent concrètement les interventions éditoriales successives. Pour des questions de faisabilité, nous nous limiterons à trois versions, quitte à applatir plusieurs versions en une seule. Si besoin, il est aussi possible de trouver des articles en cours de rédaction et d'effectuer nous-mêmes le travail de révision.

## Choix éditoriaux : une édition qui montre et permet le travail éditorial sur le texte 

Le prototype que nous proposons veut mettre en évidence et véritablement *permettre* la dimension dialogique du travail éditorial, espace de négociation entre différentes expertises. L'édition scientifique tient sur un équilibre entre le respect de la voix de l'auteur·ice et la nécessité d'assurer la qualité, la cohérence et la lisibilité du texte publié. Le travail de relecture et annotation devrait alors documenter les changements effectués mais aussi leur nature et leur statut dans la hiérarchie des décisions éditoriales, afin d'être efficace, dans le cadre de rédaction scientifique en SHS. 

## Modélisation des choix 

Notre travail de modélisation repose sur une typologie des changements qui distingue deux grands principes fondamentaux dans la pratique éditoriale imprimée, qui serviront ici de point de départ et de métaphore. D'une part, les corrections "au stylo" ou "dures" correspondent aux interventions qui relèvent de la prérogative directe de l'éditeur·ice et qui sont destinées au typographe ou à la personne en charge de la mise en forme finale. Ces corrections concernent principalement la structuration du texte en relation avec les transformations nécessaires à la mise en page, et l'application des conventions orthotypographiques. Il s'agit par exemple de la normalisation de l'usage des majuscules, de la ponctuation, ou encore de l'application de la feuille de style de la revue. Ces interventions, bien que substantielles, sont considérées comme relevant de l'autorité éditoriale et ne requièrent généralement pas l'approbation explicite de l'auteur·ice. Les corrections dites "au crayon" suggestions adressées à l'auteur·ice qui nécessitent une validation avant d'être intégrées au texte définitif. Cette catégorie se subdivise en plusieurs types d'interventions : 

- changement d'un mot ou groupe de mots
- déplacement d'un mot ou groupe de mots
- ajout d'un mot ou groupe de mots
- doute sur l'orthographe d'un mot
- ajout d'un commentaire

À noter que cette typologie n'est pas exhaustive, et pourra être rafinée au fil de l'encodage. 

## Des pistes de choix de format et de technique d’édition

Pour structurer les modifications textuelles, il est possible d'utiliser Collatex, qui permet de comparer différentes versions d'un même texte et d'identifier leurs variantes. Cette analyse serait complétée par une annotation manuelle pour corriger les sorties du script Python et pour catégoriser les changements détectés. La démarche méthodologique repose sur un détournement de l'encodage TEI, et notamment le module initialement destiné à l'édition critique de textes anciens, avec les éléments `<app>` pour appareil critique et `<lem>` pour le lemme, que nous réorientons vers la modélisation des variations éditoriales. Nous nous approprions ainsi un cadre conceptuel et technique déjà largement utilisé pour encoder les variations textuelles. 

Le `lem` indique la décision finale, qu'elle soit celle de l'éditeur·ice ou de l'auteur·ice. L'appareil "critique" (ou plutôt dans ce cas appareil "révisé") enregistre les versions rejetées. Chaque version (qu'elle soit `lem` ou `rdg`) possède en attribut une version datée et une responsabilité. 

```xml
<app xml:id="app-A" corresp="#change-words">
    <lem resp="#auteur" wit="#manus">texte original</lem>
    <rdg resp="#editeur1" wit="#epreuve1">texte suggéré</rdg>
</app>
```
La typification de changements ainsi que les versions seront renseignées dans le TEI-header. 

Après cet encodage TEI partiellement automatisé, l'idée serait de développer une interface basée sur XForm qui permettrait de visualiser les changements dits "au stylo" et de gérer les changements dits "au crayon", en suspens. 
Une telle interface offrirait à l'auteur·ice la possibilité de parcourir les suggestions éditoriales, et d'accepter ou de refuser chaque modification. Chaque action modifie le document XML en direct, met à jour le `<lem>` et l'attribut `@change`. Cela permettrait de créer un workflow de révision qui garde une trace fine des transformations du texte, tout en permettant une interaction entre auteur.ices et éditeur.ices. 

```xml
<app xml:id="app-A" corresp="#change-words" change="#auteur">
    <lem resp="#editeur1" wit="#epreuve1">texte suggéré</lem>
    <rdg resp="#auteur" wit="#manus">texte original</rdg>
</app>
```

## Bibliographie