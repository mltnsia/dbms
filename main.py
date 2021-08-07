from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import io
from urllib.request import urlopen
from Search import *
from advanced import *
from UserFine import *
from BorrowedBooks import *
from ReservedBooks import *
from ViewAllBooks import *
import datetime
from PIL import Image

client = MongoClient()
book = client.Library
collection = book.book

mypass = "password"#use your own password
mydatabase="book2" #The database name
con = pymysql.connect(host="localhost",user="root",
                      password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor



def main(userID):
    root = Tk()
    root.title("Library")
    root.minsize(width=560,height=400)
    root.geometry("700x700")

    # def CheckFine(UserID):
    #     cur.execute("SELECT FineAmount FROM fine WHERE UserID = %s", UserID)
    #     fineamt = cur.fetchone()[0]
    #     CheckDueDate = "SELECT DueDate FROM book2.borrowedbooks where BorrowedUserID = '" + UserID + "'";
    #     cur.execute(CheckDueDate)
    #     DueDate = cur.fetchall()
    #     fineAmt = 0
    #     for bookDueDate in DueDate:
    #         today = datetime.date.today()
    #         fineDays = (today - bookDueDate[0]).days
    #         if fineDays > 0:
    #             fineAmt += int(fineDays)
    #     Fine = fineamt + fineAmt
    #     sql = "UPDATE fine Set FineAmount = '" + str(Fine) + "' WHERE UserID = '" + UserID + "'"
    #     cur.execute(sql)
    #     con.commit()
    #     if Fine > 0:
    #         cur.execute("DELETE FROM reservedbooks WHERE ReservedUserID = '" + UserID + "'")
    #         con.commit()
    # CheckFine(userID)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    image = Image.open("shunya-koide-1emWndlDHs0-unsplash.jpg")
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label=Label(root, image=photo)
    label.pack(fill=BOTH, expand=YES)
    label.bind('<Configure>', resize_image)

    cur.execute("SELECT Uname from user WHERE UserID = %s", userID)
    name = cur.fetchone()[0]


    headingFrame1 = Frame(root,bg="floral white",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome, " + name, bg='floral white', fg='black', font=('Courier',18, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn0 = Button(root, text="The Library", font=('Courier', 12, 'bold'), bg='mintcream', fg='black',
                  command=lambda: ViewAllBooks(userID))
    btn0.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

    btn1 = Button(root, text="My Borrowed Books",font=('Courier',12, 'bold') , bg='mintcream', fg='black',
                  command=lambda: MemberViewBorrowedBooks(userID))
    btn1.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="My Reserved Books", font=('Courier',12, 'bold') , bg='mintcream', fg='black',
                  command=lambda: MemberViewReservedBooks(userID))
    btn2.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="My Fines",font=('Courier',12, 'bold') ,bg='mintcream', fg='black',command=lambda: ViewUserFines(userID))
    btn3.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)

    fram = Frame(root, bg='mintcream', width = 400, height = 100)
    Label(fram,font=('Courier', 9,'bold'), bg='mintcream', fg='black', text='Book Search:').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH,expand=1)
    edit.focus_set()

    bt = Button(fram, text="Advanced", bg='mintcream',font=('Courier', 9,'bold'), fg='black',command=lambda: advancedWindow())
    bt.configure(width=8,height=4)
    bt.pack(side=RIGHT)

    butt = Button(fram, text='Find', bg='mintcream',font=('Courier', 9, 'bold'), fg='black', command= lambda: searchWindow(edit.get()))
    butt.configure(width=5, height=4)
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    fram.place(relx=0.28, rely=0.4, relwidth=0.5, relheight=0.045)

    root.bind('<Return>', lambda event : searchWindow(edit.get()))

    root.mainloop()

