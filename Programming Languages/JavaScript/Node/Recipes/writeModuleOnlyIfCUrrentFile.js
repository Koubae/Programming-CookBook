/*
Credits: 
    https://stackoverflow.com/a/6090287/13903942
    https://stackoverflow.com/questions/4981891/node-js-equivalent-of-pythons-if-name-main
    https://stackoverflow.com/questions/6398196/detect-if-called-through-require-or-directly-by-command-line
*/ 

// WARN: In Node.sj

var fnName = function() {
    // main code
}

if (require.main === module) {
    fnName();
}

// WARN: If you use this code in a browser, you will get a "Reference error" since "require" is not defined. To prevent this, use:
if (typeof require !== 'undefined' && require.main === module) {
    fnName();
}