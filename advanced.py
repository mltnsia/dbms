from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
from tkinter import messagebox
from pymongo import MongoClient
from advancedSearch import *
from Search import *

client = MongoClient()
db = client.library
collection = db.books

mypass = "password"#use your own password
mydatabase="book2" #The database name
con = pymysql.connect(host="localhost",user="root",
                      password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor


def advancedWindow():
    root = Tk()
    root.title("Advanced Search")
    root.minsize(width=320, height=240)
    root.geometry("320x240")


    wrapper1 = LabelFrame(root, text = 'Advanced Search Results')
    wrapper1.pack(fill = 'both', expand = 'yes', padx=10, pady=10)
    #trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height ="30")
    # trv.pack()
    # trv.heading(1, text= "Long Description")
    # trv.column(1, width=100)
    # trv.heading(2, text= 'Title')
    # trv.column(2, width=200)

    fram = Frame(root)
    fram.pack(side=TOP)
    fram.place(relx=0.1, rely=0.2, relwidth=0.90, relheight=0.45)

    Label(fram, text='Title:').grid(row=1,column=1)
    edit1 = Entry(fram)
    edit1.grid(row=1,column=2)
    edit1.focus_set()

    Label(fram, text='ISBN').grid(row=2,column=1)
    edit2 = Entry(fram)
    edit2.grid(row=2,column=2)
    edit2.focus_set()

    Label(fram, text='Published Year').grid(row=3,column=1)
    edit3 = Entry(fram)
    edit3.grid(row=3,column=2)
    edit3.focus_set()

    Label(fram, text='Authors').grid(row=4,column=1)
    edit4 = Entry(fram)
    edit4.grid(row=4,column=2)
    edit4.focus_set()

    Label(fram, text='Categories').grid(row=5, column=1)
    edit5 = Entry(fram)
    edit5.grid(row=5, column=2)
    edit5.focus_set()

    def getCommand():
        if edit1.get() + edit2.get() + edit3.get() + edit4.get() + edit5.get() == '':
            return searchWindow('')
        else:
            return advancedSearchWindow({"title": edit1.get(), "isbn": edit2.get(),
                                         "publishedDate": edit3.get(), "authors": edit4.get(),
                                         "categories": edit5.get()})

    butt = Button(fram, text='Find', command=lambda: getCommand())

    root.bind("<Return>", lambda event: getCommand())
    butt.grid(row=1,column=3)












