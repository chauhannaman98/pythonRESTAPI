from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    result = {
        'status': True,
        'response': 'Hello World!'
    }
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
