from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello Mamm\zdf\sdfy"

@app.route('/datainquery', methods=['GET'])
def inquery():
      queryargs = {
            "firstname" : request.args["firstname"],
            "age" : request.args["age"]
      }
      print (queryargs)
      return jsonify (queryargs)

if __name__ == "__main__":
    app.run(debug = True)