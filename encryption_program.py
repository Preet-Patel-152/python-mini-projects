import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)


# Encryption process
plain_text = input("Enter the message to encrypt: ")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print(f"Encrypted message: {plain_text}")
print(f"encryption key: {cipher_text}")


# Decryption process
cipher_text = input("Enter the message to encrypt: ")
plain_text = ""

for char in cipher_text:
    index = key.index(char)
    plain_text += chars[index]

print(f"")
