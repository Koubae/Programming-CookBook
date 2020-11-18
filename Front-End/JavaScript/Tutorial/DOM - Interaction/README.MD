# DOM Interacion Document Object Model
=======================

## Features


### The Separarion of Concerns: Structure, Style, Behaviour.

- [Separation of concerns --WIKI--](https://en.wikipedia.org/wiki/Separation_of_concerns)


```

document.querySelector('h1').innerHTML = 'Hii';
console.log(document);
console.log(document.firstElementChild);
console.log(document.firstElementChild.firstElementChild);
console.log(document.firstElementChild.lastElementChild);
console.log(document.firstElementChild.lastElementChild.firstElementChild);
var myH1 = document.firstElementChild.lastElementChild.firstElementChild;
myH1.innerHTML = 'I see You!!';
myH1.style.color = "blue";

document.querySelector("input").click();

```


-----------------------------------------------------------------------------------------------------