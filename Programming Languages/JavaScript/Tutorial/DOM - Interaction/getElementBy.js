//  getElementByTagName
document.getElementsByTagName('btn');
var x = document.getElementsByTagName('li');
console.log(x);  // HTMLCollection { 0: li, 1: li, 2: li, length: 3 }

// getElementByClassName

document.getElementsByClassName('MyLabel')[0].style.color = "red";
console.log(document.getElementsByClassName('MyLabel'));
// HTMLCollection { 0: label.MyLabel, length: 1 }

//  getElementById
document.getElementById('list').style.color = 'green';