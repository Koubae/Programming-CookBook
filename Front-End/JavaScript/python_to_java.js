// <!DOCTYPE html>
// <html lang="en">
//     <head>
//         <meta charset="UTF-8">
//         <meta name="viewport" content="width=device-width, initial-scale=1.0">
//         <title>Document</title>
//     </head>
//     <body>
//         <h1>Hello World</h1>
        

//         <script>
            // GET is the default method, so we don't need to set it
            fetch('/hello')
                .then(function (response) {
                    return response.text();
                })
                .then(function (text) {
        
                    // Print the greeting as text
                    console.log('GET response text:');
                    console.log(text);
                });
        
            // Send the same request
            fetch('/hello')
                .then(function (response) {
        
                    // But parse it as JSON this time
                    return response.json();
                })
                .then(function (json) {
        
                    // Do anything with it!
                    console.log('GET response as JSON:');
                    console.log(json);
                })
        
            // POST
            fetch('/hello', {
        
                // Declare what type of data we're sending
                headers: {
                    'Content-Type': 'application/json'
                },
        
                // Specify the method
                method: 'POST',
        
                // A JSON payload
                body: JSON.stringify({"greeting": "Hello from the browser!"})
            })
                .then(function (response) {
                    return response.text();
                })
                .then(function (text) {
        
                    console.log('POST response: ');
        
                    // Should be 'OK' if everything was successful
                    console.log(text);
                });
//         </script>      
//     </body>
// </html>


{/* from flask import Flask, jsonify, request, render_template, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        session['response'] = request.get_json()
        
        return 'OK', 200
    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    if 'response' in session:
        print(session['response'])
        for i in range(10):
            print(session['response'])
    else:
        print('not yet')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) */}