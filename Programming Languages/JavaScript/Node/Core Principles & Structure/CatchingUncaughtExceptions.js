/* Catching uncaught exceptions
https://nodejs.dev/learn/error-handling-in-nodejs#catching-uncaught-exceptions


If an uncaught exception gets thrown during the execution of your program, your program will crash.
To solve this, you listen for the uncaughtException event on the process object:

*/

process.on('uncaughtException', err => {
    console.error('There was an uncaught error', err)
    process.exit(1) //mandatory (as per the Node.js docs)
})
