import customtkinter

def nothing():
    print('There is nothing, like the nothing phone ;)')

def del_dialog_directory():
    root = customtkinter.CTk()
    root.geometry('464x80')
    root.title('Attention!')

    customtkinter.CTkLabel(text='All files in this folder will be deleted but not encrypted. Do you want to continue?').place(x=7, y=10)
    customtkinter.CTkButton(text='Yes', command= nothing, width=50, fg_color='red', hover_color='darksalmon').place(x=174, y=40)
    customtkinter.CTkButton(text='No', command= nothing, width=50, fg_color='green', hover_color='yellowgreen').place(x=234, y=40)

    root.mainloop()

del_dialog_directory()