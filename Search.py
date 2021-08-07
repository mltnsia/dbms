from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
from tkinter import messagebox
from pymongo import MongoClient
import tkinter as tk
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

client = MongoClient()
db = client.library
collection = db.books

mypass = "password"#use your own password
mydatabase="book2" #The database name
con = pymysql.connect(host="localhost",user="root",
                      password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

def searchWindow(searchValue):
    root = Tk()
    root.title("Book Search")
    root.minsize(width=1000, height=750)
    root.geometry("1000x750")
    frame = Frame(root)
    frame.pack()

    #ViewBooks
    wrapper1 = LabelFrame(root, text = 'Search Results')
    wrapper1.pack(fill = 'both', expand = 'yes', padx=10, pady=10)
    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height ="30")
    trv.pack()
    trv.heading(1, text= "Book ID")
    trv.column(1, width=60)
    trv.heading(2, text= 'Title')
    trv.column(2, width=200)
    trv.heading(3, text= 'ISBN')
    trv.column(3, width=100)
    trv.heading(4, text= 'pageCount')
    trv.column(4, width=50)
    trv.heading(5, text= 'publishedDate')
    trv.column(5, width=120)
    trv.heading(6, text='Authors')
    trv.column(6, width=200)
    trv.heading(7, text="Categories")
    trv.column(7, width=200)

    # trv.pack(side=LEFT)
    # yscrollbar = ttk.Scrollbar(wrapper1, orient = "vertical", command = trv.yview)
    # yscrollbar.pack(side=RIGHT, fill='y')

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("", 'end', values=i)

    def search(searchValue):
        rows = collection.find({"title": {"$regex": "^" + searchValue, "$options": 'i'}},
                               {"_id": 1, "title": 1, "isbn": 1, "pageCount": 1,
                                "publishedDate": 1, "authors": 1, "categories": 1})
        # moreRows = collection.find({"title": {"$regex": "." + searchValue, "$options": 'i'}},
        #                            {"_id": 1, "title": 1, "isbn": 1, "pageCount": 1,
        #                             "publishedDate": 1, "authors": 1, "categories": 1})
        for i in rows:
            value = [i.get("_id"), i.get("title"), i.get("isbn"), i.get("pageCount"),
                     i.get("publishedDate"), i.get("authors"), i.get("categories")]
            trv.insert("", 'end', values=value)

        # for i in moreRows:
        #     value = [i.get("_id"), i.get("title"), i.get("isbn"), i.get("pageCount"),
        #              i.get("publishedDate"), i.get("authors"), i.get("categories")]
        #     trv.insert("", 'end', values=value)

    search(searchValue)


#################################
    def selectItem(a):
        curItem = trv.focus()
        value = trv.item(curItem, 'values')
        # Canvas1 = Canvas(root)
        # Canvas1.config(bg="#12a4d9")
        # Canvas1.pack(expand=True, fill=BOTH)

        # def update(rows):
        #     trv2.delete(*trv2.get_children())
        #     for i in rows:
        #         trv2.insert("", 'end', values=i)

        def search(searchValue):
            rows = collection.find({"title": searchValue},
                                   {"longDescription": 1, "thumbnailURL": 1})
            longstring=''
            shortstring=''
            for i in rows:
                # value = [i.get("longDescription"), i.get("thumbnailURL")]
                # trv2.insert("", 'end', values=value)
                shortstring = str(i.get("shortDescription"))
                longstring = str(i.get("longDescription"))
            return [shortstring,longstring]

        def getURL(searchValue):
            rows = collection.find({"title": searchValue},
                                   {"thumbnailUrl": 1})
            string = ''
            for i in rows:
                # value = [i.get("longDescription"), i.get("thumbnailURL")]
                # trv2.insert("", 'end', values=value)
                string = str(i.get("thumbnailUrl"))
            return string

        # Label(fram2, text="Description: " + search(str(value[1])), wraplength=350).grid(row=0, column=0)

        url = getURL(str(value[1]))
        root3=tk.Toplevel()
        root3.title("Book Search")
        root3.minsize(width=600, height=600)
        root3.configure(bg='white')
        root3.geometry("600x500")
        try:
            image_bytes = urlopen(url).read()
        except:
            image_bytes = urlopen("https://mea.nipponpaint-autorefinishes.com/wp-content/uploads/sites/18/2017/07/No-image-found.jpg").read()

        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        w, h = pil_image.size
        fname = url.split('/')[-1]
        sf = "{} ({}x{})".format(fname, w, h)
        root3.title(sf)
        tk_image = ImageTk.PhotoImage(pil_image)
        tk.Label(root3, image=tk_image).pack(padx=5, pady=5)
        tk.Label(root3, text="Short Description: " + search(str(value[1]))[0],justify=LEFT, wraplength=500, bg="white").pack(padx=0, pady=0)
        tk.Label(root3, text="Long Description: " + search(str(value[1]))[1],justify=LEFT, wraplength=500,bg="white").pack(padx=0, pady=0)
        root3.mainloop()

    trv.bind('<Double-1>', selectItem)


    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.03)

