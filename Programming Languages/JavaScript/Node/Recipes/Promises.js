

// Chaining Promises
const status = response => {
  if (response.status >= 200 && response.status < 300) {
    return Promise.resolve(response)
  }
  return Promise.reject(new Error(response.statusText))
}

const json = response => response.json()

fetch('/todos.json')
  .then(status)    // note that the `status` function is actually **called** here, and that it **returns a promise***
  .then(json)      // likewise, the only difference here is that the `json` function here returns a promise that resolves with `data`
  .then(data => {  // ... which is why `data` shows up here as the first parameter to the anonymous function
    console.log('Request succeeded with JSON response', data)
  })
  .catch(error => {
    console.log('Request failed', error)
  })

// Handling Errors
new Promise((resolve, reject) => {
  throw new Error('Error')
}).catch(err => {
  console.error(err)
})

// or

new Promise((resolve, reject) => {
  reject('Error')
}).catch(err => {
  console.error(err)
})


// Cascading Errors
new Promise((resolve, reject) => {
  throw new Error('Error')
})
  .catch(err => {
    throw new Error('Error')
  })
  .catch(err => {
    console.error(err)
  })

// Promise.all()
const f1 = fetch('/something.json')
const f2 = fetch('/something2.json')

Promise.all([f1, f2])
  .then(res => {
    console.log('Array of results', res)
  })
  .catch(err => {
    console.error(err)
})

// Using  ES2015 destructuring assignment syntax
Promise.all([f1, f2]).then(([res1, res2]) => {
  console.log('Results', res1, res2)
})

// Promise.race()
// Promise.race() runs when the first of the promises you pass to it settles (resolves or rejects), and it runs the attached callback just once, with the result of the first promise settled.

const first = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, 'first')
})
const second = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'second')
})

Promise.race([first, second]).then(result => {
  console.log(result) // second
})


// Promise.any()
// Promise.any() settles when any of the promises you pass to it fulfill or all of the promises get rejected. It returns a single promise that resolves with the value from the first promise that is fulfilled. 
// If all promises are rejected, then the returned promise is rejected with an AggregateError.
const first = new Promise((resolve, reject) => {
  setTimeout(reject, 500, 'first')
})
const second = new Promise((resolve, reject) => {
  setTimeout(reject, 100, 'second')
})

Promise.any([first, second]).catch(error => {
  console.log(error) // AggregateError
})
