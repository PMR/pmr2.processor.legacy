<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <bread><xsl:value-of select="/egg/bacon/text()" /></bread>
    </xsl:template>
</xsl:stylesheet>
