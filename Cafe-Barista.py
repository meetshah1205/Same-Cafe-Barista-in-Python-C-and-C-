import time as t

# Welcome message
print("Welcome")

# Get user's name
name = input("What is your name\n")

# Check if the user is an "Evil Ben"
if name == "Ben":
    isevil = input("Are you evil?\n")
    if isevil.lower() == "yes":
        print("You are not welcome here!! Get out You Evil Ben!!!")
        exit("Drink coffee somewhere else and learn some things in Python")
else:
    print("Welcome " + name)

# Display menu
menu = "Espresso, Latte, Black Coffee, Milk, Orange Juice"
print(menu)
print("Choose your order\n")

# Get user's order
order = input().lower()

# Process special cases for certain orders
if order == "orange juice":
    print("PATHETIC!!!\n")
    exit("GET LOST")
elif order == "milk":
    print("TRULY GODLIKE CHOICE!")

# Get quantity of the order
while True:
    try:
        print("How many\n")
        quantity = int(input())
        price = 8
        total = quantity * price
        break
    except ValueError:
        print(f"WHAT AN IDIOT! Enter a valid number.")

# Display order details
print(f"So {name}, you ordered {quantity} {order} and your total is ${total}")

# Ask for donation
print("And would you like to donate for the local programmers club?\n")
isgood = input()

# Process donation if user agrees
if isgood.lower() == "yes":
    print("How many $?\n")
    donate = input()
    print(f"So, is it sure that you want to donate ${donate}?")
    print("Yes or No\n")
    yn = input().lower()

    if yn == "no":
        print("No problems, Have a good day")
        exit()
    elif yn == "yes":
        print("So would you like to pay with UPI or Give Cash/Cheque ?\n")
        caup = input().lower()

        if caup == "cash":
            print(f"Ok then give cash ${donate}")
        elif caup == "cheque":
            print("YOU HAVE SO MUCH MONEY!!!")
            t.sleep(5)
            print("Anyway ")
            print("Here are the cheque details:\n")
            print("Payee: Envixy Coffee Shop")
            subto = int(donate) + total
            print(f"Amount: ${subto}")
            amountWords = input("Amount In Words: ")
            date = input("Date: ")
            print("So we will deposit this cheque, and the amount shall be deducted soon.")
            print("Please just check if the details on the cheque are correct.")
            print("Payee: Envixy Coffee Shop")
            print(f"Amount: ${subto}")
            print(f"Amount In Words: {amountWords}")
            correct = input("Are the details correct?\n").lower()

            if correct == "yes":
                print("The cheque will be deposited soon, and the amount shall be deducted soon.")
                exit()
            else:
                print("IDIOT SO WHY DON'T YOU FILL IN THE CORRECT DETAILS IN THE FIRST TIME")
                exit("NEVER RETURN IN THIS CAFÃ EVER AGAIN")
        else:
            print("Enter your account Info.")

            # Get bank details
            bank = input("Enter your bank\n")
            branch = input("Enter your bank branch\n")
            acno = input("Enter your A/C number\n")
            sure = input("Are you sure??\n").lower()

            if sure == "yes":
                print(f"So we will charge ${donate} from A/C No.{acno} of {bank} {branch} Branch")
            else:
                print("We didn't save your Bank Account Info.")
                exit()

            print("We respect your bank A/C privacy so we didn't save your A/C info")
            print(f"Your account has been charged for ${donate}")
else:
    # Adjust price for "Evil Ben"
    print("No problems!!!!")
    print(f"The price for you has been increased by 100 times you evil person\nNow the price for you is ${price * 100}")
    print(f"Now pay the cost ${price * 100}")
    print("You don't have an option")
    print("YOU CAN'T ESCAPE!!!!")
    exit("PAISE NAHI HAI TO BARTAN DHO")

# This script works better than I ever expected !!!!!!!