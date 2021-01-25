/*
    Get the text from a text node
    This example uses the nodeValue property to get the text of the first <title> element in "books.xml".
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
    var x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    document.getElementById("demo").innerHTML = x.nodeValue;
}


/*Change the text in a text node
This example uses the nodeValue property to change the text of the first <title> element in "books.xml".*/

//

//<p id="demo1"></p>
{/* <p id="demo2"></p> */}
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
    var x;
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];

    document.getElementById("demo1").innerHTML = x.nodeValue;

    x.nodeValue = "Easy Cooking";
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    document.getElementById("demo2").innerHTML = x.nodeValue;
}


/*
Get the node name and type of an element node
This example uses the nodeName and nodeType property to get node name and type of the root element in "books.xml".
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
    document.getElementById("demo").innerHTML =
    xmlDoc.documentElement.nodeName + "<br>" +
    xmlDoc.documentElement.nodeType;
}