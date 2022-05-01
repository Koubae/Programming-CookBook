/*
    Loop through nodes using the length property
    Use the length property to loop through all <title> elements in "books.xml"
*/ 

// <p id="demo"></p>

var xhttp;
xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunc(this);
    }
};

xhttp.open("GET", "books.xml", true);
xhttp.send();


function myFunc(xml) {
    var x, i, txt, xmlDoc;
    xmlDoc = xml.responseXML;
    txt = '';
    x = xmlDoc.getElementByTagName("title");

    for (i = 0; i < x.length; i++) {
        txt += x[i].childNodes[0].nodeValue + "<br>";
    }
    document.getElementById("demo").innerHTML = txt;
}

