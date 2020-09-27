import hashlib

def md5pwd(password):
    m = hashlib.md5(password.encode("utf8")).hexdigest()
    return m