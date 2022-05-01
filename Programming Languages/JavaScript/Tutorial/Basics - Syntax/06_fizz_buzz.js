var fizz = "fizz";
var buzz = "buzz";

function fuzzBuzz(num) {
    var fizzBuzz = []; 
    for(let x = 1; x <= num; x++) {
        if (x%3 == 0 && x%5 == 0) {
            console.log(fizz + buzz);
            fizzBuzz.push(fizz + buzz);

        }
        else if (x%3 == 0) {
            console.log(fizz);
            fizzBuzz.push(fizz);
        }
        else if (x%5 == 0) {
            console.log(buzz);
            fizzBuzz.push(buzz);
        }
        else {
            fizzBuzz.push("Nope");
        }
        
    }
    return fizzBuzz;
}

console.log(fuzzBuzz(100));