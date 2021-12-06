// How to exit from a Node.js program -- https://nodejs.dev/learn/how-to-exit-from-a-nodejs-programç
const express = require('express')

const app = express()

app.get('/', (req, res) => {
    res.send('Hi!')
})

const server = app.listen(3000, () => console.log('Server ready'))

process.on('SIGTERM', () => {
    server.close(() => {
        console.log('Process terminated')
    })
})
