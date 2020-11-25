// Default Value

let person = {
    firstName: 'John',
    lastName: 'Doe',
    currentAge: 28
};

let {
    firstName,
    lastName,
    middleName = '',
    age: currentAge = 18
} = person;

console.log(middleName); // ''
console.log(age); // 28


let person = {
    firstName: 'John',
    lastName: 'Doe',
    middleName: 'C.',
    currentAge: 28
};

let {
    firstName,
    lastName,
    middleName = '',
    currentAge: age = 18
} = person;

console.log(middleName); // 'C.'
console.log(age); // 28


//  use the OR operator (||) to fallback the null object to an empty object

function getPerson() {
    return null;
}

let {
    firstName,
    lastName
} = getPerson() || {};

// Function without the ||
// let {
//     firstName,
//     lastName
// } = getPerson();

// console.log(firstName, lastName);
// TypeError: Cannot destructure property 'firstName' of 'getPerson(...)' as it is null.


//  multiple assignement of a property to multiple variables:

let employee = {
    id: 1001,
    name: {
        firstName: 'John',
        lastName: 'Doe'
    }
};

let {
    name: {
        firstName,
        lastName
    },
    name
} = employee;

console.log(firstName); // John
console.log(lastName); // Doe
console.log(name); // { firstName: 'John', lastName: 'Doe' }


// Destructuring function arguments 
//  This technique is often used in React.

let display = (person) => console.log(`${person.firstName} ${person.lastName}`);

let person = {
    firstName: 'John',
    lastName: 'Doe'
};

display(person);

// ||

let display = ({firstName, lastName}) => console.log(`${firstName} ${lastName}`);

let person = {
    firstName: 'John',
    lastName: 'Doe'
};

display(person);




// ==============================================***
// Destructuring Assignment

function getScores() {
    return [70, 80, 90];
}

let [x, y, z] = getScores();

console.log(x); // 70
console.log(y); // 80
console.log(z); // 90

// Deconstructing more element than the Function returning arguments
function getScores() {
    return [70, 80];
}
 
let [x, y, z] = getScores();
 
 console.log(x); // 70
 console.log(y); // 80
 console.log(z); // undefined***


// Deconstructor has LESS element than the function's arguments
function getScores() {
    return [70, 80, 90, 100];
 }
 
let [x, y, z] = getScores();
 
 console.log(x); // 70
 console.log(y); // 80
 console.log(z); // 90
//  Other Argument idx get ignored;


//  Rest Syntax
let [x, y ,...args] = getScores();
console.log(x); // 70
console.log(y); // 80
console.log(args); // [90, 100]

let a, b;
[a, b] = [10, 20];
console.log(a); // 10
console.log(b); // 20

// DEFAULT VALUES

// Using the Ternary operator.
function getItems() {
    return [10, 20];
}

let items = getItems();
let thirdItem = items[2] != undefined ? items[2] : 0;

console.log(thirdItem); // 0

// Using Default Value.
let [, , thirdItem = 0] = getItems();

console.log(thirdItem); // 0

let a, b;
[a = 1, b = 2] = [10];
console.log(a); // 10
console.log(b); // 2


// If func doesnt return Array.

function getItems() {
    return null;
}

let [a = 10, b = 20] = getItems() || [];

console.log(a); // 10
console.log(b); // 20

// function getItems() {
//     return null;
// }

// let [x = 1, y = 2] = getItems();
// Uncaught TypeError: getItems is not a function or its return value is not iterable

// =============================================================== \\