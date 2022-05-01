
var arr = [1,2, 3]
var lastItem = arr[arr.length-1];
var secondLastItem = arr[arr.length-2];


function fibSeq (num) {
    let fibResult = [0];
    
    if (num >= 1) {
        fibResult.push(1);
    }
    if (num > 1) {        
        for(let x = 0; x < num+1; x++) {
            fibResult.push(fibResult[fibResult.length-2] + fibResult[fibResult.length-1]);
        }

    }
    else {
        return fibResult;
    }
    return fibResult;
}

console.log(fibSeq(8));