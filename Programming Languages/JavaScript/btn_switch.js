// Simple Swithc
function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.innerHTML === "Hello") {
      x.innerHTML = "Swapped text!";
    } else {
        x.innerHTML = "Hello";
    }
  }

function toggleTheme(button) {
    var _switch = document.getElementById("themeToggle");
    
    if (_switch.value == 'off'){ 
        _switch.value = 'on';      
        inPutEditor.setOption('theme', darculaTheme);
        outPutEditor.setOption('theme', darculaTheme);
        console.log(outPutEditor.options.theme);
        console.log(_switch.checked)

    } else {
        _switch.value = 'off';
        inPutEditor.setOption('theme', ideaTheme);
        outPutEditor.setOption('theme', ideaTheme);
        console.log(_switch.checked)
    }
    return userTheme;


// Checkbox

// Theme Mode Switch
function toggleTheme(button) {
    var _switch = document.getElementById("themeToggle");
    
    if (_switch.checked){ 
        _switch.value = 'on';      
        inPutEditor.setOption('theme', darculaTheme);
        outPutEditor.setOption('theme', darculaTheme);
        console.log(outPutEditor.options.theme);

    } else {
        _switch.value = 'off';
        inPutEditor.setOption('theme', ideaTheme);
        outPutEditor.setOption('theme', ideaTheme);

    }
    return userTheme;
}
// Call the function at least once, avoid a small bug defined below [1];
toggleTheme(); 


// Turn on only once.

function toggle(button)
{
  if(document.getElementById("1").value=="OFF"){
   document.getElementById("1").value="ON";}
   else if(document.getElementById("1").value=="ON"){
   document.getElementById("1").value="OFF";}
}}

function toggle(button) {
    if (button.value == "OFF") {
      button.value = "ON";
    } else {
      button.value = "OFF";
    }
  }


// Ternary Operator
function toggle(b){b.value=(b.value=="ON")?"OFF":"ON";}


// switch


function toggle(button) 
{
     switch(button.value)
     {
          case "ON":
               button.value = "OFF";
               break;
          case "OFF":
               button.value = "ON";
               break;
     }
}



var button = document.querySelector("button");
var body = document.querySelector("body");
var isOrange = true;

button.addEventListener("click", function() {
if(isOrange) {
    body.style.background = "orange";
}else {
    body.style.background = "none";
}
isOrange = !isOrange;
});

// .orange {
//     background: orange;
//     }

var button = document.querySelector("button");
button.addEventListener("click", function() {
    document.body.classList.toggle("orange");
});

// // <form>
//         <input type="checkbox" id="accept" checked> Accept
//         <input type="button" id="btn" value="Submit">
//     </form>
const cb = document.querySelector('#accept');
const btn = document.querySelector('#btn');
btn.onclick = () => {
    const result = cb.value;
    alert(result); // on
};


function getSelectedCheckboxValues(name) {
    const checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
    let values = [];
    checkboxes.forEach((checkbox) => {
        values.push(checkbox.value);
    });
    return values;
}

const btn = document.querySelector('#btn');
btn.addEventListener('click', (event) => {
    alert(getSelectedCheckboxValues('color'));
});

function check(checked = true) {
    const cbs = document.querySelectorAll('input[name="color"]');
    cbs.forEach((cb) => {
        cb.checked = checked;
    });
}

const btn = document.querySelector('#btn');
btn.onclick = checkAll;

function checkAll() {
    check();
    // reassign click event handler
    this.onclick = uncheckAll;
}

function uncheckAll() {
    check(false);
    // reassign click event handler
    this.onclick = checkAll;
}