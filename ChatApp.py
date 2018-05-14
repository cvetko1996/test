from flask import Flask, request, jsonify
import pymysql

nesto = 'export LC_ALL=C'



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    if 'username' and 'password' in data.keys():
        return jsonify({'info': 'succes'})
    else:
        return jsonify({'info': 'fail'})

@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    if 'username' and 'password' and 'fname' and 'lname' and 'email' in data.keys():
        return jsonify({'info':'succes!'})
    else:
        return jsonify({'info': 'fail'})

if __name__ == '__main__':
    app.run(debug=True)
