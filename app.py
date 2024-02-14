from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    return "<h2> Hello </h2>"

@app.route('/fruits', methods=['GET'])
def fruits():
    fruits_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    return jsonify({'fruits': fruits_list})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
