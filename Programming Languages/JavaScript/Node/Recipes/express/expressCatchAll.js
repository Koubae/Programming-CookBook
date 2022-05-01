// Source --> https://stackoverflow.com/a/13133140/13903942
var express = require('express');
var app = express();

let myHitCounter = {
    'count': 0
};

app.all('*', function(req, res, next){
    myHitCounter.count += 1;
    next();
});

app.get('/', function(req, res) {
  console.log(`Counter: ${myHitCounter.count}`);
  res.send(`'<div><h1>Counter: ${myHitCounter.count}</h1></div>`)
});
app.listen(5000, () => {
  console.log(`Example app listening at http://localhost:${5000}`)
})