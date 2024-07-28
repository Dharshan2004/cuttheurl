import pymongo
import certifi
import random
import string
from .hash import hash_password, compare_passwords

# loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

def generate_user_id():
    id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(15)])
    while check_user_id(id):
        id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(15)])
    return id

def check_user_id(user_id):
    client, db = get_db_connection()
    users = db.users
    user = users.find_one({"_id": user_id})
    client.close()
    if user is None:
        return True
    else:
        return False

# Generate a unique id for the URL
def generate_id():
    id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(10)])
    return id

# MongoDB connection
def get_db_connection():
    client = pymongo.MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
    db = client.get_database("app")
    return [client, db]

# Insert URL into the database
def insert_url(url):
    client, db = get_db_connection()
    id = generate_id()
    # check if the id is unique
    while get_url(id) is not None:
        id = generate_id()
    if url.startswith("http://") or url.startswith("https://"):
        pass
    else:
        url = "http://" + url
    urls = db.urls
    urls.insert_one({"_id":id, "url": url})
    client.close()
    return id

# Get URL from the database
def get_url(id):
    client, db = get_db_connection()
    urls = db.urls
    url = urls.find_one({"_id": id})
    client.close()
    if url is not None:
        return url['url']
    else:
        return None

def create_user(email, password):
    client, db = get_db_connection()
    users = db.users
    user = users.find_one({"email": email})
    if user is None:
        id = generate_user_id()
        salt = db.salt.find_one()['salt']
        password = hash_password(password, salt).decode()
        users.insert_one({"_id": id, "email": email, "password": password})
        client.close()
        return id
    else:
        client.close()
        return False
    
def login_user(email, password):
    client, db = get_db_connection()
    users = db.users
    user = users.find_one({"email": email})
    client.close()
    if user is not None:
        pw = user['password']
        if compare_passwords(password, pw):
            return True
        else:
            return False
    else:
        return False
    
def get_user(user_id):
    client, db = get_db_connection()
    users = db.users
    user = users.find_one({"_id": user_id})
    client.close()
    return user