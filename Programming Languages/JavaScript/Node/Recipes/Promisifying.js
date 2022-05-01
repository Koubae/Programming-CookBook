copy
const fs = require('fs')

const getFile = (fileName) => {
    return new Promise((resolve, reject) => {
        fs.readFile(fileName, (err, data) => {
            if (err) {
            reject(err)  // calling `reject` will cause the promise to fail with or without the error passed as an argument
            return        // and we don't want to go any further
            }
            resolve(data)
        })
    })
}

getFile('/etc/passwd')
.then(data => console.log(data))
.catch(err => console.error(err))

// Also Available is util.promisify
// https://nodejs.org/docs/latest-v11.x/api/util.html#util_util_promisify_original
const util = require('util');
const fs = require('fs');

const stat = util.promisify(fs.stat);
stat('.').then((stats) => {
  // Do something with `stats`
}).catch((error) => {
  // Handle the error.
});