from hashlib import sha256

obj = sha256(usedforsecurity=True)

obj.update('Hello'.encode('utf-8'))

print(obj.hexdigest())