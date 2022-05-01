const http = require('http');
const { URL } = require('url');
const { parse: parseQuery } = require('querystring');

// Provide the origin for relative URLs sent to Node.js requests.
const serverOrigin = 'http://localhost:8000';


const server = http.createServer((request, response) => {
  
  const url = new URL(request.url, serverOrigin);
  const query = parseQuery(url.search.substr(1));
  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.end(`Hello, ${query.name}!\n`);
});

// Listen on port 8000, IP defaults to 127.0.0.1.
server.listen(8000, function() {
    console.log(`Server Listening at port ${8000}`);
});
// curl -q http://localhost:8000/status?name=fede
// Hello, fede!