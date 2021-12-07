const http = require('http');
const { URL } = require('url');
const { parse: parseQuery } = require('querystring');


let log = console.log; // shortcut
const PROTOCOL = 'http';
const PORT = 8000;

function cleanURL(url) {
    /*Remove trailing Slashes to the given URL */
   return url.replace(/^\/+|\/+$/g, '');
}

function buildReqURL(req) {
    const baseURL =  PROTOCOL + '://' + req.headers.host + '/';
    const reqURL = new URL(req.url, baseURL);
    return [cleanURL(reqURL.href), reqURL];
}
function parse(urlObj) {
    return parseQuery(urlObj.search.substr(1))
}

function buildResponse(url, plainURL, headers, method, query) {
    return `Request from ${url} (${plainURL}) (${method})
    Request Headers: ${headers}\n 
    Request Query: ${query}\n
    `
}

function bufferRequest(request) {
    let body = [];
    request.on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
      body = Buffer.concat(body).toString();
      // at this point, `body` has the entire request body stored in it as a string
    });
    return Promise.resolve(body);
}

http.createServer(function (req, res){
    const [reqURL, URLObject] = buildReqURL(req);
    const { headers, method, url } = request;
    // Retrieve Request data
    const requestQuery = parse(URLObject);

    let response = buildResponse(reqURL, url, JSON.stringify(headers), method, JSON.stringify(requestQuery));
    bufferRequest(req).then((buffer) =>{
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(response + "\n" + buffer);
    })


}).listen(PORT, () => { log(`Server Listening at port ${PORT}`) });
