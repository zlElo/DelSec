import os
from tkinter import filedialog
from tkinter import *


# Get File
file = filedialog.askopenfilename()


# Encrypt the file
def encrypt(file):
    have_to_encrypt = open(file, "rb").read()
    key = os.urandom(100)
    encryptet = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))
    with open(file, "wb") as encryptet_out:
        encryptet_out.write(encryptet)
    

# Try to delet the file
try:
    encrypt(file)
    os.remove(file)
except OSError:  # if the deletion failed, you will get a message
    root = Tk()
    root.geometry('300x100')
    root.title('DelSec-Error')

    Label(text='Unfortunately, deleting the file did not work.').place(x=10, y=3)
    Label(text='These could be the problems:').place(x=10, y=32)
    Label(text='- You have not selected a file').place(x=10, y=55)
    Label(text='- You didnt select a file but a directory').place(x=10, y=75)
    Label(text='- An unknown error on the part of the program').place(x=10, y=95)

    root.mainloop()