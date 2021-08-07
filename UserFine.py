from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

mypass = "password"
mydatabase="book2"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
# Enter Table Names here
bookTable = "book"



def ViewUserFines(userID):
    USERID = userID
    root = Tk()
    root.title("Library")
    root.minsize(width=500, height=220)
    root.geometry("600x220")

    cur.execute("SELECT FineAmount FROM fine WHERE UserID = %s", USERID)
    fineamt = cur.fetchone()[0]


    FineFrame1 = Frame(root, bg="mintcream", bd=5)
    FineFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.16)
    FineLabel = Label(FineFrame1, text= "You have an outstanding amount of ${}".format(fineamt), bg='mintcream', fg='black',
                         font=('Courier', 15))
    FineLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    def paywithcredit():
        if fineamt == 0:
            messagebox.showinfo("Error!", "No fines to be paid.")
        else:
            cur.execute('UPDATE fine Set FineAmount = 0 WHERE UserID = %s', USERID)
            con.commit()
            cur.execute('INSERT INTO payment VALUES("credit", %s, NULL, %s, %s)', (str(USERID), fineamt, str(USERID)))
            con.commit()
            messagebox.showinfo("Success!", "You have no outstanding fines.")
            FineLabel = Label(FineFrame1, text="You have an outstanding amount of ${}".format(fineamt), bg='mintcream',fg='black',
                              font=('Courier', 15))
            FineLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
            refresh()

    def paywithdebit():
        if fineamt == 0:
            messagebox.showinfo("Error!", "No fines to be paid.")
        else:
            cur.execute('UPDATE fine Set FineAmount = 0 WHERE UserID = %s', USERID)
            con.commit()
            cur.execute('INSERT INTO payment VALUES("credit", %s, NULL, %s, %s)', (str(USERID), fineamt, str(USERID)))
            con.commit()
            messagebox.showinfo("Success!", "You have no outstanding fines.")
            FineLabel = Label(FineFrame1, text="You have an outstanding amount of ${}".format(fineamt), bg='mintcream',fg='black',font=('Courier', 15))
            FineLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
            refresh()

    def refresh():
        cur.execute("SELECT FineAmount FROM fine WHERE UserID = %s", USERID)
        fineamt = cur.fetchone()[0]

        FineFrame1 = Frame(root, bg="floral white", bd=5)
        FineFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.16)
        FineLabel = Label(FineFrame1, text="You have an outstanding amount of ${}".format(fineamt), bg='mintcream',
                          fg='black',
                          font=('Courier', 15))
        FineLabel.place(relx=0, rely=0, relwidth=1, relheight=1)





    paywithdebitBtn = Button(root, text="Pay with Debit card", bg='mintcream',fg='black', command=paywithdebit)
    paywithdebitBtn.place(relx=0.15, rely=0.45, relwidth=0.3, relheight=0.1)

    paywithcreditBtn = Button(root, text="Pay with Credit card",bg='mintcream',fg='black', command=paywithcredit)
    paywithcreditBtn.place(relx=0.55, rely=0.45, relwidth=0.3, relheight=0.1)

    # refreshBtn = Button(root, text="refresh", bg='#f7f1e3', fg='black', command=refresh)
    # paywithcreditBtn.place(relx=0.7, rely=0.8, relwidth=0.18, relheight=0.03)

    quitBtn = Button(root, text="Quit", bg='misty rose', fg='black', command=root.destroy)
    quitBtn.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.1)