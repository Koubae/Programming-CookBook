XSL | XSLT
========


Documentation
-------------

### Specification 

- [Official W3C XSLT namespace](https://www.w3.org/1999/XSL/Transform)

- [Specifications w3 XSL Transformations (XSLT) Version 3.0.](http://www.w3.org/TR/xslt-30)

- [W3C The Extensible Stylesheet Language Family (XSL)](https://www.w3.org/Style/XSL/)

- XSLT is a language for transforming XML documents.

- XPath is a language for navigating in XML documents.

- XQuery is a language for querying XML documents.


- XSLT - a language for transforming XML documents
- XPath - a language for navigating in XML documents
- XSL-FO - a language for formatting XML documents (discontinued in 2013) since 2013, CSS3 is proposed as an XSL-FO replacement.
- XQuery - a language for querying XML documents

XSLT is the most important part of XSL.

XSLT is used to transform an XML document into another XML document, or another type of document that is recognized by a browser, like HTML and XHTML. Normally XSLT does this by transforming each XML element into an (X)HTML element.

With XSLT you can add/remove elements and attributes to or from the output file. You can also rearrange and sort elements, perform tests and make decisions about which elements to hide and display, and a lot more.

A common way to describe the transformation process is to say that XSLT **transforms an XML source-tree into an XML result-tree.**


### Correct Style Sheet Declaration

- [Official W3C XSLT namespace](https://www.w3.org/1999/XSL/Transform)

The root element that declares the document to be an XSL style sheet is <xsl:stylesheet> or <xsl:transform>.

Note: <xsl:stylesheet> and <xsl:transform> are completely synonymous and either can be used!

#### Syntax

```
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> 
```
or


```
<xsl:transform version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> 
```

### XSLT <xsl:template> Element


The <xsl:template> element is used to build templates.

The match attribute is used to associate a template with an XML element. The match attribute can also be used to define a template for the entire XML document. The value of the match attribute is an XPath expression (i.e. match="/" defines the whole document).


### <xsl:value-of> Element

```
<td><xsl:value-of select="catalog/cd/title"/></td>
<td><xsl:value-of select="catalog/cd/artist"/></td>
```

**Note**: The select attribute, in the example above, contains an XPath expression. An XPath expression works like navigating a file system; a forward slash (/) selects subdirectories.

### <xsl:for-each> Element


```
<xsl:for-each select="catalog/cd">
```

We can also filter the output from the XML file by adding a criterion to the select attribute in the <xsl:for-each> element.

```
<xsl:for-each select="catalog/cd[artist='Bob Dylan']">
```

### <xsl:sort> Element


The <xsl:sort> element is used to sort the output.

```
<xsl:sort select="artist"/>
```
### <xsl:if> Element

The <xsl:if> element is used to put a conditional test against the content of the XML file.


### <xsl:choose> | <xsl:when> | <xsl:otherwise>

The <xsl:choose> element is used in conjunction with <xsl:when> and <xsl:otherwise> to express multiple conditional tests.

### <xsl:apply-templates>

The <xsl:apply-templates> element applies a template rule to the current element or to the current element's child nodes.

The <xsl:apply-templates> element applies a template to the current element or to the current element's child nodes.

If we add a "select" attribute to the <xsl:apply-templates> element, it will process only the child elements that matches the value of the attribute. We can use the "select" attribute to specify in which order the child nodes are to be processed.

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------



-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------



-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----