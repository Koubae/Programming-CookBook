const btn = document.querySelector('button');
btn.addEventListener('click', function (e) {
    console.log('Hello');
    console.log(e);
})

// dict[1].textContent = 'test';


var numberOFDrumButtons = document.querySelectorAll(".drum").length;

for (var i = 0; i<numberOFDrumButtons; i++) {
    console.log(i);
    document.querySelectorAll(".drum")[i].addEventListener("click", function () {
        console.log(this.innerHTML);
        console.log(this);
        this.style.color = "red";
    })
}