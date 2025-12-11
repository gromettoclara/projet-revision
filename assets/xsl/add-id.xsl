<xsl:stylesheet 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    version="3.0">
    

    <xsl:mode on-no-match="shallow-copy"/>
    

    <xsl:variable name="app-prefix" select="'app-'"/>
    <xsl:variable name="rdg-prefix" select="'rdg-'"/>
    <xsl:variable name="lem-prefix" select="'lem-'"/>
    
    <xsl:template match="tei:app">
        <xsl:copy>
            <xsl:attribute name="xml:id">
                <xsl:value-of 
                    select="$app-prefix || count(preceding::tei:app) + 1"/>
            </xsl:attribute>
            <xsl:apply-templates select="@*[name()!='xml:id']"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="tei:rdg">
        <xsl:copy>
            <xsl:attribute name="xml:id">
                <xsl:value-of 
                    select="$rdg-prefix || count(preceding::tei:rdg) + 1"/>
            </xsl:attribute>
            <xsl:apply-templates select="@*[name()!='xml:id']"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="tei:lem">
        <xsl:copy>
            <xsl:attribute name="xml:id">
                <xsl:value-of 
                    select="$lem-prefix || count(preceding::tei:lem) + 1"/>
            </xsl:attribute>
            <xsl:apply-templates select="@*[name()!='xml:id']"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
</xsl:stylesheet>
