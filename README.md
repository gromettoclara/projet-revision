# projet-revision

Proposition en lien avec mon sujet de thèse. 

La pratique actuelle de l’édition hérite de siècles de réflexions, souvent implicites, s’incarnant dans des protocoles, des outils et des savoir-faire cependant dénués de charge symbolique. Parmi eux, la révision de texte, thématique peu abordée dans la littérature, pratique peu valorisée et déléguée aux « petites mains » [@melletPetitesMainsLedition2023], plus récemment à des algorithmes, est une zone aveugle de la médiation éditoriale. C'est pourtant un impensé que le passage à un autre espace de pratique questionne à l'aune de la redéfinition du texte désormais numérique. Écrire, c'est avant tout réécrire, d'autant plus clairement dans le paradigme numérique [@kirschenbaumTrackChangesLiterary2016]. Au fil des siècles, la révision s’est institutionnalisée dans un protocole rigoureux avec des étapes successives d’épreuves et l'usage de signes typographiques normalisés pour catégoriser suppressions, ajouts, déplacements ou mise en page [@andrePetiteHistoireSignes1998]. Ces pratiques témoignent d’un savoir-faire éditorial riche. Le passage au numérique entraîne une double perte : celle des annotations manuscrites et celle de la maîtrise des versions, fragilisée par leur prolifération potentiellement infinie [@vitalirosatiSavoirfaireRevisionDepreuves2024]. Par ailleurs, la transposition des techniques de conception itérative et de publication Web à l'édition scientifique ou littéraire [@fauchieRepenserChainesPublication2018] fait muter la mythologie entourant l'écriture. Le concept de texte même se trouve alors bouleversé par son existence numérique, sa dimension matérielle s'y trouve réinvestie, soulignant sa fabrique collective et multi-agentielle [@monjourPourGitteratureLautorite2021 ; @fauchieFabriquerEditionsEditer2024 ; @baradPosthumanistPerformativityUnderstanding2003]. 

De la plume et de l’encre rouge des scriptoria médiévaux aux fonctions de suivi des modifications des traitements de texte, la révision et l’annotation accompagnent la production du savoir depuis les débuts de l’ère typographique. Les pratiques de révision dans l’environnement numérique ont été pensées à partir du modèle du traitement de texte. Allers-retour, multiplication des fichiers et des mails, formats propriétaires, perte de la richesse du travail de correction. Mais un avantage certain : permettre le dialogue entre l'éditeur et l'auteur. 

Expérimentation d'un prototype d'instrument de suivi éditorial. L'explicitation des transformations, le suivi des modifications et l'arrimage à un système de versionnage rationnel, dans le respect des pratiques éditoriales concrètes, en constituent les critères.

## Présentation du corpus à éditer

Cette expérimentation prend appui sur un corpus d'articles (cinq environ, à ajuster) issus de la revue Sens public, une publication francophone dont la particularité réside dans son utilisation de l'éditeur de texte sémantique Stylo, ce qui permet de capturer et de conserver plusieurs versions d'un même article, offrant ainsi une fenêtre sur le travail collaboratif qui s'opère entre auteur.ices, éditeur.ices et réviseur.euses. Sens public est une revue en SHS en libre accès, fondée en 2003, qui se distingue par son engagement envers les humanités numériques et sa réflexion sur les enjeux épistémologiques des pratiques éditoriales, ce dont témoigne son adoption de Stylo à la base de son workflow.

Le corpus que je souhaite éditer se compose donc de plusieurs versions d'articles qui montrent concrètement les interventions éditoriales successives. Pour des questions de faisabilité, nous nous limiteront à trois versions, quitte à applatir plusieurs versions en une seule. Si besoin, il est aussi possible de trouver des articles en cours de rédaction et d'effectuer moi-même le travail de révision.

## Choix éditoriaux : une édition qui montre et permet le travail éditorial sur le texte 

Mettre en évidence et permettre la dimension dialogique du travail éditorial, espace de négociation entre différentes expertises. Tenir l'équilibre délicat entre le respect de la voix de l'auteur et la nécessité d'assurer la qualité, la cohérence et la lisibilité du texte publié. Documenter les changements effectués mais aussi leur nature et leur statut dans la hiérarchie des décisions éditoriales. 

## Modélisation des choix 

Mon travail de modélisation repose sur une typologie des changements qui distingue deux grands principes fondamentaux dans la pratique éditoriale. D'une part, les corrections que je qualifie "au stylo" ou "dures" correspondent aux interventions qui relèvent de la prérogative directe de l'éditeur et qui sont destinées au typographe ou à la personne en charge mise en forme finale. Ces corrections concernent principalement la structuration du texte en relation avec les transformations nécessaires à la mise en page, ou l'application des conventions orthotypographiques. Il s'agit par exemple de la normalisation de l'usage des majuscules, de la ponctuation, ou encore de l'application de la feuille de style de la revue. Ces interventions, bien que substantielles, sont considérées comme relevant de l'autorité éditoriale et ne requièrent généralement pas l'approbation explicite de l'auteur. Les corrections dites "au crayon" suggestions adressées à l'auteur qui nécessitent une validation avant d'être intégrées au texte définitif. Cette catégorie se subdivise en plusieurs types d'interventions : 

- changement d'un mot ou groupe de mot
- déplacement d'un mot ou groupe de mot
- ajout d'un mot ou groupe de mot
- doute sur l'orthographe d'un mot
- ajout d'un commentaire

À noter que cette typologie n'est pas exhaustive, et pourra être rafinée.

## Des pistes de choix de format et de technique d’édition

Pour identifier et structurer les transformations textuelles, il est possible Collatex, qui permet de comparer différentes versions d'un même texte et d'identifier leurs variantes. Cette analyse serait complétée par une annotation manuelle pour catégoriser les changements détectés. La démarche méthodologique repose sur un détournement de l'encodage TEI, et notamment le module initialement déstiné à l'édition critique de textes anciens, avec les éléments "app" pour appareil critique et "lem" pour lemme, que je réoriente vers la modélisation des processus éditoriaux. Je m'approprie ainsi un cadre conceptuel et technique déjà largement utilisé pour encoder les variations textuelles. 

Le "lem" c'est la décision finale, qu'elle soit de l'éditeur ou de l'auteur. L'appareil "critique" ou plutôt dans ce cas appareil "révisé" enregistre les versions rejetées. Chaque version (lem ou rdg) enregistre une version datée et une responsabilité. 

Après cet encodage TEI partiellement automatisé, l'idée serait de développer une interface basée sur XForm qui permettrait de visualiser les changements dits "au stylo" et de gérer les changements dits "au crayon". Une telle interface offrirait à l'auteur la possibilité de parcourir les suggestions éditoriales, et d'accepter ou de refuser chaque modification. Chaque changement créerait un nouveau "lem" constitué du "rdg" proposé ou de l'ancien "lem" qu'on a gardé et on renseigne la version précédente dans un app. Cela permettrait de créer un workflow de révision qui garde une trace fine des transformations du texte, tout en permettant une interaction entre auteur.ices et éditeur.ices. 
