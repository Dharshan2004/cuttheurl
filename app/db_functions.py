import sqlite3
import random
import string

def generate_id():
    id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(10)])
    return id
 
def create_database():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE "url_directory" (
	"id"	TEXT UNIQUE,
	"actual_url"	TEXT NOT NULL,
	PRIMARY KEY("id")
);''')
    con.commit()
    con.close()

def insert_url(actual_url):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    id = generate_id()
    if actual_url.startswith("http://") or actual_url.startswith("https://"):
        actual_url = actual_url
    else:
        actual_url = "http://" + actual_url
    while True:
        try:
            cur.execute("INSERT INTO url_directory (id, actual_url) VALUES (?, ?)", (id, actual_url))
            con.commit()
            break
        except sqlite3.IntegrityError:
            id = generate_id()
    con.commit()
    con.close()
    return id

def get_url(id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT actual_url FROM url_directory WHERE id = ?", (id,))
    con.commit()
    url = cur.fetchone()
    con.close()
    return url