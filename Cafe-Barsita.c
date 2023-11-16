#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    printf("Welcome\n");

    char name[100];
    printf("What is your name\n");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0'; // Removing the newline character
    
    if (strcmp(name, "Ben") == 0) {
        char isevil[5];
        printf("Are you evil?\n");
        fgets(isevil, sizeof(isevil), stdin);
        isevil[strcspn(isevil, "\n")] = '\0'; // Removing the newline character

        if (strcmp(isevil, "Yes") == 0) {
            printf("You are not welcome here!! Get out You Evil Ben!!!\n");
            exit(0);
        }
    } else {
        printf("Welcome %s\n", name);
    }

    char menu[] = "Espresso, Latte, Black Coffee, Milk, Orange Juice";
    printf("%s\n", menu);

    char order[20];
    printf("Choose your order\n");
    fgets(order, sizeof(order), stdin);
    order[strcspn(order, "\n")] = '\0'; // Removing the newline character

    if (strcmp(order, "orange juice") == 0) {
        printf("PATHETIC!!!\n");
        exit(0);
    } else if (strcmp(order, "Milk") == 0) {
        printf("TRULY GODLIKE CHOICE!\n");
    }

    printf("How many\n");
    char quantity[10];
    fgets(quantity, sizeof(quantity), stdin);
    quantity[strcspn(quantity, "\n")] = '\0'; // Removing the newline character

    int price = 8;
    int total = atoi(quantity) * price;

    printf("So %s, you ordered %s %s and your total is $%d\n", name, quantity, order, total);
    printf("And would you like to donate for the local programmers club?\n");

    char isgood[5];
    fgets(isgood, sizeof(isgood), stdin);
    isgood[strcspn(isgood, "\n")] = '\0'; // Removing the newline character

    if (strcmp(isgood, "Yes") == 0) {
        printf("How many $?\n");
        char donate[10];
        fgets(donate, sizeof(donate), stdin);
        donate[strcspn(donate, "\n")] = '\0'; // Removing the newline character

        printf("So is it sure that you want to donate $%s?\n", donate);
        printf("Yes or No\n");

        char yn[5];
        fgets(yn, sizeof(yn), stdin);
        yn[strcspn(yn, "\n")] = '\0'; // Removing the newline character

        if (strcmp(yn, "No") == 0) {
            printf("No problems, Have a good day\n");
            exit(0);
        } else {
            printf("Your account has been charged for $%s\n", donate);
        }
    } else {
        printf("No problems😥😢😭\n");
        printf("The price for you has been increased by 100 times you evil person\nNow the price for you is $%d\n", price * 100);
        exit(0);
    }

    return 0;
}
