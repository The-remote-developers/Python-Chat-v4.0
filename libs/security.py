import rsa

class security:
    def __init__(self):
        pass

    # Function to get public key
    def getPublicKey():
        try:
            # Load public key
            with open('./keys/publicKey.pem', 'rb') as p:
                return rsa.PublicKey.load_pkcs1(p.read())
        except Exception as e:
            return e

    # Function to get private key
    def getPrivateKey():
        try:
            # Load private key
            with open('./keys/privateKey.pem', 'rb') as p:
                return rsa.PrivateKey.load_pkcs1(p.read())
        except Exception as e:
            return e
    
    global privateKey
    global publicKey
    publicKey = getPublicKey()
    privateKey = getPrivateKey()

    # Function to decrypt text using privateKey
    def decrypt(text):
        # Check if type is bytes
        if(type(text) == bytes):
            # Decrypt text
            return rsa.decrypt(text, privateKey).decode('utf-8')
        else:
            raise TypeError("Accept only bytes")

    # Function to encrypt text using publicKey
    def encrypt(text):
        # Check if type is bytes
        if(type(text) == str):
            # Encrypt text
            return rsa.encrypt(text.encode('utf-8'), publicKey)
        else:
            raise TypeError("Accept only str")
    
    def verifyPasscode(passcode, passcode_verify):
        passcode_db_dec = rsa.decrypt(passcode_verify, privateKey).decode('utf-8')
        if passcode == passcode_db_dec:
            return True
        else:
            return False