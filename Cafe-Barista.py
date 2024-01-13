import time as t

def welcome_user():
    """
    Welcomes the user and checks if the user is 'Evil Ben'.
    """
    print("Welcome")
    name = input("What is your name?\n").lower()

    if name.lower() == "ben":
        is_evil = input("Are you evil?\n").lower()
        if is_evil == "yes":
            print("You are not welcome here!! Get out You Evil Ben!!!")
            exit("Drink coffee somewhere else and learn some things in Python")
    else:
        print(f"Welcome {name}")

    return name

def display_menu():
    """
    Displays the coffee menu.
    """
    menu = ["Espresso", "Latte", "Black Coffee", "Milk", "Orange Juice"]
    print(", ".join(menu))
    return menu

def process_order(menu):
    """
    Processes the user's coffee order, handles special cases, and calculates the total.
    """
    order = input("Choose your order\n").lower()

    if order == "orange juice":
        print("PATHETIC!!!\n")
        exit("GET LOST")
    elif order == "milk":
        print("TRULY GODLIKE CHOICE!")

    while True:
        try:
            quantity = int(input("How many?\n"))
            price = 8
            total = quantity * price
            break
        except ValueError:
            print("WHAT AN IDIOT! Enter a valid number.")

    print(f"So {name}, you ordered {quantity} {order} and your total is ${total}")
    return quantity, total

def ask_for_donation():
    """
    Asks the user if they would like to donate and handles the donation process.
    """
    is_good = input("And would you like to donate for the local programmers club?\n").lower()

    if is_good == "yes":
        donate_amount = input("How much would you like to donate?\n")
        confirm_donation(donate_amount)
    else:
        print("No problems!!!!")

def confirm_donation(donate_amount):
    """
    Confirms the user's donation and processes the donation based on the chosen payment method.
    """
    print(f"So, are you sure you want to donate ${donate_amount}?")
    confirmation = input("Yes or No\n").lower()

    if confirmation == "yes":
        payment_method = input("Would you like to pay with UPI, Cash, or Cheque?\n").lower()

        if payment_method == "cash":
            print(f"Ok then, give cash ${donate_amount}")
        elif payment_method == "cheque":
            process_cheque(donate_amount)
        else:
            process_online_payment(donate_amount)
    else:
        print("No problems, Have a good day")
        exit()

def process_cheque(donate_amount):
    """
    Processes cheque payment, displays cheque details, and confirms details with the user.
    """
    print("YOU HAVE SO MUCH MONEY!!!")
    t.sleep(5)
    print("Anyway ")
    print("Here are the cheque details:\n")
    print("Payee: Envixy Coffee Shop")
    total_amount = int(donate_amount) + total
    print(f"Amount: ${total_amount}")
    amount_words = input("Amount In Words: ")
    date = input("Date: ")
    print("So we will deposit this cheque, and the amount shall be deducted soon.")
    print("Please just check if the details on the cheque are correct.")
    print("Payee: Envixy Coffee Shop")
    print(f"Amount: ${total_amount}")
    print(f"Amount In Words: {amount_words}")
    correct_details = input("Are the details correct?\n").lower()

    if correct_details == "yes":
        print("The cheque will be deposited soon, and the amount shall be deducted.")
        exit()
    else:
        print("IDIOT! WHY DON'T YOU FILL IN THE CORRECT DETAILS FROM THE BEGINNING")
        exit("NEVER RETURN TO THIS CAFÃ EVER AGAIN")

def process_online_payment(donate_amount):
    """
    Processes online payment and respects the user's privacy regarding bank details.
    """
    print("Enter your account info.")
    bank = input("Enter your bank\n")
    branch = input("Enter your bank branch\n")
    ac_no = input("Enter your A/C number\n")
    sure = input("Are you sure??\n").lower()

    if sure == "yes":
        print(f"So we will charge ${donate_amount} from A/C No.{ac_no} of {bank} {branch} Branch")
    else:
        print("We didn't save your Bank Account Info.")
        exit()

    print("We respect your bank A/C privacy, so we didn't save your A/C info")
    print(f"Your account has been charged for ${donate_amount}")

if __name__ == "__main__":
    name = welcome_user()
    coffee_menu = display_menu()
    quantity, total = process_order(coffee_menu)
    ask_for_donation()