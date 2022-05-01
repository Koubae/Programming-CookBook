// easily calculate how much time a function takes to run, using time() and timeEnd()
// https://nodejs.dev/learn/output-to-the-command-line-using-nodejs#calculate-the-time-spent
const doSomething = () => console.log('test')
const measureDoingSomething = () => {
    console.time('doSomething()')
    //do something, and measure the time it takes
    doSomething()
    console.timeEnd('doSomething()')
}
measureDoingSomething()
