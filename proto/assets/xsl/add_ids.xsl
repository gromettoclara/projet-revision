<xsl:stylesheet 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    version="2.0">
    
    
    <xsl:variable name="choice-prefix" select="'choice-'"/>
    <xsl:variable name="corr-prefix" select="'corr-'"/>
    <xsl:variable name="sic-prefix" select="'sic-'"/>
    
    <xsl:output method="xml" encoding="UTF-8"/>
    
    <xsl:character-map name="mapEntities">
        <xsl:output-character character="&amp;" string="&amp;"/>
        <xsl:output-character character="&lt;" string="&lt;"/>
        <xsl:output-character character="&gt;" string="&gt;"/>
    </xsl:character-map>
    
    <xsl:template match="/">
        
        <xsl:variable name="titre" select="replace(//tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title[@type='main'], ' ', '')"/>
        <xsl:variable name="fileName" select="concat($titre, '.xml')"/>
        
        <xsl:result-document href="../../../00editionFinale/{$fileName}" method="xml" encoding="UTF-8">
        
        <xsl:processing-instruction name="xml-model">
        href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng"
        type="application/xml"
        schematypens="http://relaxng.org/ns/structure/1.0"
    </xsl:processing-instruction>
        
        <xsl:processing-instruction name="xml-model">
        href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng"
        type="application/xml"
        schematypens="http://purl.oclc.org/dsdl/schematron"
    </xsl:processing-instruction>

        <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </xsl:copy>
        </xsl:result-document>
    </xsl:template>
    
    
    <xsl:template match="tei:*">
        <xsl:copy>
            
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </xsl:copy>
        
    </xsl:template>
    
    
    <xsl:template match="text()">
        <xsl:value-of
            select="."/>
    </xsl:template>
    
    
    <xsl:template match="tei:choice">
        <xsl:copy>
            <xsl:for-each select="@*">
                <xsl:if test="name() != 'xml:id'">
                    <xsl:attribute name="{name()}">
                        <xsl:value-of select="."/>
                    </xsl:attribute>
                </xsl:if>
            </xsl:for-each>
            
            <xsl:attribute name="xml:id">
                <xsl:value-of select="$choice-prefix || (count(preceding::tei:choice) + 1)"/>
            </xsl:attribute>
            
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    
    <xsl:template match="tei:corr">
        <xsl:copy>
            <xsl:for-each select="@*">
                <xsl:if test="name() != 'xml:id'">
                    <xsl:attribute name="{name()}">
                        <xsl:value-of select="."/>
                    </xsl:attribute>
                </xsl:if>
            </xsl:for-each>
            
            <xsl:attribute name="xml:id">
                <xsl:value-of select="$corr-prefix || (count(preceding::tei:corr) + 1)"/>
            </xsl:attribute>
            
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="tei:sic">
        <xsl:copy>
            <xsl:for-each select="@*">
                <xsl:if test="name() != 'xml:id'">
                    <xsl:attribute name="{name()}">
                        <xsl:value-of select="."/>
                    </xsl:attribute>
                </xsl:if>
            </xsl:for-each>
            
            <xsl:attribute name="xml:id">
                <xsl:value-of select="$sic-prefix || (count(preceding::tei:sic) + 1)"/>
            </xsl:attribute>
            
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
            

    
    
</xsl:stylesheet>