function format(literals, ...substititutions) {
    let result = '';

    for (let i = 0; i < substititutions.length; i++) {
        result += literals[i];
        result += substititutions[i];
    }
    // Add the last literal
    result += literals[literals.length -1];
    return result;
}

let quantity = 9,
    priceEach = 8.99,
    result = format`${quantity} items cost $${(quantity * priceEach).toFixed(2)}.`;

console.log(result); // 9 items cost $80.91.
