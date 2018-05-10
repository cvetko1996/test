from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/data", methods=['POST'])
def send():
    data = request.get_json()
    s = data['name']
    x = {'info':'yeaa', 'name':s}
    return jsonify(x)


if __name__ == '__main__':
    app.run(port=6000)
