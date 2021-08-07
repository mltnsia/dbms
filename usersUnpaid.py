from tkinter import *
import tkinter as tk
from tkinter import ttk
# from Pillow import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "password"
mydatabase="book2"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
# Enter Table Names here
bookTable = "book2"

def usersUnpaid():
    root = Tk()
    root.title("Library")
    global q
    q = StringVar()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("", 'end', values=i)

    wrapper1 = LabelFrame(root, text='Users with unpaid fines')
    wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3), show="headings", height="35")
    trv.pack()
    trv.heading(1, text="UserID")
    trv.column(1, width=100)
    trv.heading(2, text='Name')
    trv.column(2, width=200)
    trv.heading(3, text='Fine Amount ($)')
    trv.column(3, width=200)


    trv.pack(side=LEFT)
    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
    yscrollbar.pack(side=RIGHT, fill='y')

    try:
        getBooks = "SELECT book2.fine.UserID, Uname, FineAmount FROM book2.fine inner join book2.user on book2.fine.UserID = book2.user.userID where book2.fine.fineAmount != 0"
        cur.execute(getBooks)
        rows = cur.fetchall()
        update(rows)
        con.commit()
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.95, relwidth=0.1, relheight=0.03)
    root.mainloop()