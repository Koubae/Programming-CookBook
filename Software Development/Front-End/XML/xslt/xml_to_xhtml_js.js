/*transform the XML file to XHTML on the client*/ 
/*
<body onload="displayResult()">
<div id="example" /></div>
</body>
*/

function loadXMLDoc(filename) {
    if (window.ActiceXObject) {
        xhtpp = new ActiveXObject("Msxml2.XMLHTTP");
    } else {
        xhttp = new XMLHttpRequest();
    }
    xhttp.open("GET", filename, false);
    try {
        xhttp.responseType = "msxml-document";
    } catch (err) {} // Helping IE11
    xhttp.send("");
    return xhttp.responseXML;
}