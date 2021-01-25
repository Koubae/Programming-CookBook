/*
Replace an element node
This example uses replaceChild() to replace the first <book> node.
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
    var x, y, z, i, newNode, newTitle, newText, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.documentElement;
    
    // Create a book element, title element and a text node
    newNode = xmlDoc.createElement("book");
    newTitle = xmlDoc.createElement("title");
    newText = xmlDoc.createTextNode("A Notebook");

    // Add a text node to the title node
    newTitle.appendChild(newText);

    // Add the title node to the book node
    newNode.appendChild(newTitle);

    y = xmlDoc.getElementsByTagName("book")[0];

    // Replace the first book node with the new book node
    x.replaceChild(newNode, y);

    z = xmlDoc.getElementsByTagName("title");
    // Output all titles  
    for (i = 0; i < z.length; i++) { 
        txt += z[i].childNodes[0].nodeValue + "<br>";
    }
    document.getElementById("demo").innerHTML = txt; 
}

/*

Replace data in a text node
This example uses the nodeValue property to replace data in a text node.

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
    txt = x.nodeValue + "<br>";
    x.nodeValue="Easy Italian";
    txt += x.nodeValue;
    document.getElementById("demo").innerHTML = txt
}