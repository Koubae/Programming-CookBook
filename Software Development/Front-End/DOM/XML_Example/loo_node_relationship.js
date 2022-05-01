/*
    Loop through element nodes using node relationships
    Use the nodeType property and the nextSibling property to process element nodes in "books.xml".
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
    var x, y, i, xlen, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    x = xmlDoc.getElementsByTagName("book")[0];
    xlen = x.childNodes.length;
    y = x.firstChild;
    txt = "";

    for (i = 0; i < xlen; i++) {
        if (y.nodeType == 1) {
            txt += i + " " + y.nodeName + "<br>";
        }
        y = y.nextSibling;
    }
    
    document.getElementById("demo").innerHTML = txt; 
}