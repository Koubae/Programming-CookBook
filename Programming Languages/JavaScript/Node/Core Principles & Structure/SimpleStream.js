// Reading without Stream
const http = require('http')
const fs = require('fs')

const server = http.createServer(function(req, res) {
  fs.readFile(__dirname + '/data.txt', (err, data) => {
    res.end(data)
  })
})
server.listen(3000)

// Reading with Stream 
const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
  const stream = fs.createReadStream(__dirname + '/data.txt')
  stream.pipe(res)
})
server.listen(3000)

// How to create a readable stream https://nodejs.dev/learn/nodejs-streams#how-to-create-a-readable-stream
// How to create a writable stream  https://nodejs.dev/learn/nodejs-streams#how-to-create-a-writable-stream

 
// How to get data from a readable stream   https://nodejs.dev/learn/nodejs-streams#how-to-get-data-from-a-readable-stream
const Stream = require('stream')

const readableStream = new Stream.Readable({
  read() {}
})
const writableStream = new Stream.Writable()

writableStream._write = (chunk, encoding, next) => {
  console.log(chunk.toString())
  next()
}

readableStream.pipe(writableStream)

readableStream.push('hi!')
readableStream.push('ho!')

// You can also consume a readable stream directly, using the readable event:
readableStream.on('readable', () => {
  console.log(readableStream.read())
})
