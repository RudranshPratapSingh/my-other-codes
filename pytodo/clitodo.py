import dbhelper
import os

os.system("clear")

ch = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))

while ch != 4:
    if(ch == 1):
        os.system("cls")
        print("ID" + "\t" + "TASK\n\n")
        for rows in dbhelper.show():
            print(str(rows[0]) + "\t" + rows[1])
        ch = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
    elif(ch == 2):
        task = input("Enter A Task : ")
        if(len(task) != 0):
            dbhelper.insertdata(task)
        ch = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
    elif(ch == 3):
        os.system("cls")
        print("ID" + "\t" + "TASK\n\n")
        for rows in dbhelper.show():
            print(str(rows[0]) + "\t" + rows[1])
        id = int(input("Choose A Task ID To Delete : "))
        dbhelper.deletebyid(id)
        ch = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
    else:
        print("Choose A Correct Option")
        ch = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
else:
    print("Thank You For Using The Application ♥")