from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "harsh" and password == "pass1234":
        messagebox.showinfo("Login", "Welcome to F1 Portal!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = Tk()
root.title("F1 Login")
root.geometry("600x500")
root.resizable(False, False)


bg_img = Image.open("fuk.jpg")   
bg_img = bg_img.resize((600,500))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


login_frame = Frame(root, bg="black", bd=0)
login_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=320, height=360)


logo_img = Image.open("flogo.png")  
logo_img = logo_img.resize((120,60))
logo = ImageTk.PhotoImage(logo_img)

logo_label = Label(login_frame, image=logo, bg="black")
logo_label.pack(pady=15)


title = Label(login_frame, text="F1 LOGIN", fg="white", bg="black",
              font=("Arial",18,"bold"))
title.pack(pady=5)


user_label = Label(login_frame, text="Username", fg="white",
                   bg="black", font=("Arial",12))
user_label.pack(pady=(15,5))

user_entry = Entry(login_frame, font=("Arial",12), width=25)
user_entry.pack()


pass_label = Label(login_frame, text="Password", fg="white",
                   bg="black", font=("Arial",12))
pass_label.pack(pady=(15,5))

pass_entry = Entry(login_frame, show="*", font=("Arial",12), width=25)
pass_entry.pack()


login_btn = Button(login_frame, text="LOGIN", command=login,
                   bg="#e10600", fg="white",
                   font=("Arial",12,"bold"), width=15)
login_btn.pack(pady=25)

root.mainloop()
