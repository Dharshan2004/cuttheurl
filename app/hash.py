import bcrypt

def hash_password(password, salt):
    salt = salt.encode()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def compare_passwords(password, hash):
    return bcrypt.checkpw(password.encode('utf-8'), hash)