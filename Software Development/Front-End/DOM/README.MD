DOM | Document Object Model 
========


Documentation
-------------

**The HTML DOM** defines a standard way for accessing and manipulating HTML documents. It presents an HTML document as a tree-structure.

**The XML DOM** defines a standard way for accessing and manipulating XML documents. It presents an XML document as a tree-structure.


**The XML DOM is a standard for how to get, change, add, or delete XML elements.**

---------------------------------------------

### XML DOM Nodes

According to the XML DOM, everything in an XML document is a node:

* The entire document is a document node
* Every XML element is an element node
* The text in the XML elements are text nodes
* Every attribute is an attribute node
* Comments are comment nodes

**Text is Always Stored in Text Nodes**

The XML DOM views an XML document as a tree-structure. The tree structure is called a **node-tree.**


* In a node tree, the top node is called the root
* Every node, except the root, has exactly one parent node
* A node can have any number of children
* A leaf is a node with no children
* Siblings are nodes with the same parent


-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------



-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------


* x.nodeName - the name of x
* x.nodeValue - the value of x
* x.parentNode - the parent node of x
* x.childNodes - the child nodes of x
* x.attributes - the attributes nodes of x


* x.getElementsByTagName(name) - get all elements with a specified tag name
* x.appendChild(node) - insert a child node to x
* x.removeChild(node) - remove a child node from x


-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----