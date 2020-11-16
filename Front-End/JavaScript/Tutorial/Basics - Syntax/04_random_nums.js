//  Rundom Numbers;

let rand_num1 = Math.floor(Math.random()*10)+1;
let rand_num2 = Math.floor(Math.random()*6)+1;

function randomNum(val) {
    return Math.floor(Math.random()*val) + 1;
}

var a = randomNum(5);
var b = randomNum(6);

var message = rollDice(a, b);
console.log(a + ' vs ' + b + ' ' + message);