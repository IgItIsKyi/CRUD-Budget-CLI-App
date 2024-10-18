import os
import time
from DBFunctions import *

if os.path.isfile("database.db") == False:
    print("Thank you for testing my application! This is going to be a profile build moment.")
    print("This information is only stored on your computer and I will not be able to see it.")
    fname = input("What is your first name?: ")
    lname = input("What is your last name? (This is optional): ")
    save_goal = float(input("What is your savings goal?: "))
    save_goal = round(save_goal, 2)
    print(f'Save goal: {save_goal}')
    savings = float(input("What is your savings total?: "))
    savings = round(savings, 2)
    print(f'Current savings: {savings}')


    createProfile(fname, lname, save_goal, savings)


pf_info = getProfileInfo()
fname = pf_info[0]
lname = pf_info[1]
save_goal = pf_info[2]
savings = pf_info[3]


print(f"Welcome back {fname}!")
if savings >= save_goal:
    print("You have surpassed your savings goal!")
    print(f"Your current savings amount is ${savings}")

else:
    print(f"You are ${save_goal - savings} away from reaching your savings goal!")
    print(f"Your current savings amount is ${savings}")


time.sleep(3)
os.system('clear')

def menu():
    mm_option = -1

    # Menu Options
    while mm_option != 0:
        print('0. Exit')
        print('1. View all bills')
        print('2. Add Bill')
        print('3. Remove Bill')
        print('4. Add to Savings')
        print('5. Remove from Savings')
        mm_option = int(input('Pick an option: '))

        # Menu Option Controls
        if mm_option == 0:
            print('Exiting application...')
        elif mm_option == 1:
            print("ID  | Name  | Amount")
            viewBills()
        elif mm_option == 2:
            addBill()
        elif mm_option == 3:
            removeBill()
        elif mm_option == 4:
            addToSavings()
        elif mm_option == 5:
            removeFromSavings()
        else:
            print('Input was not an option. Try again or enter 0 to exit.')
        
        time.sleep(3)
        os.system('clear')


menu()