// GET

let request_obj = {

    method: 'GET',
    mode: 'no-cors',
    cache: 'no-cache',
    creadentials: 'include',
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
   
};

var fetch_test_get = fetch('http://example.com', request_obj);

console.log("fetch_test_get", fetch_test_get)
fetch_test_get.then(response => response)
.then(data => console.log("data", data));

console.log("======================================");

// POST
let request_obj_post = {

    method: 'POST',
    mode: 'no-cors',
    cache: 'no-cache',
    creadentials: 'include',
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'origin-list'
    },
    body: JSON.stringify( {answer: 42} )
};

var fetch_test_post = fetch('http://example.com', request_obj_post);

console.log("fetch_test_post", fetch_test_post)
fetch_test_post.then(resp => resp)
.then(data => console.log("data", data))