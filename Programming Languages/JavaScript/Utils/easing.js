/**
 *  Collection of Javascript Easing Function and Implementations
 * 
 * @example easings.net https://easings.net
 * @example Pure JavaScript animation easing https://stackoverflow.com/questions/38497765/pure-javascript-animation-easing
 * @example What is an easing function? https://stackoverflow.com/questions/8316882/what-is-an-easing-function
 */

const easing =  function (x, t, b, c, d) {
    return c * (t /= d) * t + b
}