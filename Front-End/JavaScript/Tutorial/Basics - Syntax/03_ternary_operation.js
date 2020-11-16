//  Conditional Ternary operation;

var message = (5 == 5) ? 'TRUE' : 'FALSE';
console.log(message);

function getFee(isMember) {
    return (isMember ? '$2.00' : '$10.00');
    
}

console.log(getFee(true));
console.log(getFee(false));
console.log(getFee(null));

var age = 26;
var beverage = (age >= 21) ? 'Beer' : 'Juice';
console.log(beverage); // Beer;


// Template literal

let greeting = person => {
    let name = person ? person.name : 'stranger'
    return `Howdy, ${name}`
}

console.log(greeting({name: `Alice`})); // "Howdy, Alice"
console.log(greeting(null)); // "Howdy, stranger"


// function example(...) {
//     return condition1 ? value1
//         : condition2 ? value2
//         : condition3 ? value3
//         : value4;
// }

// // Equivalent to:
// function example(...) {
//     if (condition1) {return value1; }
//     else if (condition2) {return value2; }
//     else if (condition3) {return value3; }
//     else {return value4; }
// }

