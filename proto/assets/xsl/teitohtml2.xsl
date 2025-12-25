<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs tei"
    version="1.0">

    <xsl:output encoding="UTF-8" method="html" indent="yes"/>

    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="tei:TEI">
        <div id="content">
            <xsl:apply-templates/>
        </div>
    </xsl:template>

    <xsl:template match="tei:teiHeader"/>

    <xsl:template match="tei:ab">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <xsl:template match="tei:choice">
        <span class="choice" id="{ ./@xml:id }"><xsl:apply-templates select="tei:sic"/></span>
    </xsl:template>
    
    <xsl:template match="tei:sic">
        <span class="sic" id="{ ./@xml:id }"><span style="cursor: pointer;" onclick="review('{ parent::tei:choice/@xml:id }', '{ ./@xml:id }')"><xsl:apply-templates/></span></span>
    </xsl:template>
    
    <xsl:template match="tei:corr">
        <span class="corr" id="{ ./@xml:id }"><span style="cursor: pointer;" onclick="review('{ parent::tei:choice/@xml:id }', '{ ./@xml:id }')"><xsl:apply-templates/></span></span>
    </xsl:template>

    <xsl:template match="tei:lb">
        <br/>
    </xsl:template>
    
</xsl:stylesheet>
