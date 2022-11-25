import math
import mysql.connector as conct

username = ""
password = ""

mysql = conct(host="localhost", passwrd=password, database="root", user=username)

# admin functions
def removebc():
    bc = int(input('Enter Book Code: '))
    # Change table name and attribute name accordingly#
    d = 'delete from library where INBI=%S;'
    data = (bc)
    cursor = mysql.cursor()  # Change the object name accordingly#
    cursor.execute(d, data)
    cursor.commit
    print('----------------------- BOOK REMOVED SUCCESSFULLY ------------------------------')


def add():
    bn = input("Enter Book Name: ")
    bc = int(input("Enter Book INBI number: "))
    an = input("Enter Author's Name: ")
    rp = int(input("Enter Rental Price: "))
    # ("Name", "INBI number", "Author", "Rent Price", "Available Stock")
    t = int(input("Enter Total Number Of Books: "))
    
    data = (bn, bc, an, rp, t)

    insert = 'insert into library values (%S,%S,%S,%S,%S);'
    cursor = mysql.cursor()  # Change the object name accordingly#
    cursor.execute(insert, data)
    mysql.commit
    print('------------------------- BOOK ADDED SUCCESSFULLY ------------------------------')


def updt():
    bn = input("Enter Book name: ")
    np = int(input("Enter Revised Price: "))
    # Change table name and attribute name accordingly#
    q = 'update library set RPrice=%S where BookName=%S;'
    data = (np, bn)
    cursor = mysql.cursor()  # Change the object name accordingly#
    cursor.execute(q, data)
    cursor.commit
    print("----------------------- PRICE UPDATED SUCCESSFULLY -----------------------------")


def mainadmn():
    while True:
        print("\n================================================================================")
        print("======================= L I B R A R Y M A N A G E R ============================")
        print("=============================== A D M I N ======================================")

        print("1. Show Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Availability")
        print("5. Update Rental Price")
        print("6. Return")

        T = int(input('Enter Task Number: '))
        if T == 1:
            DisplayList()
        elif T == 2:
            add()
        elif T == 3:
            removebc()
        elif T == 4:
            avai()
        elif T == 5:
            updt()
        elif T == 6:
            main()  # Assuming main is the menu where you can choose between admin login and customer login#
        else:
            print("\n-ERROR-")


# user functions
def userAdmn():
    while True:

        print("\n================================================================================")
        print("============================= W E L C O M E ====================================")
        print("=============================== U S E R ========================================")
        print("1. Show Books")
        print("2. Check Availability of a Book")
        print("3. Rent book")
        print("4. Return")
        T = int(input('Enter Task Number: '))
        if T == 1:
            DisplayList()
        elif T == 2:
            avai()
        elif T == 3:
            rent()
        elif T == 4:
            main()  # Assuming main is the menu where you can choose between admin login and customer login#
        else:
            print("\n-ERROR-")


def rent():
    bn = input("Enter Book name: ")
    cursor = mysql.cursor()  # Change the object name accordingly#

    q = 'from library select Total where BookName=%S'
    cursor.execute(q, bn)
    t = int(cursor.fetchone())

    if t > 1:
        q = 'from library select RPrice where BookName=%S'
        cursor.execute(q, bn)
        r = int(cursor.fetchone())

        print("The rental price for three weeks of ", bn, "is Rs", r)
        print("1. Rent book\n2. Cancel")
        T = input("Enter Task number: ")

        if T == 1:
            q = 'update library set Total=%S where BookName=%S;'
            data = (t-1, bn)
            cursor.execute(q, data)
            print(
                "---------------- You're book will be delivered to you're address ---------------")
            print(
                "----------- Please return in 3 weeks or the penalty is Rs.30 per day -----------")
        else:
            print(
                "------------------------------- cancelled --------------------------------------")
    else:
        print("-------------------------------- Book not available ----------------------------")


# common functions
def avai():
    bn = input("Enter book name")
    s = 'select Total from library where BookName=%S;'
    cursor = mysql.cursor()  # Change the object name accordingly#
    cursor.execute(s, bn)
    cursor.commit
    data = cursor.fetchall()
    print("Number of available book is: ",data)
    input('\n-PRESS ENTER TO CONTINUE-')


def DisplayList():

    head = ("Name", "INBI number", "Author", "Rent Price", "Available Stock")
    s = 'select * from library;'
    cursor = mysql.cursor()
    cursor.execute(s)
    r = cursor.fetchall()
    queryValue = (r)  # the table query should be stored in this
    w = []
    heading = list(head)
    queryRes = []

    for i in range(0, len(queryValue)):
        queryRes.append(list(queryValue[i]))

    if(len(queryRes) == 0):
        print("-Error-")
        return

    # To get total row width
    for i in range(0, len(heading)):
        lst = [heading[i], str(queryRes[0][i]), str(
            queryRes[1][i]), str(queryRes[2][i])]
        w.append(len(max(lst, key=len)))

    # to Print top line
    print("+", end="")
    for i in range(sum(w)+(3*len(heading)-1)-1):
        print("-", end="")
    print("-+")

    # test heading print
    print("", end="| ")
    for i in range(len(heading)):
        startLoc = math.ceil(w[i]/2) - math.floor(len(str(heading[i]))/2) - 1
        if startLoc < 0:
            startLoc = 0
        for j in range(w[i]-len(heading[i])+1):
            if(j == startLoc):
                print(heading[i], end=" ")
            else:
                print(end=" ")
        print("| ", end="")
    print()

    # to print heading and other row seperator line
    print("", end="+-")
    for i in range(0, len(heading)):
        for j in range(w[i]):
            print("-", end="")
        if (i != len(heading)-1):
            print(end="-+-")
        else:
            print(end="-+")
    print()

    # to print other row
    for l in range(len(queryRes)):
        row = queryRes[l]
        print("", end="| ")
        for i in range(len(row)):

            startLoc = math.ceil(w[i]/2) - math.floor(len(str(row[i]))/2) - 1
            if startLoc < 0:
                startLoc = 0
            for j in range(w[i]-len(str(row[i])) + 1):
                if(j == startLoc):
                    print(str(row[i]), end=" ")
                else:
                    print(end=" ")
            print("| ", end="")
        print()

    # to Print bottom line
    print("+", end="")
    for i in range(sum(w)+(3*len(heading)-1)-1):
        print("-", end="")
    print("-+")


def signup():
    u = input("\nEnter username: ")
    p = input("Enter password: ")

    if (u == username and p == password):
        mainadmn()
    else:
        print("\n-Incorrect username or password-")


#main function
def main():
    while True:

        print("\n================================================================================")
        print("                    W E L C O M E  T O  L I B R A R Y       ")
        print("1. Login as admin")
        print("2. Login as user")
        T = int(input('Enter Task Number: '))
        if T == 1:
            signup()
        elif T == 2:
            userAdmn()
        else:
            print("\n-ERROR-")

main() #calling main function
