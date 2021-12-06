// Perform a GET Request

const https = require('https')
const options = {
  hostname: 'www.google.com',
  port: 443,
  path: '/',
  method: 'GET',
  headers: {
    'Accept': 'plain/html',
    'Accept-Encoding': '*',
  }
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`);
  console.log('headers:', res.headers);

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(`Error on Get Request --> ${error}`)
})

req.end()


// Perform a POST Request
const https = require('https')

const data = new TextEncoder().encode(
  JSON.stringify({
    todo: 'Buy the milk 🍼'
  })
)

const options = {
  hostname: 'whatever.com',
  port: 443,
  path: '/todos',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})

req.write(data)
req.end()

// POST request using Axios
const axios = require('axios')

axios
.post('https://whatever.com/todos', {
    todo: 'Buy the milk'
})
.then(res => {
    console.log(`statusCode: ${res.status}`)
    console.log(res)
})
.catch(error => {
    console.error(error)
})
