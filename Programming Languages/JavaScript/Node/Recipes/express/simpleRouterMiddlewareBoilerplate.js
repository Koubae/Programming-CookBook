// file about.js

const express = require('express');
const router =  express.Router();

router.get('/', function(req, res, next) {
    res.end('<h1> About </h1>');
});

module.exports = router;

// file app.js
// ...code... 
const aboutRouter = require('./routes/about');

app.use('/', aboutRouter);

// ...code... 