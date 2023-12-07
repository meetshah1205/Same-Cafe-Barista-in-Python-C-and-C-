import java.util.Scanner;

public class CoffeeShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome");
        System.out.print("What is your name\n");
        String name = scanner.nextLine();

        if (name.equals("Ben")) {
            System.out.print("Are you evil?\n");
            String isEvil = scanner.nextLine();
            if (isEvil.equalsIgnoreCase("Yes")) {
                System.out.println("You are not welcome here!! Get out You Evil Ben!!!");
                System.exit(0);
            }
        } else {
            System.out.println("Welcome " + name);
        }

        String menu = "Espresso, Latte, Black Coffee, Milk, Orange Juice";
        System.out.println(menu);
        System.out.println("Choose your order\n");
        String order = scanner.nextLine().toLowerCase();

        if (order.equals("orange juice")) {
            System.out.println("PATHETIC!!!\n");
            System.exit(0);
        } else if (order.equals("milk")) {
            System.out.println("TRULY GODLIKE CHOICE!");
        }

        int quantity;
        while (true) {
            try {
                System.out.println("How many\n");
                quantity = Integer.parseInt(scanner.nextLine());
                int price = 8;
                int total = quantity * price;
                break;
            } catch (NumberFormatException e) {
                System.out.println("WHAT AN IDIOT! Enter a valid number.");
            }
        }

        System.out.println("So " + name + ", you ordered " + quantity + " " + order + " and your total is $" + (quantity * 8));

        System.out.println("And would you like to donate for the local programmers club?\n");
        String isGood = scanner.nextLine();

        if (isGood.equalsIgnoreCase("Yes")) {
            System.out.println("How many $?\n");
            String donate = scanner.nextLine();
            System.out.println("So is it sure that you want to donate $" + donate + "?");
            System.out.println("Yes or No\n");
            String yn = scanner.nextLine();

            if (yn.equalsIgnoreCase("No")) {
                System.out.println("No problems, Have a good day");
                System.exit(0);
            } else if (yn.equalsIgnoreCase("Yes")) {
                System.out.println("So would you like to pay with UPI or Give Cash/Cheque ?\n");
                String caup = scanner.nextLine();

                if (caup.equalsIgnoreCase("cash")) {
                    System.out.println("Ok then give cash $");
                } else if (caup.equalsIgnoreCase("cheque")) {
                    System.out.println("YOU HAVE SO MUCH MONEY!!!");
                    try {
                        Thread.sleep(5000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("Anyway ");
                    System.out.println("Here are the cheque details:\n");
                    System.out.println("Payee: Envixy Coffee Shop");
                    int subto = Integer.parseInt(donate) + (quantity * 8);
                    System.out.println("Amount: $" + subto);
                    System.out.print("Amount In Words: ");
                    String amountWords = scanner.nextLine();
                    System.out.print("Date: ");
                    String date = scanner.nextLine();
                    System.out.println("So we will deposit this cheque, and the amount shall be deducted soon.");
                    System.out.println("Please just check if the details on the cheque are correct.");
                    System.out.println("Payee: Envixy Coffee Shop");
                    System.out.println("Amount: $" + subto);
                    System.out.println("Amount In Words: " + amountWords);
                    System.out.println("Are the details correct?\n");
                    String correct = scanner.nextLine();

                    if (correct.equalsIgnoreCase("Yes")) {
                        System.out.println("The cheque will be deposited soon, and the amount shall be deducted soon.");
                        System.exit(0);
                    } else {
                        System.out.println("IDIOT SO WHY DON'T YOU FILL IN THE CORRECT DETAILS IN THE FIRST TIME");
                        System.exit(0);
                    }
                } else {
                    System.out.println("Enter your account Info.");
                }

                System.out.print("Enter your bank\n");
                String bank = scanner.nextLine();
                System.out.print("Enter your bank branch\n");
                String branch = scanner.nextLine();
                System.out.print("Enter your A/C number\n");
                String acno = scanner.nextLine();
                System.out.print("Are you sure??\n");
                String sure = scanner.nextLine();

                if (sure.equalsIgnoreCase("Yes")) {
                    System.out.println("So we will charge $" + donate + " from A/C No." + acno + " of " + bank + " " + branch + " Branch");
                } else {
                    System.out.println("We didn't save your Bank Account Info.");
                    System.exit(0);
                }

                System.out.println("We respect your bank A/C privacy so we didn't save your A/C info");
                System.out.println("Your account has been charged for $" + donate);
            }
        } else {
            System.out.println("No problems!!!!");
            System.out.println("The price for you has been increased by 100 times you evil person\nNow the price for you is $" + (8 * 100));
            System.out.println("Now pay the cost $" + (8 * 100));
            System.out.println("You don't have an option");
            System.out.println("YOU CAN'T ESCAPE!!!!");
            System.exit(0);
        }
    }
}