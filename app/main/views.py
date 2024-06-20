from flask import render_template, redirect, url_for, session, request
from . import main
from app.db_functions import insert_url, get_url

@main.route('/', methods=['GET'])
def index():
    shortend_url = session['url']
    session['url'] = ""  # clear the session
    print(shortend_url)
    return render_template('index.html', url=shortend_url) # render the index.html with the shortened URL(if any)

@main.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    id = insert_url(url)
    session['url'] = f"http://localhost:5000/{id}"
    return redirect(url_for('main.index'))

@main.route('/<id>', methods=['GET'])
def redirect_url(id):
    url = get_url(id)
    if url is None:
        return redirect(url_for('page_not_found'))
    else:
        return redirect(url)


