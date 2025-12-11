#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script : diff_to_tei.py
Objectif : créer un apparat critique TEI à partir d’un fichier diff (txt)
           utilisant la notation [-...-] {+...+}.
Entrée  : comparaison.txt
Sortie  : apparat.xml
"""

import re
from xml.sax.saxutils import escape

def diff_to_tei(diff_text: str, wit_lem="#V1", wit_rdg="#V2") -> str:
    """
    Transforme le texte avec [-...-] {+...+} en TEI avec <app>, <lem>, <rdg>.
    """
    # Regex : capture suppression [- ... -] et ajout {+ ... +}
    pattern = re.compile(r"\[-(.*?)-\]\s*\{\+(.*?)\+\}", re.DOTALL)

    def replacer(match):
        deleted = escape(match.group(1).strip())
        added = escape(match.group(2).strip())
        return f"<app><lem wit=\"{wit_lem}\">{deleted}</lem><rdg wit=\"{wit_rdg}\">{added}</rdg></app>"

    # Appliquer le remplacement
    tei_body = pattern.sub(replacer, diff_text)

    # Nettoyage : espaces multiples → un seul espace
    tei_body = re.sub(r"\s{2,}", " ", tei_body)

    # Construction du document TEI complet
    tei_doc = f"""<TEI xmlns="http://www.tei-c.org/ns/1.0">
   <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main">Titre de l'article</title>
            <title type="sub">Sous-titre</title>
            <title type="sub">Édition comparée trouver un mieux titre</title>
            <author ref="balzac"></author>
            <principal xml:id="cg">GROMETTO Clara</principal>
            <respStmt>
               <resp>Sélection, alignement des versions et édition en ligne par</resp>
               <persName ref="#cg">
                  <forename>Clara</forename>
                  <surname>Grometto</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Édition de la version finale de l'article</resp>
               <orgName>
                  <ref target="https://www.sens-public.org/">Sens Public</ref>
               </orgName>
            </respStmt>
            <respStmt>
               <resp>Directrice de la revue Sens Public</resp>
               <persName ref="#mm">
                  <forename>Margot</forename>
                  <surname>Mellet</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Situation de la revue dans l'institution</resp><!-- mal dit -->
               <orgName>DLLF</orgName>
            </respStmt>
         </titleStmt>
         <publicationStmt>
            <publisher>Université de Montréal</publisher>
            <pubPlace>Montréal, Québec</pubPlace>
            <date when-iso="2025-12-15" type="date-de-rendu">15 décembre 2025</date>
         </publicationStmt>
         <sourceDesc>
            <biblStruct>
               <analytic>
                  <author>
                     <forename>James</forename>
                     <forename>H.</forename>
                     <surname>Coombs</surname>
                  </author>
                  <author>
                     <forename>Allen</forename>
                     <surname>Renear</surname>
                  </author>
                  <author>
                     <forename>Steven</forename>
                     <forename>J.</forename>
                     <surname>DeRose</surname>
                  </author>
                  <title level="a">Markup Systems and The Future of Scholarly Text
                     Processing</title>
                  <idno type="DOI">10.1145/32206.32209</idno>
                  <ref target="http://xml.coverpages.org/coombs.html">http://xml.coverpages.org/coombs.html</ref>
               </analytic>
               <monogr>
                  <title level="j">Revue Sens Public</title>
                  <imprint>
                     <date>2025</date>
                  </imprint>
                  <biblScope unit="volume">30</biblScope>
                  <biblScope unit="issue">11</biblScope>
                  <biblScope unit="page">933–947</biblScope>
               </monogr>
               <note>Encodage issu des sources stylo</note>
            </biblStruct>
            <listWit>
               <witness xml:id="V1">Premières épreuves à telle date <ptr target="lien vers la preview de la version"/></witness>
               <witness xml:id="V2">Secondes épreuves à telle date</witness>
               <witness xml:id="V3">troisièmes épreuves à telle date</witness>
            </listWit>
            
         </sourceDesc>
      </fileDesc>
      <encodingDesc>
         <editorialDecl>
            <p>L'alignement des version a été réalisé
               avec l'aide de l'algorithme de Dekker de <ref target="https://collatex.net/">Collatex</ref>.
               Cet alignement a été repris ensuite pour constituer l'édition critique et génétique qui suit.</p>
            <p>L'édition critique et l'alignement des témoins cherchent à permettre l'étude la plus
               précise possible de la variance et des similitudes entre l'antécédent publié dans la
               presse et la version roman :
               <list>
                  <item>La structuration du texte en paragraphes (&lt;p&gt;) a été abandonnée : les
                     textes sont insérés dans un conteneur &lt;ab&gt; et les changements de
                     paragraphes sont signalés par des &lt;milestone&gt;, pour que l'alignement des
                     versions puisse mettre en avant les variantes syntaxiques, lexicales ou
                     orthographiques. On considérera essentiellement les variations affectant la structure
                     syntaxique, l'ortho-typo ou le sémantisme.</item>
                  <item>Quand deux blocs dans les versions de texte se présentent comme trop
                     éloignés pour un alignement mot-à-mot mais peuvent être mis en parallèle pour
                     d'autres raisons (structures syntaxiques, thématiques, alignement des mots qui
                     suivent), ils seront encodés dans un même élément &lt;app&gt;. L'@corresp
                     portera la valeur générale "word-diff" ; et "add-words" si l'un des deux
                     témoins est significativement plus fourni que l'autre.</item>
                  <item>Les italiques et les petites capitales ont été rendues par la balise
                     &lt;hi&gt;, et si leur présence produit une nouvelle variante, l'@corresp
                     portera la valeur "rend".</item>
                  <!--<item>Prise de décision concernant les déplacements et les structures syntaxiques
                     en miroir : il revient à l'encodeur la décision de les encoder dans un seul
                     élément &lt;app&gt; (considérant alors un déplacement au sein du bloc,
                     l'inversion de l'ordre de deux groupes dans la phrase) ou dans deux éléments
                     &lt;app&gt; distincts (considérant alors une suppression à un endroit et un
                     ajout à un autre endroit du texte) en fonction de la portée du déplacement.
                     Dans les deux cas, si on observe le déplacement d'un terme ou d'un groupe de
                     mot dans la phrase l'@corresp portera la valeur "sentence-order".</item>-->
               </list></p>
            <p>La modélisation des corrections est basée sur les distinctions opérées par le <ref target="https://www.chicagomanualofstyle.org/book/ed18/frontmatter/toc.html">CMOS18</ref>.</p>
            <p>Pour chaque élément &lt;app&gt;, un attribut "@corresp" est utilisé pour préciser la
               nature de la correction. Les valeurs possibles pour cet attribut sont:<list>
                  <item xml:id="hard">modification d'ordre éditoriale</item>
                  <item xml:id="querie">suggestion à l'auteur</item>
                  <item xml:id="orth">correction orthographique</item>
                  <item xml:id="gram">correction concernant l'usage grammatical</item>
                  <item xml:id="punct">correction de ponctuation</item>
                  <item xml:id="titles">correction des titres et des noms propres</item>
                  <item xml:id="abbr">correction des abbréviations</item>
                  <item xml:id="nbr">correction des dates et nombres</item>
                  <item xml:id="add-note">ajout d'une note de bas de page</item>
                  <item xml:id="biblio">vérification des citations et des références</item>
                  <item xml:id="list-fig">vérification des listes et figures</item>
               </list></p>
            <p>Deux systèmes se superposent : un niveau de criticité de la vérification auctoriale. querie ou hard. <!--expliquer--></p>
            <segmentation>
               <p>Pour mieux aligner les textes et mettre en avant les variations entre les versions,
                  les paragraphes ne sont pas contenus dans des &lt;p&gt;. Le passage d'un
                  paragraphe à l'autre est signalé par un &lt;milestone unit="tei:p"/&gt; et par un
                  &lt;lb/&gt;. Cette méthode est suggérée par Beshero-Bondar, Cayless,
                  Vigilanti (2019: 3.10) <bibl>
                     <author>
                        <persName>Beshero-Bondar</persName>
                        <persName>Cayless</persName>
                        <persName>Viglianti</persName>
                     </author>
                     <title>Document Modeling with the TEI Critical Apparatus</title>
                     <date>2019</date>
                     <ref target="http://bit.ly/crit-app-panel"/>
                  </bibl></p>
            </segmentation>
         </editorialDecl>
         <projectDesc>
            <p>Encodage réalisé dans le cadre du cours de ..........</p>
         </projectDesc>
         <variantEncoding method="parallel-segmentation" location="internal"/>
      </encodingDesc>
      <profileDesc>
         <langUsage>
            <language ident="fr">French</language>
         </langUsage>
         <textDesc n="novel">
            <channel mode="w">print; part issues</channel>
            <constitution type="single"/>
            <derivation type="original"/>
            <domain type="art"/>
            <factuality type="fiction"/>
            <interaction type="none"/>
            <preparedness type="prepared"/>
            <purpose type="entertain" degree="high"/>
            <purpose type="inform" degree="medium"/>
         </textDesc>
         <abstract>
            <p>résumé de l'article</p>
          
         </abstract>
         <particDesc>
            <listPerson>
               <head>Liste des personnes ayant participé à la présente édition : </head>
               <person xml:id="aarsenault" role="editor">
                  <persName>
                     <forename>Adrien</forename>
                     <surname>Arsenault</surname>
                  </persName>
               </person>
            </listPerson>
         </particDesc>
        
      </profileDesc>
      <revisionDesc status="embargoed">
         <change when="1991-11-11" who="#LB">review version 2</change>
      </revisionDesc>
   </teiHeader>
  <text>
    <body>
      <p>{tei_body}</p>
    </body>
  </text>
</TEI>
"""
    return tei_doc


def main():
    input_file = "./textes/comparaison.txt"
    output_file = "apparat.xml"

    # Lecture du fichier source
    with open(input_file, "r", encoding="utf-8") as f:
        diff_text = f.read()

    # Conversion en TEI
    tei_xml = diff_to_tei(diff_text)

    # Écriture du fichier TEI résultant
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tei_xml)

    print(f"✅ Good : {output_file}")


if __name__ == "__main__":
    main()
