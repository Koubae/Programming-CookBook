/* 
    See the node type of an element
    Use the nodeType property to get node type of the root element in "books.xml".
*/

// <p id="demo"></p>

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 & this.status == 200) {
        myFunc(this);
    }
};

xhttp.open("GET", "books.xml", true);
xhttp.send();

function myFunc(xml) {
    var xmlDoc = xmlresponseXML;
    document.getElementById("demo").innerHTML = xmlDoc.documentElement.nodeName + "<br>" +
    xmlDoc.documentElement.nodeType;
}

