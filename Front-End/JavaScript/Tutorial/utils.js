//  length;
var item1 = 'Something+';
console.log(item1.length);
// 10;

//  includes;
var arr = [1, 2, 3, 4, 5];
console.log(arr.includes(1)); // true;
console.log(arr.includes(10)); // false;

// Array push; pop;

var arr = [];
arr.push(1);
console.log(arr); // [1];
var x = arr.pop(); 
console.log(arr); // [];
console.log(x); // 1;


// console dir
console.dir(document);

// Document 
document.body.textContent = 'Hello';

// Head Area
headArea.textContent = "Something";

// typeof

const x = 5;
var y = 10;
let z = 15;
typeof(x);
typeof(y);
typeof(z);