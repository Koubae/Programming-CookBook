/*
Add a node after the last child node
This example uses appendChild() to add a child node to an existing node.
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
    var x, y, i, newElement, txt, xmlDoc;
    xmlDoc = xml.responseXML;
    newElement = xmlDoc.createElement("edition");
    x = xmlDoc.getElementsByTagName("book")[0]
    x.appendChild(newElement);

   // Display all elements
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
Add a node before a specified child node
This example uses insertBefore() to insert a node before a specified child node.
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
    var newNode = xmlDoc.createElement("book");
    var x = xmlDoc.documentElement;
    var y = xmlDoc.getElementsByTagName("book");
    document.getElementById("demo").innerHTML =
    "Book elements before: " + y.length + "<br>";

    x.insertBefore(newNode, y[3]);
    document.getElementById("demo").innerHTML +=
    "Book elements after: " + y.length;
}

/*
Add a new attribute
This example uses the setAttribute() method to add a new attribute.
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
Add data to a text node
This example uses insertData() to insert data into an existing text node.
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
    var x, txt, xmlDoc;
    xmlDoc = xml.responseXML;
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    txt = x.nodeValue + "<br>";
    x.insertData(0,"Easy ");
    txt += x.nodeValue;
    document.getElementById("demo").innerHTML = txt;
}

/*
Copy a node and append it to an existing node
This example uses cloneNode() to copy a node and append it to the root node of the XML document
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
    var x, y, cloneNode, i, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.getElementsByTagName('book')[0];
    cloneNode = x.cloneNode(true);
    xmlDoc.documentElement.appendChild(cloneNode);

    // Output all titles
    y = xmlDoc.getElementsByTagName("title");
    for (i = 0; i < y.length; i++) { 
        txt += y[i].childNodes[0].nodeValue + "<br>";
    }
    document.getElementById("demo").innerHTML = txt; 
}