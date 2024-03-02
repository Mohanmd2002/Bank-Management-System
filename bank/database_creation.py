import pymysql
a=pymysql.connect(
    host="localhost",
    user="root",
    password="Mohan2002@",
    database="BANK"
    )
##mycursor=a.cursor()
##mycursor.execute("CREATE DATABASE BANK")

mycursor=a.cursor()
mycursor.execute("CREATE TABLE bank_register(id int auto_increment,f_name VARCHAR(50),l_name VARCHAR(50),contact VARCHAR(50),password VARCHAR(50),user_name VARCHAR(50))")

##mycursor=a.cursor()
##mycursor.execute("CREATE TABLE bank_acc_details (user_name varchar(50),bank_name varchar(50),contact varchar(50))")

























##mycursor=a.cursor()
##mycursor.execute("INSERT INTO bank_register (f_name,l_name,contact,password,user_name) values('mohan','k',9360,'mohan','mk')")
##a.commit()
##print(mycursor.rowcount,"data insert")
