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
menu = "Esprsso, Latte, Black Coffee, Milk, Orange Juice"
print(menu)
order = input("Choose your order\n")
if order == "orange juice\n":
    print("PATHETIC!!!\n")
    exit("GET LOST")
elif order == "milk":
    print("TRULY GODLIKE CHOICE!")   
print("How many\n")
quantity = input()
price = 8
total = int(quantity) * price
print("So " + name + ", you ordered " + quantity + " " + order + " and your total is $" + str(total))
#---'-----------------'-----------------'------------------------------------------------------'------
#Main script was till here 
#Additional script asking for donation
print("And would you like to donate for the local programmers club?\n")
isgood = input()
if isgood == "Yes":
    print("How many $?\n")
    donate = input()
    print("So is it sure that you want to donate $" + donate + "?")
    print("Yes or No\n")
    yn = input()
    if yn == "no":
        print("No problems, Have a good day")
        exit()
    elif yn == "Yes" or yn == "yes":
        print("So would you like to pay with UPI or Give Cash/Cheque ?\n")
        caup = input()
        if caup == "Cash" or caup == "cash":
            print("Ok then give cash $")
        elif caup == "Cheque" or caup == "cheque":
            print("YOU HAVE SO MUCH MONEY!!!")
            t.sleep(5)
            print("Anyway ")
            print("Here are the cheque details:\n")
            payto = print("Payee: Envixy Coffee Shop")
            subto = int(donate) + total
            ammount = print("Amount: $" + str(subto))
            amountWords = input("Amount In Words: ")
            date = input("Date: ")
            print("So we will deposit this cheque and the ammount shall be deducted soon.")
            print("Please just check if the details on the cheque are correct.")
            print("Payee: Envixy Coffee Shop")
            print("Ammount: $" + str(subto))
            print("Ammount In Words: " + amountWords)
            correct = input("Are the deatils correct?\n")
            if correct == "Yes" or correct == "yes":
                print("The cheque will be deposited soon and the ammount shall be deducted soon.")
                exit()
            else:
                print("IDIOT SO WHY DON'T YOU FILL IN THE CORRECT DETAILS IN THE FIRET TIME")
                exit("NEVER RETURN IN THIS CAFÈ EVER AGAIN")
        else:
            print("Enter your account Info.")
        bank = input("Enter your bank\n")
        branch = input("Enter your bank branch\n")
        acno = input("Enter your A/C number\n")
        sure = input("Are you sure??\n")
        if sure == "yes":
            print("So we will charge $" + donate + " from A/C No." + acno + " of " + bank + " " + branch + " Branch")
        else:
            print("We didn't save your Bank Account Info.")  
            exit()  
        print("We respect your bank A/C privacy so we didn't save your A/C info")
        print("Your account has been charged for $" + donate)
        
else:
     print("No problems!!!!")
     print("The price for you has been increased by 100 times you evil person\nNow the price for you is $" + str(price * 100))
     print("Now pay the cost $" + str(price) *100)
     print("You dont have an option")
     print("YOU CAN'T ESCAPE!!!!")
     exit("PAISE NAHI HAI TO BARTAN DHO")
#This script works better than I ever expected !!!!!!!     