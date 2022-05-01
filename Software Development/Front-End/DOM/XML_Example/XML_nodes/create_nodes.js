/*
Create an element node
This example uses createElement() to create a new element node, and appendChild() to add it to a node.
*/
// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var xmlDoc = xml.responseXML;
    var x, y, i, newEle, newText, txt;

    // add an edition element
    newEle = xmlDoc.createElement("edition");
    newText = xmlDoc.createTextNode("first");
    newEle.appendChild(newText);
    x = xmlDoc.getElementsByTagName("book")[0];
    x.appendChild(newEle);

    // display all elements
    xlen = x.childNodes.length;
    y = x.firstChild;
    txt = "";
    for (i = 0; i < xlen; i++) {
        if (y.nodeType == 1) {
            txt += y.nodeName + "<br>";
        }
    y = y.nextSibling;
    }
    document.getElementById("demo").innerHTML = txt;
}


/*
Create an attribute node using createAttribute
This example uses createAttribute() to create a new attribute node, and setAttributeNode() to insert it to an element.
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var x, newatt, xmlDoc;
    xmlDoc = xml.responseXML;
    newatt = xmlDoc.createAttribute("edition");
    newatt.nodeValue = "first";
    x = xmlDoc.getElementsByTagName("title");
    x[0].setAttributeNode(newatt);
    document.getElementById("demo").innerHTML =
    "Edition: " + x[0].getAttribute("edition");
}


/*
Create an attribute node using setAttribute
This example uses setAttribute() to create a new attribute for an element.
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var xmlDoc = xml.responseXML;
    var x = xmlDoc.getElementsByTagName("title");
    x[0].setAttribute("edition", "first");
    document.getElementById("demo").innerHTML =
    "Edition: " + x[0].getAttribute("edition");
}


/*
Create a text node
This example uses createTextNode() to create a new text node, and appendChild() to add it to an element.
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var xmlDoc = xml.responseXML;
    var x, y, i, newEle, newText, txt;

    // add an edition element
    newEle = xmlDoc.createElement("edition");
    newText = xmlDoc.createTextNode("first");
    newEle.appendChild(newText);
    x = xmlDoc.getElementsByTagName("book")[0];
    x.appendChild(newEle);

    // display all elements
    xlen = x.childNodes.length;
    y = x.firstChild;
    txt = "";
    for (i = 0; i < xlen; i++) {
        if (y.nodeType == 1) {
            txt += y.nodeName + "<br>";
        }
    y = y.nextSibling;
    }
    document.getElementById("demo").innerHTML = txt;
}


/*
Create a CDATA section node
This example uses createCDATAsection() to create a CDATA section node, and appendChild() to add it to an element.
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var x, newCDATA, xmlDoc;
    xmlDoc = xml.responseXML;
    newCDATA = xmlDoc.createCDATASection("Special Offer & Book Sale");
    x = xmlDoc.getElementsByTagName("book")[0];
    x.appendChild(newCDATA);
    document.getElementById("demo").innerHTML = x.lastChild.nodeValue;
}


/*
Create a comment node
This example uses createComment() to create a comment node, and appendChild() to add it to an element.
*/


// <p id="demo"></p>


var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunction(xml) {
    var x, newComment, xmlDoc;
    xmlDoc = xml.responseXML;
    newComment = xmlDoc.createComment("Revised April 2015");
    x = xmlDoc.getElementsByTagName("book")[0];
    x.appendChild(newComment);
    document.getElementById("demo").innerHTML = x.lastChild.nodeValue;
}