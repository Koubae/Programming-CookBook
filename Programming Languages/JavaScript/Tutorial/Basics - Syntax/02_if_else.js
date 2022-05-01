//  If; else if; else;
let boo = true;
let boo1 = false;
if (boo1){
    console.log('is boo1');
}else {
    console.log('Boo');
}

if(5 < 5) {
    console.log('Tre');
}else if(5 == 5) {
    console.log('Equa');
}else {
    console.log('False');
}



function rollDice(num1, num2) {
    let res;
    if(num1 > num2){
        res = 'Number 1 Wins';
    }else if(num1 == num2){
        res = 'Tie Game';
    }else {
        res = 'Number 2 wins';
    }
    return res;
}
console.log(rollDice(5, 7));
console.log(rollDice(56, 7));
console.log(rollDice(56, 56));