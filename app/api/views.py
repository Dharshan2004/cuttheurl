from flask import render_template, redirect, url_for, session, request, jsonify
from . import api

from app.db_functions import insert_url, get_url

@api.route('/shorten', methods=['POST'])
def shorten():
    # get the actual URL from the request
    data = request.get_json()
    
    # insert the URL into the database and get the shortened URL
    url = data['url']
    id = insert_url(url)

    # return the shortened URL
    res = [{"shortened_url": f"http://localhost:5000/{id}"}]
    return jsonify(res)

@api.route('/get/<id>', methods=['GET'])
def get_url_api(id):
    # get the actual URL from the database
    url = get_url(id)
    
    # return the actual URL
    res = [{"actual_url": url}]
    return jsonify(res)