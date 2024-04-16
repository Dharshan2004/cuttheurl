from flask import Flask, request, render_template, redirect # type: ignore

# initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/<id>', methods=['GET'])
def redirect_url(id):
    return "Hello world"