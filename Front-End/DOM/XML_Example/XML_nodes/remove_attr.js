/*
Remove an element node
This example uses removeChild() to remove the first <book> element.
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
    var root = xmlDoc.documentElement;
    var currNode = root.childNodes[1];
    removedNode = currNode.removeChild(currNode.childNodes[1]);
    document.getElementById("demo").innerHTML =
    "Removed node: " + removedNode.nodeName;
}


/* Remove the current element node
This example uses parentNode and removeChild() to remove the current <book> element.
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
    var x, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "Number of book nodes before removeChild(): " +
    xmlDoc.getElementsByTagName("book").length + "<br>";
    x = xmlDoc.getElementsByTagName("book")[0];
    x.parentNode.removeChild(x);
    txt += "Number of book nodes after removeChild(): " +
    xmlDoc.getElementsByTagName("book").length;
    document.getElementById("demo").innerHTML = txt;
}


/*
Remove a text node
This example uses removeChild() to remove the text node from the first <title> element.
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
    var x, y, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.getElementsByTagName("title")[0];
    txt += "Child nodes: " + x.childNodes.length +"<br>";
    y = x.childNodes[0];
    x.removeChild(y);
    txt += "Child nodes: " + x.childNodes.length;
    document.getElementById("demo").innerHTML = txt;
}

/*
Clear the text of a text node
This example uses the nodeValue() property to clear the text node of the first <title> element.

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
    var x, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    txt = "Value: " + x.nodeValue + "<br>";
    x.nodeValue = "";
    txt += "Value: " + x.nodeValue;
    document.getElementById("demo").innerHTML = txt;
}

/*
Remove an attribute by name
This example uses removeAttribute() to remove the "category" attribute from the first <book> element.*/
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
    var x = xmlDoc.getElementsByTagName("book");
    document.getElementById("demo").innerHTML =
    x[0].getAttribute('category') + "<br>";

    x[0].removeAttribute('category');
    document.getElementById("demo").innerHTML +=
    x[0].getAttribute('category');
}

/*Remove attributes by object
This example uses removeAttributeNode() to remove all attributes from all <book> elements.*/

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
    var x, i, attnode, old_att, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.getElementsByTagName('book');
    for (i = 0; i < x.length; i++) { 
        while (x[i].attributes.length > 0) {
            attnode = x[i].attributes[0];
            old_att = x[i].removeAttributeNode(attnode);
            txt += "Removed: " + old_att.nodeName +
            ": " + old_att.nodeValue + "<br>";
        }
    }
    document.getElementById("demo").innerHTML = txt; 
}