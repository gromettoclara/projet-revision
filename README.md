# projet-revision

La pratique actuelle de l’édition hérite de siècles de réflexions, souvent implicites, s’incarnant dans des protocoles, des outils et des savoir-faire cependant dénués de charge symbolique. Parmi eux, la révision de texte, thématique peu abordée dans la littérature, pratique peu valorisée et déléguée aux « petites mains » (Mellet 2023), plus récemment à des algorithmes, est une zone aveugle de la médiation éditoriale. C'est pourtant un impensé que le passage à un autre espace de pratique questionne à l'aune de la redéfinition du texte désormais numérique. Écrire, c'est avant tout réécrire, d'autant plus clairement dans le paradigme numérique (Kirschenbaum 2016). Au fil des siècles, la révision s’est institutionnalisée dans un protocole rigoureux avec des étapes successives d’épreuves et l'usage de signes typographiques normalisés pour catégoriser suppressions, ajouts, déplacements ou mise en page (André 1998). Ces pratiques témoignent d’un savoir-faire éditorial riche. Le passage au numérique entraîne une double perte : celle des annotations manuscrites et celle de la maîtrise des versions, fragilisée par leur prolifération potentiellement infinie (Vitali-Rosati 2024). Par ailleurs, la transposition des techniques de conception itérative et de publication Web à l'édition scientifique ou littéraire (Fauchié et Parisot 2018) fait muter la mythologie entourant l'écriture. Le concept de texte même se trouve alors bouleversé par son existence numérique, sa dimension matérielle s'y trouve réinvestie, soulignant sa fabrique collective et multi-agentielle (Monjour et Sauret 2021; Fauchié 2024; Barad 2003). 

De la plume et de l’encre rouge des scriptoria médiévaux aux fonctions de suivi des modifications des traitements de texte, la révision et l’annotation accompagnent la production du savoir depuis les débuts de l’ère typographique. Or, les pratiques de révision dans l’environnement numérique ont été pensées à partir du modèle proposé par Microsoft Word, qui présente de nombreuses limites : allers-retours par mail, multiplication des fichiers, écrasement des versions et de la richesse du travail d'annotation. Dans le système de commentaire et suggestion du traitement de texte, les modifications sont toutes au même niveau. Le format propriétaire docx constitue aujourd'hui, si ce n'est la seule alternative, du moins la plus utilisée et celle considérée par défaut par les éditeur·ices pour travailler avec les auteurs. Cela dit, le système présente un avantage certain : celui d'autoriser le dialogue entre l'éditeur·ice et les auteur·ices. 

Nous proposons ici une alternative aux formats propriétaire, en expérimentant un prototype d'instrument de suivi éditorial. L'explicitation des transformations, le suivi des modifications et l'arrimage à un système de versionnage rationnel, dans le respect des pratiques éditoriales concrètes, en constituent les critères.

## Présentation du corpus à éditer

Cette expérimentation prend appui sur un corpus d'articles (cinq environ, à ajuster) issus de la revue Sens public, une publication francophone qui se distingue par sa réflexion sur les enjeux épistémologiques des pratiques éditoriales, ce dont témoigne son adoption de l'éditeur de texte sémantique Stylo à la base de son workflow. Cela qui permet de capturer et de conserver plusieurs versions d'un même article, offrant ainsi une fenêtre sur le travail collaboratif qui s'opère entre auteur.ices, éditeur.ices et réviseur.euses. 

Le corpus que je souhaite éditer se compose donc de plusieurs versions d'articles qui montrent concrètement les interventions éditoriales successives. Pour des questions de faisabilité, nous nous limiterons à trois versions, quitte à applatir plusieurs versions en une seule. Si besoin, il est aussi possible de trouver des articles en cours de rédaction et d'effectuer nous-même le travail de révision.

## Choix éditoriaux : une édition qui montre et permet le travail éditorial sur le texte 

Le prototype que nous proposons veut mettre en évidence et véritablement *permettre* la dimension dialogique du travail éditorial, espace de négociation entre différentes expertises. L'édition scientifique tient sur un équilibre entre le respect de la voix de l'auteur et la nécessité d'assurer la qualité, la cohérence et la lisibilité du texte publié. Le travail de relecture et annotation devrait alors documenter les changements effectués mais aussi leur nature et leur statut dans la hiérarchie des décisions éditoriales, afin d'être efficace, dans le cadre de rédaction scientifique en SHS. 

## Modélisation des choix 

Notre travail de modélisation repose sur une typologie des changements qui distingue deux grands principes fondamentaux dans la pratique éditoriale imprimée, qui serviront ici de point de départ et de métaphore. D'une part, les corrections "au stylo" ou "dures" correspondent aux interventions qui relèvent de la prérogative directe de l'éditeur et qui sont destinées au typographe ou à la personne en charge mise en forme finale. Ces corrections concernent principalement la structuration du texte en relation avec les transformations nécessaires à la mise en page, et l'application des conventions orthotypographiques. Il s'agit par exemple de la normalisation de l'usage des majuscules, de la ponctuation, ou encore de l'application de la feuille de style de la revue. Ces interventions, bien que substantielles, sont considérées comme relevant de l'autorité éditoriale et ne requièrent généralement pas l'approbation explicite de l'auteur. Les corrections dites "au crayon" suggestions adressées à l'auteur qui nécessitent une validation avant d'être intégrées au texte définitif. Cette catégorie se subdivise en plusieurs types d'interventions : 

