import os
from tkinter import filedialog

file = filedialog.askopenfilename()

def encrypt(file): # Your file will be encryptet
    have_to_encrypt = open(file, "rb").read()
    key = os.urandom(100)
    encryptet = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))
    with open(file, "wb") as encryptet_out:
        encryptet_out.write(encryptet)

encrypt(file)