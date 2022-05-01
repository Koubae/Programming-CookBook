var myCodeMirror = CodeMirror(document.getElementById('code'), {
    value: "print u\"Hello\"",
    mode:  "python"
});
setTimeout(function() {
    myCodeMirror.doc.setValue('function hi()\n{\n    echo "hello";\n}\n');
    myCodeMirror.setOption('mode', 'text/x-php');

    setTimeout(function(){
        myCodeMirror.doc.setValue('function myScript(){return 100;}\n');
        myCodeMirror.setOption('mode', 'javascript');
    }, 3000);

}, 3000);