import time as t

print("Welcome")
name = input("What is your name\n")

if name == "Ben":
    isevil = input("Are you evil?\n")
    if isevil == "Yes":
        print("You are not welcome here!! Get out You Evil Ben!!!")
        exit("Drink coffee somewhere else and learn some things in Python")
else:    
    print("Welcome " + name)

menu = "Espresso, Latte, Black Coffee, Milk, Orange Juice"
print(menu)
print("Choose your order\n")
order = input().lower()

if order == "orange juice":
            print("PATHETIC!!!\n")
            exit("GET LOST")
elif order == "milk":
            print("TRULY GODLIKE CHOICE!")


while True:
    try:
        
        print("How many\n")
        quantity = int(input())
        price = 8
        total = quantity * price
        break

    except ValueError:
        print(f"WHAT AN IDIOT! Enter a valid number.")

print("So " + name + ", you ordered " + str(quantity) + " " + order + " and your total is $" + str(total))

# Additional script asking for donation
print("And would you like to donate for the local programmers club?\n")
isgood = input()

if isgood == "Yes":
    print("How many $?\n")
    donate = input()
    print("So is it sure that you want to donate $" + donate + "?")
    print("Yes or No\n")
    yn = input()

    if yn.lower() == "no":
        print("No problems, Have a good day")
        exit()
    elif yn.lower() == "yes":
        print("So would you like to pay with UPI or Give Cash/Cheque ?\n")
        caup = input()

        if caup.lower() == "cash":
            print("Ok then give cash $")
        elif caup.lower() == "cheque":
            print("YOU HAVE SO MUCH MONEY!!!")
            t.sleep(5)
            print("Anyway ")
            print("Here are the cheque details:\n")
            payto = print("Payee: Envixy Coffee Shop")
            subto = int(donate) + total
            ammount = print("Amount: $" + str(subto))
            amountWords = input("Amount In Words: ")
            date = input("Date: ")
            print("So we will deposit this cheque, and the amount shall be deducted soon.")
            print("Please just check if the details on the cheque are correct.")
            print("Payee: Envixy Coffee Shop")
            print("Amount: $" + str(subto))
            print("Amount In Words: " + amountWords)
            correct = input("Are the details correct?\n")

            if correct.lower() == "yes":
                print("The cheque will be deposited soon, and the amount shall be deducted soon.")
                exit()
            else:
                print("IDIOT SO WHY DON'T YOU FILL IN THE CORRECT DETAILS IN THE FIRST TIME")
                exit("NEVER RETURN IN THIS CAFÈ EVER AGAIN")
        else:
            print("Enter your account Info.")

        bank = input("Enter your bank\n")
        branch = input("Enter your bank branch\n")
        acno = input("Enter your A/C number\n")
        sure = input("Are you sure??\n")

        if sure.lower() == "yes":
            print("So we will charge $" + donate + " from A/C No." + acno + " of " + bank + " " + branch + " Branch")
        else:
            print("We didn't save your Bank Account Info.")  
            exit()  

        print("We respect your bank A/C privacy so we didn't save your A/C info")
        print("Your account has been charged for $" + donate)
else:
    print("No problems!!!!")
    print("The price for you has been increased by 100 times you evil person\nNow the price for you is $" + str(price * 100))
    print("Now pay the cost $" + str(price * 100))
    print("You don't have an option")
    print("YOU CAN'T ESCAPE!!!!")
    exit("PAISE NAHI HAI TO BARTAN DHO")
# This script works better than I ever expected !!!!!!!