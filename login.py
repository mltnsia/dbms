from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from Search import *
from advanced import *
from main import *
from AdminDashboard import *

mypass = "password"
mydatabase="book2"
con = pymysql.connect(host="localhost",user="root",
                      password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # avoid garbage collection

    image = Image.open("shunya-koide-1emWndlDHs0-unsplash.jpg")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label=Label(root2, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)


    global username_verification
    global password_verification

    Label(root2, text='Please Enter your Account Details', bd=5,font=('Courier', 12, 'bold'), relief="flat", bg ="floral white",
          fg="black",width=300).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
    username_verification = StringVar()
    password_verification = StringVar()

    Label(root2, text="Username :", fg="black", bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.35, relwidth=0.25, relheight=0.1)
    username = Entry(root2, textvariable=username_verification)
    username.place(relx=0.4, rely=0.35, relwidth=0.5, relheight=0.1)
    Label(root2, text="Password :", fg="black", bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.5, relwidth=0.25, relheight=0.1)
    password = Entry(root2, textvariable=password_verification, show="*").place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.1)

    Button(root2, text="Login", fg='black', bg="mintcream", relief="flat", font=('Courier', 12, 'bold'),
           command=lambda : login_verification(username.get())).place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

    root2.bind('<Return>', lambda x: login_verification(userID=username.get()))

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Enter Library", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command= lambda: member_log).pack()




def failed():
    # global failed_message
    # failed_message = Toplevel(root2)
    # failed_message.title("Invalid Message")
    # failed_message.geometry("500x100")
    # Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    # Label(failed_message, text="").pack()

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Error", "Invalid Username/Password!")

# def login_verification(userID):
#     user_verification = username_verification.get()
#     pass_verification = password_verification.get()
#     sql = "select * from book2.user where UserID = %s and pass = %s"
#     cur.execute(sql,[(user_verification),(pass_verification)])
#     results = cur.fetchall()
#     if results:
#         for i in results:
#             # main(userID)
#             member_log(userID)
#             break
#     else:
#         failed()

def Exit():
    wayOut = tk.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def Register():
    global root3
    root3 = Toplevel(root)
    root3.title("Account Login")
    root3.geometry("450x300")
    root3.config(bg="white")

    global user_name
    global username_verification2
    global password_verification2

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # avoid garbage collection

    image = Image.open("shunya-koide-1emWndlDHs0-unsplash.jpg")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label=Label(root3, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)

    Label(root3, text='Please Enter your Account Details', bd=5,font=('Courier', 12, 'bold'), relief="flat", fg="black",
                   bg="floral white",width=300).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
    user_name = StringVar()
    username_verification2 = StringVar()
    password_verification2 = StringVar()

    Label(root3, text="Name :", fg="black",bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.1)
    Entry(root3, textvariable=user_name).place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.1)

    Label(root3, text="Username :", fg="black",bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.45, relwidth=0.25, relheight=0.1)
    Entry(root3, textvariable=username_verification2).place(relx=0.4, rely=0.45, relwidth=0.5, relheight=0.1)

    Label(root3, text="Password :", fg="black", bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.6, relwidth=0.25, relheight=0.1)
    Entry(root3, textvariable=password_verification2, show="*").place(relx=0.4, rely=0.6, relwidth=0.5, relheight=0.1)

    Button(root3, text="Sign up",fg='black', bg="mintcream", relief="flat", font=('Courier', 12, 'bold'),command=insert).place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


def insert():
    if (username_verification2 == "" or password_verification2 == ""):
        tkinter.messagebox.showinfo("Insert Status", "please input")
    else:
        user_verification3 = username_verification2.get()
        pass_verification3 = password_verification2.get()
        user_name2 = user_name.get()
        sql = "INSERT INTO book2.user(UserID, Pass, Uname) VALUES ('" + user_verification3 + "','" + pass_verification3 + "','" + user_name2 + "');"
        cur.execute(sql)
        sql2 = "INSERT INTO fine VALUES ('" + user_verification3 + "', 0 , '" + user_verification3 + "')"
        cur.execute(sql2)
        con.commit()
        tk.messagebox.showinfo("Insert status", "Success, please login")

