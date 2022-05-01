/* =============== < RANDOMIZE ARRAY
*/ 

let myArray = [];
let targetArray = [
    'item_1',
    'item_2',
    'item_3',
    'item_4',
    'item_5',
    'item_6',
    'item_7',
    'item_8',
    'item_9',
    'item_10',
]

function scrambleArray() {
    
    myArray = targetArray.slice();          // Creates a New Copy of the Array

    myArray.sort((_, _1) => {              // Randomize Array
        return 0.5 - Math.random();
    });
}

/* =============== < RANDOMIZE STRING
*/ 

let targetString = 'The quick brown fox jumps over the lazy dog';


function scrambleString(string) {

    let scrumbled = string.split('').sort(() => {
        return 0.5 - Math.random()
    }).join('');
    return scrumbled; 
}

console.log(scrambleString(targetString));
