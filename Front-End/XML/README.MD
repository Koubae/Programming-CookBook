XML
========


Documentation
-------------

**XML Validator**

An XML document with correct syntax is called *"Well Formed".*

The syntax rules were described in the previous chapters:

- XML documents must have a root element
- XML elements must have a closing tag
- XML tags are case sensitive
- XML elements must be properly nested
- XML attribute values must be quoted

A "well formed" XML document is not the same as a "valid" XML document.

A "valid" XML document must be well formed. In addition, it must conform to a document type definition.

There are two different document type definitions that can be used with XML:

- DTD - The original Document Type Definition
- XML Schema - An XML-based alternative to DTD

The purpose of a DTD is to define the structure and the legal elements and attributes of an XML document.


### Entity References

There are 5 pre-defined entity references in XML:

**Only < and & are strictly illegal in XML, but it is a good habit to replace > with &gt; as well.**
```

&lt; 	< 	less than
&gt; 	> 	greater than
&amp; 	& 	ampersand 
&apos; 	' 	apostrophe
&quot; 	" 	quotation mark

```

------------------------------------------------

### Naming Styles
	
 
|Style|Example|Description|
|---|---|---|
|Lower case | `<firstname>`  |All letters lower case|
|Upper case | `<FIRSTNAME>`  |All letters upper case|
|Underscore | `<first_name>` |Underscore separates words|
|Pascal case| `<FirstName>`  |Uppercase first letter in each word|
|Camel case | `<firstName>`  |Uppercase first letter in each word except the first|

------------------------------------------------

### Namespace | 

**Note**: The namespace URI is not used by the parser to look up information.
The purpose of using an URI is to give the namespace a unique name.
However, companies often use the namespace as a pointer to a web page containing namespace information.

Syntax for xmlns:

`xmlns:prefix="URI"`

Default Namespace:

Defining a default namespace for an element saves us from using prefixes in all the child elements. It has the following syntax:

`xmlns="namespaceURI" `

------------------------------------------------

### Uniform Resource Identifier (URI)

**A Uniform Resource Identifier (URI)** is a string of characters which identifies an Internet Resource.

The most common URI is the **Uniform Resource Locator (URL)** which identifies an Internet domain address. 

Another, not so common type of URI is the **Uniform Resource Name (URN)**.

------------------------------------------------

### XLS Parser

The XML DOM (Document Object Model) defines the properties and methods for accessing and editing XML.
However, before an XML document can be accessed, it must be loaded into an XML DOM object.
All modern browsers have a built-in XML parser that can convert text into an XML DOM object.

------------------------------------------------

### DOM

> The W3C Document Object Model (DOM) is a platform and language-neutral interface that allows programs and scripts to dynamically access and update the content, structure, and style of a document.

The HTML DOM defines a standard way for accessing and manipulating HTML documents. It presents an HTML document as a tree-structure.

The XML DOM defines a standard way for accessing and manipulating XML documents. It presents an XML document as a tree-structure.

------------------------------------------------

### XSLT

**XSLT (eXtensible Stylesheet Language Transformations)** is the recommended style sheet language for XML.

**XSLT** is a language that can be used to transform XML documents into other formats.

XSLT is far more sophisticated than CSS. With XSLT you can add/remove elements and attributes to or from the output file. You can also rearrange and sort elements, perform tests and make decisions about which elements to hide and display, and a lot more.

XSLT uses XPath to find information in an XML document.

------------------------------------------------

### XPath

XPath is a major element in the XSLT standard.
XPath can be used to navigate through elements and attributes in an XML document.

* XPath is a syntax for defining parts of an XML document
* XPath uses path expressions to navigate in XML documents
* XPath contains a library of standard functions
* XPath is a major element in XSLT and in XQuery
* XPath is a W3C recommendation

#### XPath Expressions

XPath expressions can be used in JavaScript, Java, XML Schema, PHP, Python, C and C++, and lots of other languages.

------------------------------------------------

### XQuery

XQuery is to XML what SQL is to databases.
XQuery was designed to query XML data.


- XQuery is the language for querying XML data
- XQuery for XML is like SQL for databases
- XQuery is built on XPath expressions
- XQuery is supported by all major databases
- XQuery is a W3C Recommendation

XQuery - Examples of Use


- Extract information to use in a Web Service
- Generate summary reports
- Transform XML data to XHTML
- Search Web documents for relevant information


```

for $x in doc("books.xml")/bookstore/book
where $x/price>30
order by $x/title
return $x/title

```



* The XLink namespace is declared at the top of the document (xmlns:xlink="http://www.w3.org/1999/xlink")
* The xlink:type="simple" creates a simple "HTML-like" link
* The xlink:href attribute specifies the URL to link to (in this case - an image)
* The xlink:show="new" specifies that the link should open in a new window


------------------------------------------------

### XLink 


- XLink is used to create hyperlinks within XML documents
- Any element in an XML document can behave as a link
- With XLink, the links can be defined outside the linked files
- XLink is a W3C Recommendation

In HTML, the <a> element defines a hyperlink. However, this is not how it works in XML. In XML documents, you can use whatever element names you want - therefore it is impossible for browsers to predict what link elements will be called in XML documents.

#### XLink Attribute Reference

- [XLink Attribute Reference](https://www.w3schools.com/xml/xml_xlink.asp)

------------------------------------------------

### XPointer


- XPointer allows links to point to specific parts of an XML document
- XPointer uses XPath expressions to navigate in the XML document
- XPointer is a W3C Recommendation

There is no browser support for XPointer. But XPointer is used in other XML languages.

Instead of linking to the entire document (as with XLink), XPointer allows you to link to specific parts of the document. To link to a specific part of a page, add a number sign (#) and an XPointer expression after the URL in the xlink:href attribute, like this: xlink:href="https://dog.com/dogbreeds.xml#xpointer(id('Rottweiler'))". The expression refers to the element in the target document, with the id value of "Rottweiler

------------------------------------------------


### XML Schema

An XML Schema describes the structure of an XML document, just like a DTD.
An XML document with correct syntax is called "Well Formed".
An XML document validated against an XML Schema is both "Well Formed" and "Valid".

**XML Schemas are More Powerful than DTD**


- XML Schemas are written in XML
- XML Schemas are extensible to additions
- XML Schemas support data types
- XML Schemas support namespaces

-----------------------------------------------------------------------------------------------------