- changement d'un mot ou groupe de mot
- déplacement d'un mot ou groupe de mot
- ajout d'un mot ou groupe de mot
- doute sur l'orthographe d'un mot
- ajout d'un commentaire

À noter que cette typologie n'est pas exhaustive, et pourra être rafinée au fil de l'encodage. 

## Des pistes de choix de format et de technique d’édition

Pour structurer les modifications textuelles, il est possible d'utiliser Collatex, qui permet de comparer différentes versions d'un même texte et d'identifier leurs variantes. Cette analyse serait complétée par une annotation manuelle pour corriger les sorties du script Python et pour catégoriser les changements détectés. La démarche méthodologique repose sur un détournement de l'encodage TEI, et notamment le module initialement déstiné à l'édition critique de textes anciens, avec les éléments `<app>` pour appareil critique et `<lem>` pour le lemme, que nous réorientons vers la modélisation des variations éditoriales. Nous nous approprions ainsi un cadre conceptuel et technique déjà largement utilisé pour encoder les variations textuelles. 

Le `lem` indique la décision finale, qu'elle soit celle de l'éditeur ou de l'auteur. L'appareil "critique" (ou plutôt dans ce cas appareil "révisé") enregistre les versions rejetées. Chaque version (qu'elle soit `lem` ou `rdg`) possède en attribut une version datée et une responsabilité. 

```xml
<app xml:id="app-A" corresp="#change-words">
    <lem resp="#auteur" wit="#manus">texte original</lem>
    <rdg resp="#editeur1" wit="#epreuve1">texte suggéré</rdg>
</app>
```
La typification de changements ainsi que les versions seront renseignées dans le TEI-header. 

Après cet encodage TEI partiellement automatisé, l'idée serait de développer une interface basée sur XForm qui permettrait de visualiser les changements dits "au stylo" et de gérer les changements dits "au crayon", en suspens. 
Une telle interface offrirait à l'auteur la possibilité de parcourir les suggestions éditoriales, et d'accepter ou de refuser chaque modification. Chaque action modifie le document XML en direct, met à jour le `<lem>` et l'attribut @change. Cela permettrait de créer un workflow de révision qui garde une trace fine des transformations du texte, tout en permettant une interaction entre auteur.ices et éditeur.ices. 

```xml
<app xml:id="app-A" corresp="#change-words" change="#auteur">
    <lem resp="#editeur1" wit="#epreuve1">texte suggéré</lem>
    <rdg resp="#auteur" wit="#manus">texte original</rdg>
</app>
```
## Bibliographie 

André, Jacques. 1998. « Petite histoire des signes de correction typographique ». *Cahiers GUTenberg*, nᵒ 31: 45‑59. [https://doi.org/10.5802/cg.253](https://doi.org/10.5802/cg.253).

Barad, Karen. 2003. « Posthumanist Performativity: Toward an Understanding of How Matter Comes to Matter ». *Signs 28* (3): 801‑31. [https://doi.org/10.1086/345321](https://doi.org/10.1086/345321).

Fauchié, Antoine. 2024. « Fabriquer des éditions, éditer des fabriques : reconfiguration des processus techniques éditoriaux et nouveaux modèles épistémologiques ». Thèse de doctorat, Université de Montréal.

Fauchié, Antoine, et Thomas Parisot. 2018. « Repenser les chaînes de publication par l’intégration des pratiques du développement logiciel ». *Sciences du Design* 8 (2): 45‑56. [https://doi.org/10.3917/sdd.008.0045](https://doi.org/10.3917/sdd.008.0045).

Kirschenbaum, Matthew G. 2016. *Track Changes: A Literary History of Word Processing*. Illustrated édition. Belknap Press.

Mellet, Margot. 2023. « Les Petites Mains de l’édition : Réflexion Pour Des Environnements Éditoriaux Équitables, Pluriels et Inclusifs ». 

Monjour, Servanne, et Nicolas Sauret. 2021. « Pour Une Gittérature : L’autorité à l’épreuve Du Hack ». *Revue XXI-XX*, Classiques Garnier, nᵒ 2.

Vitali Rosati, Marcello. 2024. « Du Savoir-Faire de La révision d’épreuves à l’abrutissement Du Suivi de Modification de Word ». *Culture Numérique. Pour Une Philosophie Du Numérique.* [http://blog.sens-public.org/marcellovitalirosati/revision.html](http://blog.sens-public.org/marcellovitalirosati/revision.html.).
