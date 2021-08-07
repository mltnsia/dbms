from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql


mypass = "password"
mydatabase="book2"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
# Enter Table Names here
bookTable = "borrowedbooks"

def ViewAllBooks(userID):
    USERID = userID
    root = Tk()
    root.title("Library")
    q = StringVar()

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("", 'end', values=i)

    def _data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)

    # ViewBooks
    wrapper1 = LabelFrame(root, text='All Books')
    wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings", height="30")
    trv.pack()
    trv.heading(1, text="ID")
    trv.column(1, width=30)
    trv.heading(2, text='Title')
    trv.column(2, width=200)
    trv.heading(3, text='Author')
    trv.column(3, width=300)
    trv.heading(4, text="Category")
    trv.column(4, width=150)
    trv.heading(5, text="BorrowedDueDate")
    trv.column(5, width=100)
    trv.heading(6, text="ReservedDate")
    trv.column(6, width=100)





    def selectItem(a):
        curItem = trv.focus()
        value = trv.item(curItem, 'values')

        def reserveItem():
            id = str(value[0])

            cur.execute("SELECT FineAmount FROM fine WHERE UserID = %s", USERID)
            fineamt = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM reservedbooks WHERE ReservedBookID = %s", id)
            checkifReserved = cur.fetchone()[0]

            cur.execute("SELECT BorrowedUserID FROM borrowedbooks WHERE BorrowedBookID = %s", id)
            try:
                BorrowedUser = cur.fetchone()[0]
            except:
                BorrowedUser = ""

            cur.execute("SELECT ReservedUserID FROM ReservedBooks WHERE ReservedBookID = %s", id)
            try:
                ReservedUser = cur.fetchone()[0]
            except:
                ReservedUser = ""

            if str(BorrowedUser) == USERID:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "You have already borrowed this book.")

            elif str(ReservedUser) == USERID:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "You have already reserved this book.")

            elif checkifReserved == 1:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "Book has been reserved by another user.")

            elif fineamt > 0:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "You have an unpaid fine.")

            else:
                try:
                    cur.execute("INSERT INTO reservedbooks VALUES(%s, %s, CURDATE())", (id, USERID))
                    con.commit()
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Reserved", "Your book has been reserved.")
                except:
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Error", "Book cannot be reserved")

        def refresh():
            cur.execute(
                "SELECT BookID, Title, Author, Category, bb.duedate, r.reserveddate FROM book b LEFT JOIN borrowedbooks bb ON b.BookID = bb.BorrowedBookID LEFT JOIN reservedbooks r ON b.BookID = r.reservedBookID")
            rows = cur.fetchall()
            update(rows)
            con.commit()
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Refreshed", "Your library has been refreshed!")

        def borrowItem():
            id = str(value[0])

            cur.execute("SELECT COUNT(*) FROM BorrowedBooks WHERE BorrowedBookID = %s", id)
            checkifBorrowed = cur.fetchone()[0]

            cur.execute("SELECT Fineamount FROM fine WHERE UserID = %s", USERID)
            fineamt = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM BorrowedBooks WHERE BorrowedUserID = %s", USERID)
            checkfour= cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM reservedbooks WHERE ReservedBookID = %s", id)
            checkifReserved = cur.fetchone()[0]

            cur.execute("SELECT ReservedUserID FROM reservedbooks WHERE ReservedBookID = %s", id)
            try:
                ReservedUser = cur.fetchone()[0]
            except:
                ReservedUser = ""

            if fineamt > 0:
                root = Tk()
                root.withdraw()
                messagebox.showinfo("Error", "You have an unpaid fine.")

            elif checkfour>4:
                root = Tk()
                root.withdraw()
                messagebox.showinfo("Error", "You have exceeded the limit of 4 books.")

            elif (checkifReserved == 1) and  (str(ReservedUser) != str(USERID)):
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "Book is reserved by another user.")

            elif checkifBorrowed == 1:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error", "Book is borrowed by another user")


            elif  checkifReserved == 1 and  (str(ReservedUser) == str(USERID)):
                cur.execute("DELETE FROM reservedbooks WHERE ReservedBookID = %s", id)
                con.commit()
                cur.execute("INSERT INTO BorrowedBooks VALUES(%s, %s, 0, DATE_ADD(CURDATE(), INTERVAL 28 DAY), CURDATE())",
                            (id, USERID))
                con.commit()

                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Borrowed", "Your book has been borrowed.")

            else:
                try:
                    cur.execute("INSERT INTO BorrowedBooks VALUES(%s, %s, 0, DATE_ADD(CURDATE(), INTERVAL 28 DAY), CURDATE())",(id, USERID))
                    con.commit()
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Borrowed", "Your book has been borrowed.")
                except:
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Error", "Book cannot be borrowed")



        returnBtn = Button(root, text="Reserve Book", bg='#f7f1e3', fg='black', command=reserveItem)
        returnBtn.place(relx=0.2, rely=0.8, relwidth=0.18, relheight=0.03)

        borrowBtn = Button(root, text="Borrow Book", bg='#f7f1e3', fg='black', command=borrowItem)
        borrowBtn.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.03)

        refreshBtn = Button(root, text="Refresh", bg='#f7f1e3', fg='black', command=refresh)
        refreshBtn.place(relx=0.6, rely=0.8, relwidth=0.18, relheight=0.03)

    trv.bind('<Double-1>', selectItem)

    try:
        cur.execute(
            "SELECT BookID, Title, Author, Category, bb.duedate, r.reserveddate FROM book b LEFT JOIN borrowedbooks bb ON b.BookID = bb.BorrowedBookID LEFT JOIN reservedbooks r ON b.BookID = r.reservedBookID")
        rows = cur.fetchall()
        update(rows)
        con.commit()
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.03)

    root.mainloop()