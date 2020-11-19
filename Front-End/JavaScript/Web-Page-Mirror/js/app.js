function showPreview(){
    var htmlCode = document.getElementById("htmlCode").value;
    var cssCode = "";
    var jsCode = ""+document.getElementById("jsCode").value+"";
    var frame = document.getElementById("preview-window").contentWindow.document;
    frame.open();
    frame.write(htmlCode+cssCode+jsCode);
    frame.close();
  }