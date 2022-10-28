import os, glob
import sys
from tkinter import filedialog
from time import sleep
import customtkinter


def quit(root):
    root.destroy()


# Encrypt the file
def encrypt(file):
    have_to_encrypt = open(file, "rb").read()
    key = os.urandom(100)
    encryptet = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))
    with open(file, "wb") as encryptet_out:
        encryptet_out.write(encryptet)

def deletion():
  # Try to delet the file
  try:
      encrypt(file)
      sleep(1)
      os.remove(file)
  except OSError:  # if the deletion failed, you will get a message
      root = customtkinter.CTk()
      root.geometry('300x130')
      root.title('DelSec-Error')

      customtkinter.CTkLabel(text='Unfortunately, deleting the file did not work.').place(x=10, y=3)
      customtkinter.CTkLabel(text='These could be the problems:').place(x=10, y=32)
      customtkinter.CTkLabel(text='- You have not selected a file').place(x=10, y=55)
      customtkinter.CTkLabel(text='- You didnt select a file but a directory').place(x=10, y=75)
      customtkinter.CTkLabel(text='- An unknown error on the part of the program').place(x=10, y=95)

      root.mainloop()


def del_directory():
    dir = file
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

def del_dialog():
    root = customtkinter.CTk()
    root.geometry('314x80')
    root.title('Attention!')

    customtkinter.CTkLabel(text='Are you sure you want to permanently delete the file?').place(x=7, y=10)
    customtkinter.CTkButton(text='Yes', command= lambda: [deletion(), quit(root)], width=50, fg_color='red', hover_color='darksalmon').place(x=95, y=40)
    customtkinter.CTkButton(text='No', command= lambda: quit(root), width=50, fg_color='green', hover_color='yellowgreen').place(x=155, y=40)

    root.mainloop()

def del_dialog_directory():
    root = customtkinter.CTk()
    root.geometry('464x80')
    root.title('Attention!')

    customtkinter.CTkLabel(text='All files in this folder will be deleted but not encrypted. Do you want to continue?').place(x=7, y=10)
    customtkinter.CTkButton(text='Yes', command= lambda: [del_directory(), quit(root)], width=50, fg_color='red', hover_color='darksalmon').place(x=174, y=40)
    customtkinter.CTkButton(text='No', command= lambda: quit(root), width=50, fg_color='green', hover_color='yellowgreen').place(x=234, y=40)

    root.mainloop()
  


# Start the main Program

# Get the file to delet
try: # Try to get a dropped file
    sys.argv[1]
    file = sys.argv[1]

    # Check for Directory
    is_it_Directory = os.path.isdir(file)
    if is_it_Directory == True:
      del_dialog_directory()
      
      
    
except: # If the program doesnt got a dropped file it will show a select dialog
    file = filedialog.askopenfilename()
    del_dialog()

# -- End of Program -- 