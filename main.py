
string = "This is a top secret message. Tell ,e if you got the message"
encrypt_str = ""
encrypt_key = 50
for i in string:
    encrypt_str += chr(ord(i) + encrypt_key)
print(encrypt_str)

decrypt_str = ""
for x in encrypt_str:
    decrypt_str += chr(ord(x) - encrypt_key)
print(decrypt_str)
