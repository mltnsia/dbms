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
bookTable = "borrowedbooks"

def MemberViewBorrowedBooks(userID):
    USERID = userID
    root = Tk()
    root.title("Library")
    q = StringVar()
    # root.minsize(width=600, height=300)
    # root.geometry("600x300")
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("", 'end', values=i)

    def _data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)


    #ViewBooks
    wrapper1 = LabelFrame(root, text = 'BorrowedBooks')
    wrapper1.pack(fill = 'both', expand = 'yes', padx=10, pady=10)
    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show = "headings", height ="30")
    trv.pack()
    trv.heading(1, text= "BookID")
    trv.column(1, width=100)
    trv.heading(2, text= 'Title')
    trv.column(2, width=200)
    trv.heading(3, text= 'Author')
    trv.column(3, width=200)
    trv.heading(4, text="DueDate")
    trv.column(4, width=100)
    trv.heading(5, text="BorrowedDate")
    trv.column(5, width=100)

    def selectItem(a):
        curItem = trv.focus()
        value = trv.item(curItem, 'values')

        def returnItem():
            id = str(value[0])
            #returnQuery = "UPDATE borrowedbooks SET UserID = NULL WHERE BorrowedBookID = " + id
            returnQuery = "DELETE FROM borrowedbooks WHERE BorrowedBookID = " + id
            cur.execute(returnQuery)
            con.commit()
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Returned", "Your book has been returned.")

        def extendItem():
            id = str(value[0])
            cur.execute("SELECT COUNT(*) FROM Reservedbooks WHERE ReservedBookID = %s", id)
            isReserved = cur.fetchone()[0]
            cur.execute("SELECT isExtended FROM BorrowedBooks WHERE BorrowedBookID = %s", id)
            isExtended = cur.fetchone()[0]
            if isReserved == 1:
                root = Tk()
                root.withdraw()
                messagebox.showinfo("Error", "Book cannot be extended because it is reserved by another user.")

            elif isExtended == True:
                root = Tk()
                root.withdraw()
                messagebox.showinfo("Error", "Book has already been extended once.")
            else:
                extendQuery = 'UPDATE borrowedbooks SET DueDate = DATE_ADD(DueDate, INTERVAL 28 DAY) WHERE isExtended = false AND BorrowedBookID NOT IN (SELECT ReservedBookID FROM Reservedbooks) AND BorrowedBookID = ' + id
                cur.execute(extendQuery)
                disableExtendQuery = 'UPDATE borrowedbooks SET isExtended = true WHERE BorrowedBookID =' + id
                cur.execute(disableExtendQuery)
                con.commit()
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Extended", "Your book has been extended by 4 weeks. You can only extend it once provided it is not reserved.")


        def refresh():
            cur.execute("SELECT BorrowedBookID, Title, Author, DueDate, BorrowedDate FROM BorrowedBooks BB LEFT JOIN book ON BB.BorrowedBookID = book.bookID WHERE BB.BorrowedUserID = %s", USERID)
            rows = cur.fetchall()
            update(rows)
            con.commit()
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Refreshed", "Your library has been refreshed!")

        returnBtn = Button(root, text="Return Book", bg='#f7f1e3', fg='black', command=returnItem)
        returnBtn.place(relx=0.2, rely=0.8, relwidth=0.18, relheight=0.03)

        extendBtn = Button(root, text="Extend Book", bg='#f7f1e3', fg='black', command=extendItem)
        extendBtn.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.03)

        refreshBtn = Button(root, text="Refresh", bg='#f7f1e3', fg='black', command=refresh)
        refreshBtn.place(relx=0.6, rely=0.8, relwidth=0.18, relheight=0.03)

    trv.bind('<Double-1>', selectItem)

    try:
        cur.execute("SELECT BorrowedBookID, Title, Author, DueDate, BorrowedDate FROM BorrowedBooks BB LEFT JOIN book ON BB.BorrowedBookID = book.bookID WHERE BB.BorrowedUserID = %s", USERID)
        rows = cur.fetchall()
        update(rows)
        con.commit()
    except:
        messagebox.showinfo("Failed to fetch files from database")


    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.03)

    root.mainloop()