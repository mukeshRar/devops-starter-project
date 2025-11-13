from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>DevOps Project Success! - Version 1.0</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)