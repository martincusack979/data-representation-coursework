from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello Mamm\zdf\sdfy"

@app.route('/datainquery', methods=['GET'])
def inquery():
      firstname = request.args["firstname"]
      return "your name is " + firstname
if __name__ == "__main__":
    app.run(debug = True)