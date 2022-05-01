/*
https://nodejs.org/en/knowledge/errors/what-are-the-error-conventions/
*/

var isTrue = function(value, callback) {
    if (value === true) {
        callback(null, "Value was true.");
    }
    else {
        callback(new Error("Value is not true!"));
    }
}

var callback = function (error, retval) {
    if (error) {
        console.log(error);
    return;
    }
    console.log(retval);
}

// Note: when calling the same asynchronous function twice like this, you are in a race condition.
// You have no way of knowing for certain which callback will be called first when calling the functions in this manner.

isTrue(false, callback);
isTrue(true, callback);

/*

Error: Value is not true!
    at isTrue (C:\app.js:23:15)
    at Object.<anonymous> (C:\app.js:39:12)
    at Module._compile (internal/modules/cjs/loader.js:1085:14)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1114:10)
    at Module.load (internal/modules/cjs/loader.js:950:32)
    at Function.Module._load (internal/modules/cjs/loader.js:790:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:76:12)
    at internal/main/run_main_module.js:17:47
Value was true.

*/
