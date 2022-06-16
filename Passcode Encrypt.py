#Simple script to generate a passcode

import rsa

with open('./keys/publicKey.pem', 'rb') as p:
    publicKey = rsa.PublicKey.load_pkcs1(p.read())

passcode = "test"

passcode_enc = rsa.encrypt(passcode.encode('utf-8'), publicKey)
print(passcode_enc)