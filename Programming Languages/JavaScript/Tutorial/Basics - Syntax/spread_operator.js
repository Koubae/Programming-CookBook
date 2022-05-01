// Roughly equivenl to Python Unpack and the *arg **kwargs notation




// The three dots represent the Spread Operator in ES6. It allows us to do quite a few things in Javascript:

// Concatenate arrays

var shooterGames = ['Call of Duty', 'Far Cry', 'Resident Evil'];
var racingGames = ['Need For Speed', 'Gran Turismo', 'Burnout'];
var games = [...shooterGames, ...racingGames];

console.log(games)  // ['Call of Duty', 'Far Cry', 'Resident Evil',  'Need For Speed', 'Gran Turismo', 'Burnout']

// Destructuring an array

var shooterGames = ['Call of Duty', 'Far Cry', 'Resident Evil'];
var [first, ...remaining] = shooterGames;
console.log(first); //Call of Duty
console.log(remaining); //['Far Cry', 'Resident Evil']


//   Combining two objects

var myCrush = {
    firstname: 'Selena',
    middlename: 'Marie'
};

var lastname = 'my last name';

var myWife = {
    ...myCrush,
    lastname
}

console.log(myWife); // {firstname: 'Selena',
                        //   middlename: 'Marie',
                        //   lastname: 'my last name'}

// There's another use for the three dots which is known as Rest Parameters and it makes it possible to take all of the arguments to a function in as one array.

//     Function arguments as array

function fun1(...params) { 

}  

