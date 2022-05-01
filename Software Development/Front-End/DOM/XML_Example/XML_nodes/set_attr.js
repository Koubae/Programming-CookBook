/*
    Change an element's text node
    This example uses the nodeValue property to change the text node of the first <title> element in "books.xml".
*/ 

//<p id="demo"></p>

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
    var txt = "";
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    txt += x.nodeValue + "<br>";    
    x.nodeValue = "Easy Cooking";
    x = xmlDoc.getElementsByTagName("title")[0].childNodes[0];
    txt += x.nodeValue + "<br>";    
    document.getElementById("demo").innerHTML = txt;
}

/*
Change an attribute's value using setAttribute
This example uses the setAttribute() method to change the value of the "category" attribute of the first <book>.
*/ 

//<p id="demo"></p>
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
    var x = xmlDoc.getElementsByTagName('book');
    x[0].setAttribute("category","food");
    document.getElementById("demo").innerHTML =
    x[0].getAttribute("category");
}

/* 
Change an attribute's value using nodeValue
This example use the nodeValue property to change the value of the "category" attribute of the first <book>.
*/
//<p id="demo"></p>
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
    var x = xmlDoc.getElementsByTagName("book")[0]
    var y = x.getAttributeNode("category");
    var txt = y.nodeValue + "<br>";
    y.nodeValue ="food";
    txt += y.nodeValue;
    document.getElementById("demo").innerHTML = txt;
}