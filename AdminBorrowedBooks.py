from tkinter import *
import tkinter as tk
from tkinter import ttk
# from Pillow import ImageTk,Image
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

mypass = "password"
mydatabase="book2"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
# Enter Table Names here
bookTable = "book2"

def ViewBorrowedBooks():
    root = Tk()
    root.title("Library")
    global q
    q = StringVar()

  #  root.minsize(width=400, height=400)
  #  root.geometry("600x500")

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("", 'end', values=i)

    def search():
        q2 = q.get()
        query = "SELECT * FROM book WHERE BookID = " + q2
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        update(rows)

    def clear():
        query = "SELECT * FROM book WHERE DueDate IS NOT NULL"
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        update(rows)

    #Search section
    # wrapper2 = LabelFrame(root, text = "Search")
    # wrapper2.pack(fill = "both", padx=10, pady=10)
    # ClearBtn = Button(wrapper2, text="Clear", command = clear)
    # ClearBtn.pack(side=tk.RIGHT, padx=6)
    # SearchBtn = Button(wrapper2, text="Search", command = search)
    # SearchBtn.pack(side=tk.RIGHT, padx=6)
    # entry3 = Entry(wrapper2, textvariable=q, width = 200)
    # entry3.pack(side=tk.RIGHT, expand = 'yes', padx=20)



    #ViewBooks
    wrapper1 = LabelFrame(root, text = 'BorrowedBooks')
    wrapper1.pack(fill = 'both', expand = 'yes', padx=10, pady=10)
    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8), show = "headings", height ="35")
    trv.pack()
    trv.heading(1, text= "BookID")
    trv.column(1, width=100)
    trv.heading(2, text= 'Title')
    trv.column(2, width=200)
    trv.heading(3, text= 'Author')
    trv.column(3, width=200)
    trv.heading(4, text= 'Category')
    trv.column(4, width=200)
    trv.heading(5, text='Publisher')
    trv.column(5, width=100)
    trv.heading(6, text="YearOfPublication")
    trv.column(6, width=100)
    trv.heading(7, text="UserID")
    trv.column(7, width=100)
    trv.heading(8, text="Due date")
    trv.column(8, width=100)

    trv.pack(side=LEFT)
    #scrollbar
    yscrollbar = ttk.Scrollbar(wrapper1, orient = "vertical", command = trv.yview)
    yscrollbar.pack(side=RIGHT, fill='y')

  #  Canvas1 = Canvas(root)
   # Canvas1.config(bg="#12a4d9")
    #Canvas1.pack(expand=True, fill=BOTH)
   # headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    #headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    #headingLabel = Label(headingFrame1, text="View Borrowed Books", bg='black', fg='white', font=('Courier', 15))
    #headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    #labelFrame = Frame(root, width=500, height=500, bg='black')
    #labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    #y = 0.25
    #scrollbar = Scrollbar(labelFrame, orient="horizontal")
   # scrollbar.pack(side = BOTTOM, fill = X)
    #Label(labelFrame, text="%s%15s%-50s%-50s%-30s%-40s%-50s%-40s%-40s" % ('BookID', 'Title', 'Author', 'Category', 'Publisher',
     ##    bg='black', fg='white').place(relx=0.07, rely=0.1)
    #Label(labelFrame, text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='black',
     #     fg='white').place(relx=0.05, rely=0.2)

   # getBooks = "select * from book where DueDate IS NOT NULL"
    try:
        getBooks = "SELECT BookID, Title, Author, Category, Publisher, YearOfPublication, BorrowedUserID, DueDate FROM book b RIGHT JOIN borrowedbooks c ON b.BookID = c.BorrowedBookID"
        cur.execute(getBooks)
        rows = cur.fetchall()
        update(rows)
        con.commit()
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.98, relwidth=0.1, relheight=0.03)
    root.mainloop()