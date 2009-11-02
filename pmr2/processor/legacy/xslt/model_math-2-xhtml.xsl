<?xml version='1.0'?>

<xsl:stylesheet 
    xmlns="http://www.w3.org/1999/xhtml"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tmp-doc="http://cellml.org/tmp-documentation"
    xmlns:cellml="http://www.cellml.org/cellml/1.0#"
    xmlns:cellml11="http://www.cellml.org/cellml/1.1#"
    xmlns:mml="http://www.w3.org/1998/Math/MathML"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:cmeta="http://www.cellml.org/metadata/1.0#"
    xmlns:bqs="http://www.cellml.org/bqs/1.0#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
    exclude-result-prefixes="tmp-doc cellml rdf cmeta bqs dc dcterms vCard"
    version='1.0'>

  <xsl:include href="ctop.xsl"/>

  <xsl:output method="xml"
              indent="no"
              omit-xml-declaration="no"
              />
              
  <xsl:template match="cellml:model|cellml11:model">
    <div>
      <xsl:apply-templates select="cellml:component|cellml11:component"/>
    </div>
  </xsl:template>

  <xsl:template name="get_cmeta_id">
    <xsl:param name="element"/>
    <xsl:if test="$element/@cmeta:id">
      <!-- need to add a # to signify that the component is in the
           current document -->
      <xsl:value-of select="concat('#',$element/@cmeta:id)"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="cellml:component|cellml11:component">
    <h3>
      <xsl:text>Component: </xsl:text>
      <xsl:value-of select="@name"/>
    </h3>
    <!-- metadata about the component -->
    <xsl:variable name="cmeta_id">
      <xsl:call-template name="get_cmeta_id">
        <xsl:with-param name="element" select="."/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:if test="rdf:RDF/rdf:Description[@rdf:about=$cmeta_id]/cmeta:comment/rdf:value">
      <p class="model-metadata">
        <xsl:value-of select="normalize-space(rdf:RDF/rdf:Description[@rdf:about=$cmeta_id]/cmeta:comment/rdf:value)"/>
      </p>
    </xsl:if>
    <xsl:for-each select="mml:math">
      <p>
        <xsl:apply-templates mode="c2p" select="."/>
      </p>
    </xsl:for-each>
  </xsl:template><!--cellml:component-->
  
</xsl:stylesheet>
