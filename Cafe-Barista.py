import time as t

user_responses = []  # List to store user inputs and questions

def welcome_user():
    try:
        print("Welcome")
        name = input("What is your name?\n").lower()
        user_responses.append(("name", name))  # Store user's name

        if name.lower() == "ben":
            is_evil = input("Are you evil?\n").lower()
            user_responses.append(("evil_status", is_evil))  # Store evil status
            if is_evil == "yes":
                print("You are not welcome here!! Get out You Evil Ben!!!")
                exit("Drink coffee somewhere else and learn some things in Python")
        else:
            print(f"Welcome {name}")

        return name
    except Exception as e:
        print("There was an error. Please try again.")
        return welcome_user()

def display_menu():
    try:
        menu = ["Espresso", "Latte", "Black Coffee", "Milk", "Orange Juice"]
        print("Choose your order:")
        for i, item in enumerate(menu, start=1):
            print(f"{i}. {item}")

        return menu
    except Exception as e:
        print("There was an error. Please try again.")
        return display_menu()

def process_order(menu):
    try:
        order_index = input("Choose the index of your order (e.g., 1 for Espresso):\n")

        order_index = int(order_index)
        if 1 <= order_index <= len(menu):
            order = menu[order_index - 1].lower()
        else:
            print("Invalid order index. Please choose a valid order.")
            return process_order(menu)

        if order == "orange juice":
            print("YOUR ENTIRE BANK ACCOUNT!!!\n")
            exit("GET LOST")
        elif order == "milk":
            print("TRULY GODLIKE CHOICE!")

        prices = {"espresso": 8, "latte": 10, "black coffee": 19, "milk": 0}

        while order not in prices:
            print("Sorry, we don't have that. Please choose from the menu.")
            return process_order(menu)

        while True:
            try:
                quantity_expr = input("How many?\n")
                quantity = eval(quantity_expr)
                total = quantity * prices[order]
                break
            except (ValueError, ZeroDivisionError, NameError):
                print("Enter a valid numerical expression for quantity.")

        print(f"So {name}, you ordered {quantity} {order} and your total is ${total}")
        user_responses.append(("order", f"{quantity} {order}"))
        return quantity, total
    except Exception as e:
        print("There was an error. Please try again.")
        return process_order(menu)

def ask_for_donation():
    try:
        is_good = input("And would you like to donate for the local programmers club? (Y/N)\n").lower()

        if is_good in ["y", "yes", "true", "yup"]:
            donate_amount_expr = input("How much would you like to donate?\n")
            donate_amount = eval(donate_amount_expr)
            user_responses.append(("donation", f"${donate_amount}"))
            confirm_donation(donate_amount)
        else:
            print("No problems!!!!")
            t.sleep(0.5)
            print("Nirdahi insaan ÃÂ°ÃÂÃÂÃÂ­")
    except Exception as e:
        print("There was an error. Please try again.")
        return ask_for_donation()

def confirm_donation(donate_amount):
    try:
        print(f"So, are you sure you want to donate ${donate_amount}? (Y/N)\n")
        confirmation = input().lower()

        if confirmation in ["y", "yes", "true", "yup"]:
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
    except Exception as e:
        print("There was an error. Please try again.")
        return confirm_donation(donate_amount)

def process_cheque(donate_amount):
    try:
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
        correct_details = input("Are the details correct? (Y/N)\n").lower()

        if correct_details in ["y", "yes", "true", "yup"]:
            print("The cheque will be deposited soon, and the amount shall be deducted.")
            exit()
        else:
            print("IDIOT! WHY DON'T YOU FILL IN THE CORRECT DETAILS FROM THE BEGINNING")
            exit("NEVER RETURN TO THIS CAFÃÂ EVER AGAIN")
    except Exception as e:
        print("There was an error. Please try again.")
        return process_cheque(donate_amount)

def process_online_payment(donate_amount):
    try:
        print("Enter your account info.")
        bank = input("Enter your bank\n")
        branch = input("Enter your bank branch\n")
        ac_no = input("Enter your A/C number\n")
        sure = input("Are you sure?? (Y/N)\n").lower()

        if sure in ["y", "yes", "true", "yup"]:
            print(f"So we will charge ${donate_amount} from A/C No.{ac_no} of {bank} {branch} Branch")
        else:
            print("We didn't save your Bank Account Info.")
            exit()

        print("We respect your bank A/C privacy, so we didn't save your A/C info")
        print(f"Your account has been charged for ${donate_amount}")
    except Exception as e:
        print("There was an error. Please try again.")
        return process_online_payment(donate_amount)

if __name__ == "__main__":
    try:
        name = welcome_user()
        coffee_menu = display_menu()
        quantity, total = process_order(coffee_menu)
        ask_for_donation()

        while True:
            repeat = input("Type '/inputs' to see your inputs and questions, or press Enter to exit:\n")
            if repeat == "/inputs":
                for i, (question, response) in enumerate(user_responses, start=1):
                    print(f"{i}. {question}: {response}")

                repeat_question = input("Type the number of the question you want to repeat, or press Enter to continue:\n")
                if repeat_question:
                    try:
                        repeat_question_index = int(repeat_question) - 1
                        if 0 <= repeat_question_index < len(user_responses):
                            repeated_question, _ = user_responses[repeat_question_index]
                            repeated_input = input(f"Repeat '{repeated_question}'? (Y/N)\n").lower()
                            if repeated_input in ["y", "yes", "true", "yup"]:
                                user_responses.append((repeated_question, input(f"{repeated_question}: ")))
                                continue
                    except ValueError:
                        pass

            else:
                break
    except Exception as e:
        print("There was an error. Please try again.")
        exit()