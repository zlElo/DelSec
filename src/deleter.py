import os, glob
from time import sleep
import customtkinter
import shutil


def quit(root):
    root.destroy()


# Encrypt the file
def encrypt(file):
    have_to_encrypt = open(file, "rb").read()
    key = os.urandom(100000)
    encryptet = bytes(a ^ b for (a, b) in zip(have_to_encrypt, key))
    with open(file, "wb") as encryptet_out:
        encryptet_out.write(encryptet)


def deletion(file):
  # Try to delet the file
    try:
        encrypt(file)
        sleep(1)
        os.remove(file)
    except OSError:  # if the deletion failed, you will get a message
        root = customtkinter.CTk()
        root.geometry('300x130')
        root.title('DelSec-Error')

        customtkinter.CTkLabel(root, text='Unfortunately, deleting the file did not work.').place(x=10, y=3)
        customtkinter.CTkLabel(root, text='These could be the problems:').place(x=10, y=32)
        customtkinter.CTkLabel(root, text='- You have not selected a file').place(x=10, y=55)
        customtkinter.CTkLabel(root, text='- You didnt select a file but a directory').place(x=10, y=75)
        customtkinter.CTkLabel(root, text='- An unknown error on the part of the program').place(x=10, y=95)

        root.mainloop()


def del_directory(file, root):
    def start_deletion():
        root.destroy()
        dir = file
        filelist = glob.glob(os.path.join(dir, "*"))
        items_all = len(filelist)
        items = 0
        for f in filelist:
            encrypt(f)
            os.remove(f)

            items += 1
            done = int(50*items/items_all)
            bar.set(done/50)

            files_deleted.configure(text=f'{items}/{items_all} files removed')

            win.update()
            win.update_idletasks()
        
        shutil.rmtree(dir)
        win.title('Progress done!')
        files_deleted.configure(text=f'Done! You can close this window', text_color='green')


    win = customtkinter.CTk()
    win.geometry('314x80')
    win.title('Progress...')

    bar = customtkinter.CTkProgressBar(win)
    bar.pack(pady=15)

    files_deleted = customtkinter.CTkLabel(win, text='', text_color='red')
    files_deleted.pack(pady=3)

    # Schedule start_deletion() to be called after 0 milliseconds
    win.after(500, start_deletion)

    win.mainloop()

    
        

def del_dialog(file):
    root = customtkinter.CTk()
    root.geometry('314x80')
    root.title('Attention!')

    customtkinter.CTkLabel(root, text='Are you sure you want to permanently delete the file?').place(x=7, y=10)
    customtkinter.CTkButton(root, text='Yes', command= lambda: [deletion(file), quit(root)], width=50, fg_color='red', hover_color='darksalmon').place(x=95, y=40)
    customtkinter.CTkButton(root, text='No', command= lambda: quit(root), width=50, fg_color='green', hover_color='yellowgreen').place(x=155, y=40)

    root.mainloop()


def del_dialog_directory(file):

    def btn_command():
        del_directory(file, root)
        

    root = customtkinter.CTk()
    root.geometry('314x80')
    root.title('Attention!')

    customtkinter.CTkLabel(root, text='Are you sure you want to permanently delete the files?').place(x=7, y=10)
    customtkinter.CTkButton(root, text='Yes', command= btn_command, width=50, fg_color='red', hover_color='darksalmon').place(x=95, y=40)
    customtkinter.CTkButton(root, text='No', command= lambda: quit(root), width=50, fg_color='green', hover_color='yellowgreen').place(x=155, y=40)

    root.mainloop()
  