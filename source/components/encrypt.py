from hashlib import sha256
import secrets, string

# obj = sha256(usedforsecurity=True)

# obj.update('Hello'.encode('utf-8'))

# print(obj.hexdigest())

def generate_salt(length=16):
    """
    Generate a random string (salt) of the specified length
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    salt = ''.join(secrets.choice(characters) for _ in range(length))
    return salt

def encrypt_password(password_str, random_salt=""):
    """
    Encrypts the password with added salt
    Returns:
    Hash value of the password and the salt
    """
    if random_salt == "":
        random_salt = generate_salt()
    password_str = random_salt + password_str + random_salt

    sha_obj = sha256(usedforsecurity=True)
    sha_obj.update(password_str.encode('utf-8'))

    return (sha_obj.hexdigest(), random_salt)