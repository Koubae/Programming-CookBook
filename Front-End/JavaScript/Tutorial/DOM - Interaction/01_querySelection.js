// DOM interaction;

const output = document.querySelector('.output');
console.dir(output);
output.style.backgroundColor = 'red';
output.textContent = 'Hello World';


const divs = document.querySelectorAll('div');

// innerHTML

document.querySelector('h1').innerHTML = 'Hii';


// DOMTokenList 

document.querySelector('button').classList;
console.log(document.querySelector('button').classList);
// DOMTokenList []

//  Add
document.querySelector('button').classList.add("new_class");
console.log(document.querySelector('button').classList);
// DOMTokenList [ "new_class" ] 

// Remove
document.querySelector('button').classList.remove("new_class");

//  toggle
document.querySelector('button').classList.toggle("new_class");

// textContent
document.querySelector("h1").textContent;

// getAttribute
document.querySelector("h1").getAttribute("href");

//  setAttribute
document.querySelector("h1").setAttribute("href", "test");