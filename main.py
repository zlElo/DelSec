import customtkinter
import sys
from src.deleter import del_dialog_directory, del_dialog
import os
from tkinter import filedialog

# main GUI
def GUI():
    window = customtkinter.CTk()
    window.geometry('300x150')
    window.title('DelSec')
    window.iconbitmap('src/icon.ico')

    customtkinter.CTkLabel(window, text='DelSec - delete secure').pack(pady=10)

    frame = customtkinter.CTkFrame(window)
    frame.pack()

    delete_file_btn = customtkinter.CTkButton(frame, text='Delete file', command=lambda: del_dialog(filedialog.askopenfilename()))
    delete_file_btn.pack(padx=50, pady=5)

    delete_folder_btn = customtkinter.CTkButton(frame, text='Delete folder', command=lambda: del_dialog_directory(filedialog.askdirectory()))
    delete_folder_btn.pack(padx=50, pady=5)

    window.mainloop()


# Get the file to delet
try: # Try to get a dropped file
    sys.argv[1]
    file = sys.argv[1]

    # Check for Directory
    is_it_Directory = os.path.isdir(file)
    if is_it_Directory == True:
        del_dialog_directory(file)
    else:
        del_dialog(file)
      
except: # If the program doesnt got a dropped file it will show a select dialog
    GUI()

# -- End of Program -- 