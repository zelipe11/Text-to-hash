import hashlib

text = 'Teste do texto em teste'

textToSHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
textToMD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

print("\"" +myText + "\" - " + SHA256 + " - " + MD5)