// Function declaration;
// Can call function before assignement.
test(); 

function test(){
    console.log('Func test');
}
test();

const test2 = function(num){
    console.log('function expression ' + num);
}

test2(100);
