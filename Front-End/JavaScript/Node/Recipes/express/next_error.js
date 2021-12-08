// Credit --> https://stackoverflow.com/a/13145618/13903942
`
In most frameworks you get a request and you want to return a response. 
Because of the async nature of Node.js you run into problems with nested call backs if you are doing non trivial stuff. 
To keep this from happening Connect.js (prior to v4.0, Express.js was a layer on top of connect.js) has something that is called middleware which is a function with 2, 3 or 4 parameters.

function (<err>, req, res, next) {}
Your Express.js app is a stack of these functions.

The router is special, it's middleware that lets you execute one or more middleware for a certain url. So it's a stack inside a stack.

So what does next do? Simple, it tells your app to run the next middleware. 
But what happens when you pass something to next? Express will abort the current stack and will run all the middleware 
that has 4 parameters.
function (err, req, res, next) {}
This middleware is used to process any errors. I like to do the following:
`

next({ type: 'database', error: 'datacenter blew up' });

`
With this error I would probably tell the user something went wrong and log the real error.

If you picture your Express.js application as a stack you probably will be able to fix a lot of weirdness yourself. For example when you add your Cookie middleware after you router it makes sense that your routes wont have cookies.
`

function (err, req, res, next) {
    if (err.type === 'database') {
        res.send('Something went wrong user');
        console.log(err.error);
    }
};