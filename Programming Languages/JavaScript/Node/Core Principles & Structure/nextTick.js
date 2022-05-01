/*Smple and minimalistic way to how to use nextTick 
for the whole example --> https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#process-nexttick
*/

let bar;

function someAsyncApiCall(callback) {
    process.nextTick(callback);
}

someAsyncApiCall(() => {
    console.log('bar', bar); // 1
});

bar = 1;
// >>> 1

// Example to emit withn the constructor


// warn: this will not work
const EventEmitter = require('events');
const util = require('util');

function MyEmitter() {
    EventEmitter.call(this);
    this.emit('event'); // This will never be emited because will be called at construction
}
util.inherits(MyEmitter, EventEmitter);

const myEmitter = new MyEmitter(); 
    myEmitter.on('event', () => {
    console.log('an event occurred!');
});

// NOTE: Correct way usin process.nextTick;
const EventEmitter = require('events');
const util = require('util');

function MyEmitter() {
    EventEmitter.call(this);

    // use nextTick to emit the event once a handler is assigned;
    // allows a callback to run after the call stack has unwound but before the event loop continues.
    process.nextTick(() => {
    this.emit('event');
    });
}
util.inherits(MyEmitter, EventEmitter);

const myEmitter = new MyEmitter();
    myEmitter.on('event', () => {
    console.log('an event occurred!');
});

