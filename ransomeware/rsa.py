from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(pubKey)
pubKey = RSA.import_key(pubKey.export_key())
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", (encrypted))
privkey = RSA.import_key(keyPair.export_key())
with open('private.pem', 'wb') as f:
    f.write(keyPair.export_key())

# save public key to file
with open('public.pem', 'wb') as f:
    f.write(pubKey.export_key())
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)