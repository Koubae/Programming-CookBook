// =======================================================
//---------------> LOOPS <-------------------------------\\
// =======================================================  

const dice = ['2', '3', '4', '5', '6'];
let count = 10;
let x = 0;

// While Loop;

while (x <= count){
    console.log('Counter is ' + x);
    x++;
    if(x == 5) {
        console.log(5);
    } else {
        console.warn(null);
    }
}

// for loop;

const dice2 = ['Test2', 3, '4', 5, 'six'];

for(let x=0;x<count;x++){
    console.log('Counter is ' + x);
}

for(let x=0;x<dice2.length;x++){
    console.log('Counter is ' + dice[x]);
}

console.log('===================================');
// forEach;

dice2.forEach(function (el, index, arr){
    console.log('el >>>', el);
    console.log('index >>>', index);
    console.log('dice[index] >>> ', dice[index]);
    console.log('arr', arr);
})

dice2.forEach(function (el, index, arr) {
    console.log(el, index, arr[index]);
    console.log(arr);
})

console.log('===================================');

function randomNum(val) {
    return Math.floor(Math.random() * val) + 1;
}

function rollDice(num1, num2) {
    let res;
    if (num1 > num2) {
        res = 'Number 1 Wins';
    }
    else if (num1 == num2) {
        res = 'Tie Game';
    }
    else {
        res = 'Number 2 Wins';
    }
    return res;
}

let game1 = [randomNum(6), randomNum(6)];
let game2 = [randomNum(6), randomNum(6)];
let game3 = [randomNum(6), randomNum(6)];
console.log(rollDice(game1[0], game1[1]));
console.log(rollDice(game2[0], game2[1]));
console.log(rollDice(game3[0], game3[1]));