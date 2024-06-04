from flask import Flask, request, render_template, redirect, url_for, session

# initialize the Flask app
app = Flask(__name__)
app.secret_key = 'secret'

# GET method to render the index.html
@app.route('/', methods=['GET'])
def main():
    shortend_url = session['url']
    session.clear() # clear the session
    return render_template('index.html', url=shortend_url) # render the index.html with the shortened URL(if any)

# POST method to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    session['url'] = url
    return redirect(url_for('main'))

@app.route('/<id>', methods=['GET'])
def redirect_url(id):
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)