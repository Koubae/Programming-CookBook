/*
Firefox, and some other browsers, will treat empty white-spaces or new lines as text nodes, Internet Explorer will not.

This causes a problem when using the properties: firstChild, lastChild, nextSibling, previousSibling.

To avoid navigating to empty text nodes (spaces and new-line characters between element nodes), we use a function that checks the node type:

*/ 



function get_nextSibling(n) {
    var y = n.nextSibling;

    while (y.nodeType != 1) {
        y = y.nextSibling;
    }
    return y;
}

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
    var x = get_firstChild(xmlDoc.getElementsByTagName("book")[0]);
    document.getElementById("demo").innerHTML = x.nodeName;
}

//check if the first node is an element node
function get_firstChild(n) {
    var y = n.firstChild;

    while (y.nodeType != 1) {
        y = y.nextSibling;
    }
    
    return y;
}