import pymongo
import certifi
import random
import string

# loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

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