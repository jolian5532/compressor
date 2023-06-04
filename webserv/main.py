from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    folder = request.files['folder']
    print(folder)

    return "!"

app.run(host='localhost', port=5151)