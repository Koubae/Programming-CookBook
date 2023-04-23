import time
from flask import Flask
app = Flask(__name__)

@app.route('/liveness')
def healthx():
  return "OK", 200
  
@app.route('/readiness')
def healthz():
  return "OK", 200
  
@app.route("/")
def hello():
  return "<h1><center>Hello World app! Version 1</center><h1>"

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=5000, debug=True)