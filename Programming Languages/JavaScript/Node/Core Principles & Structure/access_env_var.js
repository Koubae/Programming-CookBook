// An example that accesses the USER_ID and USER_KEY environment variables, which we set in above code.
// https://nodejs.dev/learn/how-to-read-environment-variables-from-nodejs


let userId = process.env.USER_ID // "239482"
let userKey = process.env.USER_KEY // "foobar"

// Using dotenv.js --> https://www.npmjs.com/package/dotenv
require('dotenv').config();

let userId = process.env.USER_ID // "239482"
let userKey = process.env.USER_KEY // "foobar"
let nodeEnv = process.env.NODE_ENV // "development"
// run node -r dotenv/config index.js, have dotenv installed globally but not in the project


// iterate over all the arguments (including the node path and the file path) using a loop
process.argv.forEach((val, index) => {
    console.log(`${index}: ${val}`)
})

//get only the additional arguments by creating a new array

const args = process.argv.slice(2)
console.log(`All Args passed through command line: ${args}`);