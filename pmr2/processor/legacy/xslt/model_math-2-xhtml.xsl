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
              doctype-public="-//W3C//DTD XHTML 1.1 plus MathML 2.0 plus SVG 1.1//EN"
              doctype-system="http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd"/>
              
  <xsl:template match="cellml:model|cellml11:model">
    <!-- 
    
        We'll preprocess content into presentation instead
        
    <xsl:processing-instruction name="xml-stylesheet">
      <xsl:text>type="text/xsl" </xsl:text>
      <xsl:text>href="http://www.w3.org/Math/XSL/mathml.xsl"</xsl:text>
    </xsl:processing-instruction>
    
    -->
    <html>
 
<!--
     <xsl:call-template name="do-head">
        <xsl:with-param name="name" select="@name"/>
      </xsl:call-template>
-->
      <body>
<!--
        <xsl:variable name="cmeta_id">
          <xsl:call-template name="get_cmeta_id">
            <xsl:with-param name="element" select="."/>
          </xsl:call-template>
        </xsl:variable>
        <h1>
          <xsl:text>cellml.org model repository: </xsl:text>
          <xsl:value-of select="@name"/>
        </h1>
-->
        <!-- The author of the CellML model -->
<!--
        <xsl:if test="rdf:RDF/rdf:Description[@rdf:about='']">
          <xsl:call-template name="output-author">
            <xsl:with-param name="rdf"
              select="rdf:RDF/rdf:Description[@rdf:about='']"/>
          </xsl:call-template>
        </xsl:if>
-->
        <!-- metadata about the model -->
<!--
        <xsl:if test="rdf:RDF/rdf:Description[@rdf:about=$cmeta_id]/cmeta:comment/rdf:value">
          <p class="model-metadata">
            <xsl:value-of select="normalize-space(rdf:RDF/rdf:Description[@rdf:about=$cmeta_id]/cmeta:comment/rdf:value)"/>
          </p>
        </xsl:if>
        <h2>
          <xsl:text>Pretty print of model math</xsl:text>
        </h2>
        <p>
          <xsl:text>
            If your browser is capable of rendering MathML you should see a 
            nice rendering of
            the mathematics from this model below. If you see nothing, try one
            of these excellent browsers and/or plugins:blah blah blah...
          </xsl:text>
        </p>
-->
        <xsl:apply-templates select="cellml:component|cellml11:component"/>
<!--
        <xsl:call-template name="do-footer"/>
-->
      </body>
    </html>
  </xsl:template>
  
  <xsl:template name="do-head">
    <xsl:param name="name"/>
      <head>
        <title>
          <xsl:text>cellml.org model respository: </xsl:text>
          <xsl:value-of select="$name"/>
        </title>
      </head>
  </xsl:template>
  
  <xsl:template name="do-footer">
    <h2>Alternate views of this model</h2>
    <ul>
      <li>
        <xsl:text>
          Model documentation.
        </xsl:text>
      </li>
      <li>
        <xsl:text>
          The raw CellML code.
        </xsl:text>
      </li>
      <li>
        <xsl:text>
          Pretty-print of the CellML code.
        </xsl:text>
      </li>
      <li>
        <xsl:text>
          Load this model into mozCellML.
        </xsl:text>
      </li>
      <li>
        <xsl:text>
          Edit this model.
        </xsl:text>
      </li>
    </ul>
  </xsl:template>

  <xsl:template name="get_cmeta_id">
    <xsl:param name="element"/>
    <xsl:if test="$element/@cmeta:id">
      <!-- need to add a # to signify that the component is in the
           current document -->
      <xsl:value-of select="concat('#',$element/@cmeta:id)"/>
    </xsl:if>
  </xsl:template>

  <xsl:template name="output-author">
    <xsl:param name="rdf"/>
    <xsl:if test="$rdf/dc:creator/vCard:N">
      <p class="model-author">
        <xsl:value-of select="$rdf/dc:creator/vCard:N/vCard:Given/text()"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$rdf/dc:creator/vCard:N/vCard:Family/text()"/>
        <xsl:if test="$rdf/dc:creator/vCard:ORG/vCard:Orgunit">
          <br/>
          <xsl:value-of select="$rdf/dc:creator/vCard:ORG/vCard:Orgunit/text()"/>
        </xsl:if>
        <xsl:if test="$rdf/dc:creator/vCard:ORG/vCard:Orgname">
          <br/>
          <xsl:value-of select="$rdf/dc:creator/vCard:ORG/vCard:Orgname/text()"/>
        </xsl:if>
      </p>
    </xsl:if>
  </xsl:template><!--output-author-->

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
