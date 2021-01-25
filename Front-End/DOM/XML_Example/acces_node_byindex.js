/*
    Access a node using its index number in a node list
    Use the getElementsByTagName() method to get the third <title> element in "books.xml"
*/ 


// <p id="demo"></p>

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myFunc(this);
    }
};


xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunc(xml) {
    var xmlDoc = xml.responseXML;
    var x = xmlDoc.getElementsByTagName("title");
    document.getElementById("demo").innterHTML = x[2].childNodes[0].nodeValue;
};

