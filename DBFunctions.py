import sqlite3

def createProfile(first_name, last_name, savings_goal, current_savings):
    #Inital setup for database connection
    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()

    # Create table for user profile
    cur.execute('''CREATE TABLE profile(
                first_name TEXT NOT NULL,
                last_name TEXT,
                savings_goal REAL,
                current_savings REAL
                )''')
    
    cur.execute("""INSERT INTO profile(first_name,last_name,savings_goal,current_savings) VALUES (?,?,?,?)""", (first_name, last_name, savings_goal, current_savings))
    con.commit()
    cur.execute("SELECT * FROM profile")

    #Create table for user bills
    cur.execute('''CREATE TABLE bills(
                name TEXT NOT NULL UNIQUE,
                amount REAL NOT NULL
                )''')




    # Close database connection
    con.close() # Close database conneciton
    print('Database disconnected.')

def getProfileInfo():
    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()

    cur.execute("SELECT * FROM profile")
    res = cur.fetchone()
    return res
    con.close() # Close database conneciton
    print('Database disconnected.')

def addBill():
    choice = False

    # Get input for Bill name and amount and make sure it is correct

    while choice == False:
        name = input("What bill would you like to add?: ")
        amount = input("What is the amount for the bill?: ")

        print(f"Bill name: {name}  Bill amount: {amount}")
        YorN = input("Is this correct? (Y / N): ")
        print(YorN)
        if YorN == "Y":
            choice = True
            print(choice)
        elif YorN == "N":
            choice = False
        else:
            print("Invalid entry. Please input bill name and amount in again and respond with ""Y"" or ""N""")

    # Add it to SQL database

    # Connect to database
    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()

    cur.execute("""INSERT INTO bills(name, amount) VALUES (?,?)""", (name, amount))
    con.commit()
    print("Bill added")

    # End database connection
    con.close() # Close database conneciton
    print('Database disconnected.')

def viewBills():
    con = sqlite3.connect("database.db")

    cur = con.cursor()

    res =  cur.execute("SELECT * FROM bills").fetchall()

    for i in res:
        print(i)
    

    con.close() # Close database conneciton

def removeBill():
    name = input("What is the name of the bill you would like to delete?")

    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()


    cur.execute("DELETE FROM bills WHERE name = ?", (name,))
    con.commit()
    print("Bill removed")
    con.close() # Close database conneciton
    print('Database disconnected.')


def addToSavings():
    add = float(input("How much money would you like to add to your savings?"))
    add = round(add,2)

    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()

    res = cur.execute("SELECT current_savings FROM profile").fetchone()

    new_savings = add + res[0]

    cur.execute("UPDATE profile SET current_savings = ?", (new_savings,))
    con.commit()
    res = cur.execute("SELECT current_savings FROM profile").fetchone()

    print(f"{res[0]} is your new savings total.")

    con.close() # Close database conneciton
    print('Database disconnected.')


def removeFromSavings():
    rem = float(input("How much money would you like to remove from your savings?"))
    rem = round(rem,2)

    con = sqlite3.connect("database.db")
    print('Database connected.')
    cur = con.cursor()

    res = cur.execute("SELECT current_savings FROM profile").fetchone()

    new_savings = res[0] - rem

    cur.execute("UPDATE profile SET current_savings = ?", (new_savings,))
    con.commit()
    res = cur.execute("SELECT current_savings FROM profile").fetchone()

    print(f"{res[0]} is your new savings total.")

    con.close() # Close database conneciton
    print('Database disconnected.')




# For database testing
# con = sqlite3.connect("database.db")
# print('Database connected.')
# cur = con.cursor()


# con.close() # Close database conneciton
# print('Database disconnected.')
