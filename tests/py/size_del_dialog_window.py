import customtkinter

def nothing():
    print('There is nothing, like the nothing phone ;)')

root = customtkinter.CTk()
root.geometry('314x80')
root.title('Attention!')

customtkinter.CTkLabel(text='Are you sure you want to permanently delete the file?').place(x=7, y=10)
customtkinter.CTkButton(text='Yes', command= nothing, width=50, fg_color='red', hover_color='darksalmon').place(x=95, y=40)
customtkinter.CTkButton(text='No', command= nothing, width=50, fg_color='green', hover_color='yellowgreen').place(x=155, y=40)

root.mainloop()