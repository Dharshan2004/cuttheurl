from flask import Flask, request, render_template, redirect, url_for, session
from db_functions import insert_url, get_url

# initialize the Flask app
app = Flask(__name__)
app.secret_key = 'secret'
session = {"url": ""}

# GET method to render the index.html
@app.route('/', methods=['GET'])
def main():
    shortend_url = session['url']
    session['url'] = ""  # clear the session
    print(shortend_url)
    return render_template('index.html', url=shortend_url) # render the index.html with the shortened URL(if any)

# POST method to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    print(url)
    id = insert_url(url)
    session['url'] = f"http://localhost:5000/{id}"
    return redirect(url_for('main'))

@app.route('/<id>', methods=['GET'])
def redirect_url(id):
    print(id)
    url = get_url(id)
    print(url)
    return redirect(url)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)