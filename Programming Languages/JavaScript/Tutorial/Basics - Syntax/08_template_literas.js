
// If a string contains a backtick, you must escape it using a backslash ( \) :
let strWithBacktick = `Template literals use backticks \` insead of quotes`;


// Multiline
let p =
`This text
can
span multiple lines`;


let a = 5;
let b = 10;
console.log(`Fifteen is ${a + b} and
not ${2 * a + b}.`);
// "Fifteen is 15 and
// not 20."


// Interpolation to HTML use the object destructuring technique

let post = {
    title: 'JavaScript Template Literals',
    excerpt: 'Introduction to JavaScript template literals in ES6',
    body: 'Content of the post will be here...',
    tags: ['es6', 'template literals', 'javascript']
};


let {title, excerpt, body, tags} = post;

var postHtml = `<article>
<header>
    <h1>${title}</h1>
</header>
<section>
    <div>${excerpt}</div>
    <div>${body}</div>
</section>
<footer>
    <ul>
      ${tags.map(tag => `<li>${tag}</li>`).join('\n      ')}
    </ul>
</footer>`;

// ------------------------------------------------

let firstName = 'John',
    lastName = 'Doe';

let greeting = `Hi ${firstName}, ${lastName}`;
console.log(greeting); // Hi John, Doe



let price = 8.99,
    tax = 0.1;

var netPrice = `Net Price:$${(price * (1 + tax)).toFixed(2)}`;

console.log(netPrice); // netPrice:$9.89



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


// ------------------------------------------------
//  NESTING TEMPLATES
// ------------------------------------------------

//  ES5

let classes = 'header';
classes += (isLargeScreen() ?
    '' : item.isCollapsed ?
    ' icon-expander' : ' icon-collapser');

//  ES2015 with template literals and without nesting
const classes = `header ${ isLargeScreen() ? '' :
    (item.isCollapsed ? 'icon-expander' : 'icon-collapser') }`;

//  ES2015 with nested template literals:
const classes = `header ${ isLargeScreen() ? '' :
    `icon-${item.isCollapsed ? 'expander' : 'collapser'}` }`;