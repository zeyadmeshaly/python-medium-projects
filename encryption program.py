import random
import string

chars = string.ascii_letters + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(key)
print(chars)

plain_text = input("enter your text ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(plain_text)
print(cipher_text)

import os
os.system("pause")