# def Adminlogin():
#     global root2
#     root2 = Toplevel(root)
#     root2.title("Account Login")
#     root2.geometry("450x300")
#     root2.config(bg="white")
#     global username_verification
#     global password_verification
#     Label(root2, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
#                    bg="blue",width=300).pack()
#     username_verification = StringVar()
#     password_verification = StringVar()
#     Label(root2, text="").pack()
#     Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
#     Entry(root2, textvariable=username_verification).pack()
#     Label(root2, text="").pack()
#     Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
#     Entry(root2, textvariable=password_verification, show="*").pack()
#     Label(root2, text="").pack()
#     Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command= lambda:Admin_login_verification()).pack()
#     Label(root2, text="")
#     root2.bind('<Return>', lambda event: AdminDashboard())



def Admin_logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Get in", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=AdminDashboard).pack()


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # avoid garbage collection

    image = Image.open("shunya-koide-1emWndlDHs0-unsplash.jpg")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label=Label(root, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)

    Label(root,text='Welcome to the Library',  bd=20, font=('Courier', 20, 'bold'), relief="flat", bg ="floral white", fg="black",
                 width=300).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
    Button(root, text='Admin Login', height="1", width="20", bd=8, font=('Courier', 12, 'bold'), relief="flat", fg="black",
           bg="mintcream", command=Adminlogin).place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)

    Button(root,text='Member Login', height="1",width="20", bd=8, font=('Courier', 12, 'bold'), relief="flat", fg="black",
                   bg="mintcream",command=login).place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    Button(root, text='Member Sign up', height="1", width="20", bd=8, font=('Courier', 12, 'bold'), relief="flat", fg="black",
           bg="mintcream", command=Register).place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

    Button(root,text='Exit', height="1",width="20", bd=8, font=('Courier', 12, 'bold'), relief="flat", fg="black",
                   bg="mistyrose",command=Exit).place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


def login_verification(userID):
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from book2.user where UserID = %s and pass = %s"
    cur.execute(sql,[(user_verification),(pass_verification)])
    results = cur.fetchall()
    if results:
        for i in results:
            # main(userID)
            member_log(userID)
            break
    else:
        failed()

def member_log(userID):
    root.destroy()
    main(userID)

def Adminlogin():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")
    global username_verification
    global password_verification

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # avoid garbage collection

    image = Image.open("shunya-koide-1emWndlDHs0-unsplash.jpg")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label=Label(root2, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)

    Label(root2, text='Please Enter your Account Details', bd=5,font=('Courier', 12, 'bold'), relief="flat", fg="black",
                   bg="floral white" ,width=300).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)

    username_verification = StringVar()
    password_verification = StringVar()

    Label(root2, text="Username :", fg="black", bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.35, relwidth=0.25, relheight=0.1)
    Entry(root2, textvariable=username_verification).place(relx=0.4, rely=0.35, relwidth=0.5, relheight=0.1)
    Label(root2, text="Password :", fg="black", bg="mintcream", font=('Courier', 12, 'bold')).place(relx=0.1, rely=0.5, relwidth=0.25, relheight=0.1)
    Entry(root2, textvariable=password_verification, show="*").place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.1)
    Button(root2, text="Login", bg="mintcream", fg='black', relief="flat", font=('Courier', 12, 'bold'),command= lambda:Admin_login_verification())\
        .place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)
    root2.bind('<Return>', lambda event: Admin_login_verification())

def Admin_login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from book2.admin where AdminID = %s and pass = %s"
    cur.execute(sql,[(user_verification),(pass_verification)])
    results = cur.fetchall()
    if results:
        for i in results:
            # Admin_logged()
            admin_log_success()
            break
    else:
        failed()

def admin_log_success():
    root.destroy()
    AdminDashboard()



main_display()

root.mainloop()