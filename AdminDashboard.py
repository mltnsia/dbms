from tkinter import *
from AdminReservedBooks import *
from AdminBorrowedBooks import *
from usersUnpaid import *
import io
from urllib.request import urlopen
from PIL import ImageTk,Image
from tkinter import messagebox



mypass = "password" #use your own password
mydatabase="book2" #The database name
con = pymysql.connect(host="localhost",user="root",
                      password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor


def AdminDashboard():
    root = Tk()
    root.title("Admin")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

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
    label = Label(root, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)

    headingFrame1 = Frame(root, bg="floral white", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome back, Admin!", bg='floral white', fg='black',
                         font=('Courier', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    btn1 = Button(root, text="Books Borrowed", bg='mintcream', fg='black', command=ViewBorrowedBooks)
    btn1.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    btn2 = Button(root, text="Books Reserved", bg='mintcream', fg='black', command=ViewRbooks)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
    btn3 = Button(root, text="Users with unpaid fines", bg='mintcream', fg='black', command=usersUnpaid)
    btn3.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    root.mainloop()
