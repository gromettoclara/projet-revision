#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from xml.sax.saxutils import escape

def diff_to_tei(diff_text: str, wit_lem="#V1", wit_rdg="#V2") -> str:
    """
    Transforme le texte avec [-...-] {+...+} en TEI avec <app>, <lem>, <rdg>.
    """
    pattern = re.compile(r"\[-(.*?)-\]\s*\{\+(.*?)\+\}", re.DOTALL)

    def replacer(match):
        deleted = escape(match.group(1).strip())
        added = escape(match.group(2).strip())
        return f"<app><lem wit=\"{wit_lem}\">{deleted}</lem><rdg wit=\"{wit_rdg}\">{added}</rdg></app>"

    tei_body = pattern.sub(replacer, diff_text)

    tei_body = re.sub(r"\s{2,}", " ", tei_body)

    tei_doc = f"""<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>

<!DOCTYPE TEI [
     <!ENTITY nbsp '&#160;'>

]>

<TEI xmlns="http://www.tei-c.org/ns/1.0">
   <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main">Titre de l'article</title>
            <title type="sub">Sous-titre</title>
            <title type="sub">Édition comparée de deux moments du texte</title>
            <principal xml:id="cg">GROMETTO Clara</principal>
            <respStmt>
               <resp>Sélection, alignement des versions et prototype pour comparaison</resp>
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
               <persName ref="#gm">
                  <forename>Gérard</forename>
                  <surname>Wormser</surname>
               </persName>
            </respStmt>
            <respStmt>
               <resp>Rattachement institutionnel</resp>
               <orgName>DLLF</orgName>
            </respStmt>
         </titleStmt>
         <publicationStmt>
            <publisher>Université de Montréal</publisher>
            <pubPlace>Montréal, Québec</pubPlace>
            <date when-iso="2025-12-15" type="date-de-rendu">25 décembre 2025</date>
         </publicationStmt>
         <sourceDesc>
            <biblStruct>
               <!--ref de l'article-->
               <note>Encodage XML à partir des sources stylo : versions préparatoires de l'article</note>
            </biblStruct>
            <listWit>
               <witness xml:id="V1">Version du <date when-iso="date" type="versionning" resp="#truc">date</date><ptr
                  target="url"/></witness>
               <witness xml:id="V2">Version du <date when-iso="date" type="versionning" resp="#truc">date</date> <desc>desc</desc><ptr
                  target="url"/></witness>
            </listWit>
         </sourceDesc>
      </fileDesc>
      <encodingDesc>
         <editorialDecl>
            <p>L'alignement des versions a été réalisé avec l'aide de l'algorithme <code>wdiff</code>. Cet alignement a été répris et traité par un script en python "maison", pour constituer un premier encodage en XML-TEI. Ce premier encodage a été corrigé à la main, puis une feuille de style XSLT a été appliquée pour rajouter des identifiants à tous les éléments &lt;app&gt;. </p>
            <p>Voici les principes adoptés pour l'alignement : <list>
               <item>La structuration du texte en paragraphes (&lt;p&gt;) a été abandonnée : les
                  textes sont insérés dans un conteneur &lt;ab&gt; et les changements de
                  paragraphes sont signalés par des &lt;milestone&gt;, et les retours simples ont été supprimé lors d'une étape de nettoyage des articles (on estime qu'ils servent uniquement la lisbilité du code en écriture et n'ont pas d'impact sur la suite de la chaîne).</item>
               <item>autre item</item>
               <item>Étant donné que les éditeurs travaillent sur du code en markdown, on a comparé les articles en markdown. Il y a pas encore d'aspect </item>
               <!--<item>autre item éventuellement</item>-->
            </list></p>
            <p>La modélisation des corrections est basée sur les distinctions opérées par le <ref
               target="https://www.chicagomanualofstyle.org/book/ed18/frontmatter/toc.html"
               >CMOS18</ref> et sur un entretien avec l'éditrice de la revue HN Florence.</p>
            <p>Deux systèmes se superposent : un niveau de criticité de vérification et une expertise métier reliée.
               querie ou hard. <!--expliquer--></p>
            <p>Pour chaque élément &lt;app&gt;, un attribut "@corresp" est utilisé pour préciser la
               nature de la correction. Les valeurs possibles pour cet attribut sont:<list>
                  <item xml:id="meca">Corrections mécaniques : mécanique de la langue, mécanique du code, mécanique de la pipeline, fluidité de la lecture : on peut diviser en sous-catégories.
                     
                     <list><item xml:id="orth">orthographe -- rectifications d’erreurs typographiques, harmonisation des graphies.</item>
                        <item xml:id="unif">Casse, capitalisation, abréviations, ponctuation, faces -- questions d'uniformisation des majuscules/minuscules, dés abréviations, des signes de ponctuation, espaces insécables. des changement qui peuvent se faire en masse.</item>
                        <item xml:id="num">Numérotation, listes, dates, chiffres -- correction ou cohérence des éléments numériques.</item>
                        <item xml:id="gram">Grammaire et Syntaxe -- accord, conjugaison, structure de phrases, impropriétés syntaxiques.</item>
                        <item xml:id="md">Code markdown -- harmonisation et correction pour rentrer sans frottement dans la chaîne de conversion.</item></list></item>
                  
                  <item xml:id="subst">Modifications substantives : sémantiques, rhétoriques ou stylistique : les so
                     <list><item xml:id="puct">ponctuation -- virgules, points, tirets, guillemets, usage des italiques avec une incidence sur le sens ou le style.</item>
                        <item xml:id="change">Substitutions lexicales non mécaniques.</item>
                        <item xml:id="add">Ajouts de mots/phrases.</item>
                        <item xml:id="supp">Suppressions de mots/phrases.</item>
                        <item xml:id="move">Déplacement de mots/phrases.</item>
                        <item xml:id="reformulation">Réécriture ponctuelle de segments.</item></list></item>
                  <item xml:id="para">Autour du texte -- interventions sur les références et paratexte éditorial
                     <list><item xml:id="fn">Ajouts d'une note de bas de page éditoriale.</item>
                        <item xml:id="quote">Correction de citations.</item>
                        <item xml:id="ref">Vérification de fond sur la bibliographie.</item></list>
                  </item>
               </list></p>
            
            <segmentation>
               <p>Pour mieux aligner les textes et mettre en avant les variations entre les
                  versions, les paragraphes ne sont pas contenus dans des &lt;p&gt;. Le passage d'un
                  paragraphe à l'autre est signalé par un &lt;milestone unit="tei:p"/&gt; et par un
                  &lt;lb/&gt;. Cette méthode est suggérée par Beshero-Bondar, Cayless, Vigilanti
                  (2019: 3.10) <bibl>
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
            <p>Encodage réalisé dans le cadre du cours de littérature et culture numérique FRA6730 qui s'est tenu à l'automne 2025.</p>
         </projectDesc>
         <variantEncoding method="parallel-segmentation" location="internal"/>
      </encodingDesc>
      <profileDesc>
         <langUsage>
            <language ident="fr">French</language>
         </langUsage>
         <textDesc>
            <channel mode="w">Stylo <ptr target="https://stylo.huma-num.fr/"/>; éditeur collaboratif sémantique en markdown</channel>
            <constitution/>
            <derivation type="revision"/>
            <domain type="education"/>
            <factuality type="fact"/>
            <interaction/>
            <preparedness type="revised"/>
            <purpose type="inform" degree="high"/>
         </textDesc>
         <textClass>
            <keywords scheme="#fr_RAMEAU">
               <!--mots-clés contrôlés-->
            </keywords>
            <keywords >
               <!--liste de mots clés-->
            </keywords>
         </textClass>
         <abstract>
            <p>le résumé</p>
         </abstract>
         <particDesc>
            <listPerson>
               <head>Liste des personnes ayant participé à l'écriture de l'article</head>
               <!--liste des personnes-->
            </listPerson>
         </particDesc>
         
      </profileDesc>
      <!--<revisionDesc status="submitted">
         <change when-iso="2025-12-25" who="#???">review de la version 1.1</change>
      </revisionDesc>-->
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

    with open(input_file, "r", encoding="utf-8") as f:
        diff_text = f.read()

    tei_xml = diff_to_tei(diff_text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tei_xml)

    print(f"Good : {output_file}")


if __name__ == "__main__":
    main()
