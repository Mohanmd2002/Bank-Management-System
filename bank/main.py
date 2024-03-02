'''connections'''
from functools import partial
from tkinter import *

from tkinter import messagebox
import pymysql
import colors as cs
import database as db

import random
import datetime

import pymysql
from tkinter import *
from tkinter import ttk

class Bank_management:
    def __init__(self,root):
        self.window = root
        self.window.title("Bank Management System")
        self.window.maxsize(width=1000 ,  height=700)
        self.window.minsize(width=1000 ,  height=700)

        #self.window.geometry("780x480")
        self.window.config(bg = "white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.color_5 = cs.color_5
        self.color_6 = cs.color_6
        self.color_7 = cs.color_7

        
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
##        self.host = db.host
##        self.user = db.user
##        self.password = db.password
##        self.database = db.database

        #left frame
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        #buttons
        self.user_register=Button(self.frame_1,text="USER REGISTER",font=(self.font_1,12), bd=2, command=self.User_Register,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=100,width=300)
        self.user_register=Button(self.frame_1,text="BANK ACCOUNT",font=(self.font_1,12), bd=2, command=self.Bank_Account,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=300,width=300)
        self.user_register=Button(self.frame_1,text="WALLET BALANCE",font=(self.font_1,12), bd=2, command=self.Wallet_Balance,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=500,width=300)
        self.user_register=Button(self.frame_1,text="EXIT",font=(self.font_1,12), bd=2, command=self.Exit,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
    
        """main"""
    def User_Register(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Back_to_home,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()

        self.name = Label(self.frame_2, text="USER REGISTER", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=400,y=5)
        
        self.f_name = Label(self.frame_2, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=80)
        self.f_name_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.f_name_entry.place(x=450,y=87, width=300)

        self.l_name = Label(self.frame_2, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=160)
        self.l_name_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.l_name_entry.place(x=450,y=167, width=300)

        self.contact = Label(self.frame_2, text="Contact No", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=240)
        self.contact_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=450,y=247, width=300)
        
        self.user_name = Label(self.frame_2, text="User Name", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=320)
        self.user_name_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.user_name_entry.place(x=450,y=327, width=300)

        self.password = Label(self.frame_2, text="Password", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=400)
        self.password_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.password_entry.place(x=450,y=407, width=300)

        self.submit_bt_1 = Button(self.frame_2, text='Submit', font=(self.font_1, 12), bd=2,command=self.Submit, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=250,y=480,width=100)
        
        self.clear_bt_1 = Button(self.frame_2, text='Cancel', font=(self.font_1, 12), bd=2,command=self.ClearScreen, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=400,y=480,width=100)
        
        '''submit'''
    def Submit(self):
        if (self.f_name_entry.get() == "" or self.l_name_entry.get() == "" or self.contact_entry.get() == "" or self.password_entry.get() == ""or self.user_name_entry.get() == ""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
                curs = connection.cursor()
                curs.execute("select * from bank_register where contact=%s", self.contact_entry.get())
                row=curs.fetchone()
                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into bank_register (f_name,l_name,contact,user_name,password,wallet_balance)values(%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.f_name_entry.get(),
                                            self.l_name_entry.get(),
                                            self.contact_entry.get(),
                                            self.user_name_entry.get(),
                                            self.password_entry.get(),
                                            100000
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                pass
##                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def Bank_Account(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Back_to_home,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2 = Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()
        
        self.name = Label(self.frame_2, text="BANK ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=400,y=100)
        
        self.user_name2 = Label(self.frame_2, text="USER NAME", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=200)
        self.user_name2_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.user_name2_entry.place(x=450,y=205, width=300)
 
        self.password2 = Label(self.frame_2, text="PASSWORD", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=300)
        self.password2_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.password2_entry.place(x=450,y=300, width=300)

        self.submit_bt_2 = Button(self.frame_2, text='Submit', font=(self.font_1, 12), bd=2,command=self.CheckBankAccount, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=250,y=450,width=100)

        self.clear_bt_1 = Button(self.frame_2, text='Cancel', font=(self.font_1, 12), bd=2,command=self.ClearScreen, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=400,y=450,width=100)
        
    def CheckBankAccount(self):
        if(self.password2_entry.get()=="" and self.user_name2_entry.get()==""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
                curs = connection.cursor()
                curs.execute("select * from bank_register where password=%s and user_name = %s", (self.password2_entry.get(),self.user_name2_entry.get()))
                row=curs.fetchone()
                id=row[0]
                print("bank_register_id",id)
                print(row)
                curs.execute("select * from banking_account where user_id=%s ", id)

                try:
                    connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
                    curs = connection.cursor()
                    curs.execute("select * from banking_account where user_id=%s ", id)
                    row=curs.fetchone()
                    print(row)
                    
                    if row==None:
                        self.frame_1=Frame(self.window,bg=self.color_6)
                        self.frame_1.place(x=0,y=0,width=1000,height=700)

                        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Bank_Account,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
                        
                        self.frame_2 = Frame(self.window, bg = self.color_6)
                        self.frame_2.place(x=0,y=100,width=1000, height=600)
                        self.ClearScreen()

                        self.create = Label(self.frame_2, text="CREATE ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=400,y=50)

                        self.sbi = Label(self.frame_2, text="SBI ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=150)
                        self.sbi_bt_1 = Button(self.frame_2, text='SBI', font=(self.font_1, 12), bd=2,command=self.CreateAccountsbi, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=600,y=150,width=100)
                    
                        self.cnr = Label(self.frame_2, text="CNR ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=250)
                        self.cnr_bt_1 = Button(self.frame_2, text='CNR', font=(self.font_1, 12), bd=2,command=self.CreateAccountcnr, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=600,y=250,width=100)

                        self.icic = Label(self.frame_2, text="ICIC ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=350)
                        self.icic_bt_1 = Button(self.frame_2, text='ICIC', font=(self.font_1, 12), bd=2,command=self.CreateAccounticic, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=600,y=350,width=100)

                        self.kvb = Label(self.frame_2, text="KVB ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=450)
                        self.kvb_bt_1 = Button(self.frame_2, text='KVB', font=(self.font_1, 12), bd=2,command=self.CreateAccountkvb, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=600,y=450,width=100)
                    else:
                        self.frame_1=Frame(self.window,bg=self.color_6)
                        self.frame_1.place(x=0,y=0,width=1000,height=700)

                        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Bank_Account,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
                        
                        self.frame_2 = Frame(self.window, bg = self.color_6)
                        self.frame_2.place(x=0,y=100,width=1000, height=600)
                        self.ClearScreen()

                        self.bankservices = Label(self.frame_2, text="BANK SERVICES", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=400,y=25)

                        self.deposit_bt_1 = Button(self.frame_2, text='DEPOSIT', font=(self.font_1, 12), bd=2,command=self.Depositbutton, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=450,y=150,width=100)

                        self.withdraw_bt_1 = Button(self.frame_2, text='WITHDRAW', font=(self.font_1, 12), bd=2,command=self.Withdrawbutton, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=450,y=250,width=100)

                        self.savings_bt_1 = Button(self.frame_2, text='SAVINGS', font=(self.font_1, 12), bd=2,command=self.Savingsbutton, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=450,y=350,width=100)

                        self.history_bt_1 = Button(self.frame_2, text='HISTORY', font=(self.font_1, 12), bd=2,command=self.Historybutton, cursor="hand2",
                        bg=self.color_5,fg=self.color_3).place(x=450,y=450,width=100)
                        
                        connection.commit()
                        connection.close()
                except Exception as e:
                    pass
            except Exception as e:
                messagebox.showerror("Error!","User name & Password doesn't register.",parent=self.window)
                
    def CreateAccountsbi(self):
        user_name2=self.user_name2_entry.get()
        password2=self.password2_entry.get()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        sbi=curs.execute("select id from bank_register where user_name=%s and password=%s ",(user_name2,password2))
        row=curs.fetchone()
        print("banking_account_userid",row)

        four_digit_num =str(random.randint(1000, 9999))
        code="SBI"
        account_number=code+four_digit_num
        print(account_number)
        
        user_id=row[0]
        print("user_id",user_id)
        curs.execute("insert into banking_account (account_no,user_id,bank_name,bank_balance)values(%s,%s,%s,%s)",
                                        (account_number,user_id,'SBI',0,))
        connection.commit()
        connection.close()
        messagebox.showinfo('Done!', "Welcome, SBI account created successful")
    def CreateAccountcnr(self):
        user_name2=self.user_name2_entry.get()
        password2=self.password2_entry.get()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        sbi=curs.execute("select id from bank_register where user_name=%s and password=%s ",(user_name2,password2))
        row=curs.fetchone()
        print(row)

        four_digit_num =str(random.randint(1000, 9999))
        code="CNR"
        account_number=code+four_digit_num
        print(account_number)

        user_id=row[0]
        print("user_id",user_id)
        curs.execute("insert into banking_account (account_no,user_id,bank_name,bank_balance)values(%s,%s,%s,%s)",
                                        (account_number,user_id,'CNR',0,))
        connection.commit()
        connection.close()
        messagebox.showinfo('Done!', "Welcome, CNR account created successful")
        
    def CreateAccounticic(self):
        user_name2=self.user_name2_entry.get()
        password2=self.password2_entry.get()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        sbi=curs.execute("select id from bank_register where user_name=%s and password=%s ",(user_name2,password2))
        row=curs.fetchone()
        print(row)

        four_digit_num =str(random.randint(1000, 9999))
        code="ICIC"
        account_number=code+four_digit_num
        print(account_number)
        
        user_id=row[0]
        print("user_id",user_id)
        curs.execute("insert into banking_account (account_no,user_id,bank_name,bank_balance)values(%s,%s,%s,%s)",
                                        (account_number,user_id,'ICIC',0,))
        connection.commit()
        connection.close()
        messagebox.showinfo('Done!', "Welcome, ICIC account created successful")
        
    def CreateAccountkvb(self):
        user_name2=self.user_name2_entry.get()
        password2=self.password2_entry.get()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        sbi=curs.execute("select id from bank_register where user_name=%s and password=%s ",(user_name2,password2))
        row=curs.fetchone()
        print(row)

        four_digit_num =str(random.randint(1000, 9999))
        code="KVB"
        account_number=code+four_digit_num
        print(account_number)
        
        user_id=row[0]
        print("user_id",user_id)
        curs.execute("insert into banking_account (account_no,user_id,bank_name,bank_balance)values(%s,%s,%s,%s)",
                                        (account_number,user_id,'KVB',0,))
        connection.commit()
        connection.close()
        messagebox.showinfo('Done!', "Welcome, KVB account created successful")
        
####
    def Depositbutton(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.CheckBankAccount,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2 = Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()

        self.deposit = Label(self.frame_2, text="DEPOSIT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=450,y=50)
        self.deposit = Label(self.frame_2, text="DEPOSIT AMOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=200,y=200)
        self.deposit_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.deposit_entry.place(x=500,y=200, width=300,height=30)
        self.deposit_bt_1 = Button(self.frame_2, text='DEPOSIT', font=(self.font_1, 12), bd=2,command=self.Deposit, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=700,y=350,width=100)
        self.clear_bt_1 = Button(self.frame_2, text='CLEAR', font=(self.font_1, 12), bd=2,command=self.Deposit, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=200,y=350,width=100)
        
    def Withdrawbutton(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.CheckBankAccount,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2= Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()

        self.withdraw = Label(self.frame_2, text="WITHDRAW", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=450,y=50)
        
        self.withdraw = Label(self.frame_2, text="WITHDRAW AMOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=175,y=200)
        self.withdraw_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.withdraw_entry.place(x=525,y=200, width=300,height=30)
        self.withdraw_bt_1 = Button(self.frame_2, text='WITHDRAW', font=(self.font_1, 12), bd=2,command=self.Withdraw, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=725,y=350,width=100)
        self.clear_bt_1 = Button(self.frame_2, text='CLEAR', font=(self.font_1, 12), bd=2,command=self.Withdraw, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=175,y=350,width=100)
        
    def Savingsbutton(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.CheckBankAccount,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2= Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()

        self.Savings = Label(self.frame_2, text="SAVINGS", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=450,y=50)    
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        curs.execute("select * from bank_register where password=%s and user_name = %s", (self.password2_entry.get(),self.user_name2_entry.get()))
        row=curs.fetchone()
        id=row[0]
        print(row[0])
        
        curs.execute("select bank_balance from banking_account where user_id=%s",id )
        row=curs.fetchone()
        print(row,"SAVINGS")
        self.Savings = Label(self.frame_2, text="SAVINGS AMOUNT :", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=250)
        self.SavingsAmount = Label(self.frame_2, text=row, font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=625,y=250)


    def Historybutton(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.CheckBankAccount,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        user_name2=self.user_name2_entry.get()
        password2=self.password2_entry.get()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        sbi=curs.execute("select id from bank_register where user_name=%s and password=%s ",(user_name2,password2))
        row=curs.fetchone()
        id=row[0]
        print(id)
        
        # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",password="Mohan2002@",database="BANK")
        mycursor = mydb.cursor()
        curs = connection.cursor()
        curs.execute("select * from banking_transactions where user_id = %s",id)
        print("id",id)
        rowcount=curs.fetchall()
        for row in rowcount:
            print(row)
        root = Tk()
        root.title("History Table")
        tree = ttk.Treeview(root,height=2)
        tree["columns"] = ("id", "user_id", "banking_table_id","transaction_reason","date_field","amount","balance_amount")
        tree.column("#0", width=0, stretch=NO)
        tree.column("id", anchor=W, width=50)
        tree.column("user_id", anchor=W, width=50)
        tree.column("banking_table_id", anchor=W, width=100)
        tree.column("transaction_reason", anchor=W, width=200)
        tree.column("date_field", anchor=W, width=200)
        tree.column("amount", anchor=W, width=200)
        tree.column("balance_amount", anchor=W, width=200)
        tree.heading("#0", text="", anchor=W)
        tree.heading("id", text="ID", anchor=W)
        tree.heading("user_id", text="user_id", anchor=W)
        tree.heading("banking_table_id", text="banking_table_id", anchor=W)
        tree.heading("transaction_reason", text="transaction_reason", anchor=W)
        tree.heading("date_field", text="date_field", anchor=W)
        tree.heading("amount", text="amount", anchor=W)
        tree.heading("balance_amount", text="balance_amount", anchor=W)
        for record in rowcount:
            tree.insert("", "end", values=record)
        def increase_height():
            tree.config(height=tree.cget("height") + 1)
        increase_button = ttk.Button(root, text="MORE", command=increase_height)
        increase_button.pack()
        tree.pack()
        root.mainloop()
        
    def Deposit(self):
        deposit=int(self.deposit_entry.get())
        print('deposit_amount:',deposit)
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        curs.execute("select * from bank_register where password=%s and user_name = %s", (self.password2_entry.get(),self.user_name2_entry.get()))
        row1=curs.fetchone()
        print(row1)
        print(1)

        id=row1[0]
        print(2)
        print("over",id)
        curs.execute("select * from banking_account where user_id=%s ", id)
        row2=curs.fetchone()
        print('user_account',row2)

        print(row1)
        wallet_balance=row1[6]
        print("wallet_balance:",wallet_balance)

        wallet=wallet_balance-deposit
        print("after_wallet",wallet)

        bank_balance=row2[4]
        print('bank_balance',bank_balance)
        total=bank_balance+deposit
        print("total_balance",total)

        curs.execute("update bank_register set wallet_balance=%s where id=%s",(wallet,id))
        curs.execute("update banking_account set bank_balance=%s where user_id=%s",(total,id))
        row=curs.fetchone()
        connection.commit()
        connection.close()
        messagebox.showinfo('Deposit Successfully!',"Your amount is credit successfully.")

        ###banking_transactions_table
        current_time=datetime.datetime.now()
        print(current_time)
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        curs.execute("select * from banking_account where user_id = %s",id)
        row1=curs.fetchone()
        history=row1[2]
        print("banking_transactions_table",history)
        curs.execute("insert into banking_transactions (user_id,transaction_reason,date_field,amount,balance_amount)values(%s,%s,%s,%s,%s)",
                     (id,"Credited",current_time,self.deposit_entry.get(),total))
        connection.commit()
        connection.close()
        
    def Withdraw(self):
        withdraw=int(self.withdraw_entry.get())
        print('withdraw_amount:',withdraw)
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        curs.execute("select * from bank_register where password=%s and user_name = %s", (self.password2_entry.get(),self.user_name2_entry.get()))
        row=curs.fetchone()

        id=row[0]
        curs.execute("select * from banking_account where user_id=%s ", id)
        row=curs.fetchone()
        print('user_account',row)
        
        
        bank_balance=row[4]
        print(bank_balance)
        total=bank_balance-withdraw
        print(total)

        curs.execute("update banking_account set bank_balance=%s where user_id=%s",(total,id))
        row=curs.fetchone()
        connection.commit()
        connection.close()
        messagebox.showinfo('Withdraw Successfully!',"Your amount is withdraw successfully.")

        ###banking_transactions_table
        current_time=datetime.datetime.now()
        connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
        curs = connection.cursor()
        curs.execute("select * from banking_account where user_id = %s",id)
        row1=curs.fetchone()
        savings=row1[2]
        print("banking_transactions_table",savings)
        curs.execute("insert into banking_transactions (user_id,transaction_reason,date_field,amount,balance_amount)values(%s,%s,%s,%s,%s)",
                     (id,"Withdraw",current_time,self.withdraw_entry.get(),total))
        connection.commit()
        connection.close()
        
    def Wallet_Balance(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Back_to_home,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2 = Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()
        
        self.name = Label(self.frame_2, text="WALLET ACCOUNT", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=400,y=100)
        
        self.user_name3 = Label(self.frame_2, text="USER NAME", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=200)
        self.user_name3_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.user_name3_entry.place(x=450,y=205, width=300)
 
        self.password3 = Label(self.frame_2, text="PASSWORD", font=(self.font_2, 15, "bold"), bg=self.color_6).place(x=250,y=300)
        self.password3_entry = Entry(self.frame_2, bg=self.color_4, fg=self.color_3)
        self.password3_entry.place(x=450,y=300, width=300)

        self.submit_bt_3 = Button(self.frame_2, text='Submit', font=(self.font_1, 12), bd=2,command=self.Wallet, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=250,y=450,width=100)

        self.clear_bt_3 = Button(self.frame_2, text='Cancel', font=(self.font_1, 12), bd=2,command=self.ClearScreen, cursor="hand2",
        bg=self.color_5,fg=self.color_3).place(x=400,y=450,width=100)

    def Wallet(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)

        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Wallet_Balance,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
        
        self.frame_2 = Frame(self.window, bg = self.color_6)
        self.frame_2.place(x=0,y=100,width=1000, height=600)
        self.ClearScreen()

        if(self.password3_entry.get()=="" and self.user_name3_entry.get()==""):
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host='localhost',user='root',password='Mohan2002@',database='BANK')
                curs = connection.cursor()
                curs.execute("select * from bank_register where password=%s and user_name = %s", (self.password3_entry.get(),self.user_name3_entry.get()))
                row=curs.fetchone()
                id=row[0]
                print("bank_register_id",id)
                wallet=row[6]
                print(wallet)
                curs.execute("select * from banking_account where user_id=%s ", id)
            except Exception as e:
                messagebox.showerror("Error!","User name & Password doesn't register.",parent=self.window)
        self.wallet = Label(self.frame_2, text="WALLET AMOUNT :", font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=300,y=250)
        self.walletAmount = Label(self.frame_2, text=wallet, font=(self.font_2, 20, "bold"), bg=self.color_6).place(x=625,y=250)

        
    def Exit(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)
        self.user_register=Button(self.frame_1,text="USER REGISTER",font=(self.font_1,12), bd=2, command=self.User_Register,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=100,width=300)
        self.user_register=Button(self.frame_1,text="BANK ACCOUNT",font=(self.font_1,12), bd=2, command=self.Bank_Account,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=300,width=300)
        self.user_register=Button(self.frame_1,text="WALLET BALANCE",font=(self.font_1,12), bd=2, command=self.Wallet_Balance,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=500,width=300)
        self.user_register=Button(self.frame_1,text="BACK",font=(self.font_1,12), bd=2, command=self.Back,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)

    '''Remove all widgets from the frame 1'''
    def ClearScreen(self):
        for widget in self.frame_2.winfo_children():
            widget.destroy()

    '''Exit window'''
    def Exit(self):
        self.window.destroy()




    def Back_to_home(self):
        self.frame_1=Frame(self.window,bg=self.color_6)
        self.frame_1.place(x=0,y=0,width=1000,height=700)
        
        self.user_register=Button(self.frame_1,text="USER REGISTER",font=(self.font_1,12), bd=2, command=self.User_Register,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=100,width=300)
        self.user_register=Button(self.frame_1,text="BANK ACCOUNT",font=(self.font_1,12), bd=2, command=self.Bank_Account,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=300,width=300)
        self.user_register=Button(self.frame_1,text="WALLET BALANCE",font=(self.font_1,12), bd=2, command=self.Wallet_Balance,
                                  bg=self.color_5,fg=self.color_3).place(x=350,y=500,width=300)
        self.user_register=Button(self.frame_1,text="EXIT",font=(self.font_1,12), bd=2, command=self.Exit,
                                  bg=self.color_1,fg=self.color_3).place(x=850,y=30,width=100)
      
        
    

        

#THE MAIN FUNCTION:
if __name__=="__main__":
    root=Tk()
    obj=Bank_management(root)
    root.mainloop
            
