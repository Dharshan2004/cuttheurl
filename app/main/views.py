from flask import render_template, redirect, url_for, session, request, abort
from . import main
from app.db_functions import insert_url, get_url

session = {"url": ""}

@main.route('/', methods=['GET'])
def index():
    shortend_url = session['url']
    session['url'] = ""  # clear the session
    return render_template('index.html', url=shortend_url) # render the index.html with the shortened URL(if any)

@main.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    id = insert_url(url)
    session['url'] = url_for('main.redirect_url', id=id, _external=True)
    return redirect(url_for('main.index'))

@main.route('/<id>', methods=['GET'])
def redirect_url(id):
    url = get_url(id)
    if url is None:
        return abort(404)
    else:
        return redirect(url)


