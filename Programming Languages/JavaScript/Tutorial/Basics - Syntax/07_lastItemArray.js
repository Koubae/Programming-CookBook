var arr = [1,2, 3]
console.log(arr[arr.length-1]);
var last = arr.slice(-1)[0];
console.log(last);

const lotteryNumbers = [12, 16, 4, 33, 41, 22];
const [lastNumber] = lotteryNumbers.slice(-1);

console.log(lotteryNumbers.slice(-1));
// => [22]
console.log(lastNumber);
// => 22