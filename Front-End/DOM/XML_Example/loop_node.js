/*
    Loop through element nodes
    Use the nodeType property to only process element nodes in "books.xml".
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readystate == 4 && this.status == 200) {
        myFunc(this);
    }
};

xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunc(xml) {
    var x, i, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.documentElement.childNodes;

    for (i = 0; i < x.length; i++) {
        if (x[i].nodeType == 1) {
            txt += x[i].nodeName + "<br>";
        }
    }
    document.getElementById("demo").innerHTML = txt;
}

