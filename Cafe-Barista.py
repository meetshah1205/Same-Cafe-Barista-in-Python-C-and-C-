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
if order == "orange juice":
    print("PATHETIC!!!")
    exit("GO, GET LOST")
elif order == "Milk":
    print("TRULY GODLIKE CHOICE!")    
print("How many\n")
quantity = input()
price = 8
total = int(quantity) * price
print("So " + name + ", you ordered " + quantity + " " + order + " and your total is $" + str(total))
print("And would you like to donate for the local programmers club?\n")
isgood = input()
if isgood == "Yes":
    print("How many $?\n")
    donate = input()
    print("So is it sure that you want to donate $" + donate + "?")
    print("Yes or No\n")
    yn = input()
    if yn == "No":
        print("No problems, Have a good day")
        exit()
    else:
         print("Your account has been charged for $" + donate)
        
else:
     print("No problems😥😢😭")
     print("The price for you has been increased by 100 times you evil person\nNow the price for you is $" + str(price * 100))
     exit()