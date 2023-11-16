#include <iostream>
#include <string>

int main() {
    std::cout << "Welcome" << std::endl;
    
    std::string name;
    std::cout << "What is your name" << std::endl;
    std::getline(std::cin, name);
    
    if (name == "Ben") {
        std::string isevil;
        std::cout << "Are you evil?" << std::endl;
        std::getline(std::cin, isevil);
        
        if (isevil == "Yes") {
            std::cout << "You are not welcome here!! Get out You Evil Ben!!!" << std::endl;
            std::exit(0);
        }
    } else {
        std::cout << "Welcome " << name << std::endl;
    }
    
    std::string menu = "Espresso, Latte, Black Coffee, Milk, Orange Juice";
    std::cout << menu << std::endl;
    
    std::string order;
    std::cout << "Choose your order" << std::endl;
    std::getline(std::cin, order);
    
    if (order == "orange juice") {
        std::cout << "PATHETIC!!!" << std::endl;
        std::exit(0);
    } else if (order == "Milk") {
        std::cout << "TRULY GODLIKE CHOICE!" << std::endl;
    }
    
    std::cout << "How many" << std::endl;
    std::string quantity;
    std::getline(std::cin, quantity);
    
    int price = 8;
    int total = std::stoi(quantity) * price;
    
    std::cout << "So " << name << ", you ordered " << quantity << " " << order << " and your total is $" << total << std::endl;
    std::cout << "And would you like to donate for the local programmers club?" << std::endl;
    
    std::string isgood;
    std::getline(std::cin, isgood);
    
    if (isgood == "Yes") {
        std::cout << "How many $?" << std::endl;
        std::string donate;
        std::getline(std::cin, donate);
        
        std::cout << "So is it sure that you want to donate $" << donate << "?" << std::endl;
        std::cout << "Yes or No" << std::endl;
        
        std::string yn;
        std::getline(std::cin, yn);
        
        if (yn == "No") {
            std::cout << "No problems, Have a good day" << std::endl;
            std::exit(0);
        } else {
            std::cout << "Your account has been charged for $" << donate << std::endl;
        }
    } else {
        std::cout << "No problems😥😢😭" << std::endl;
        std::cout << "The price for you has been increased by 100 times you evil person\nNow the price for you is $" << price * 100 << std::endl;
        std::exit(0);
    }
    
    return 0;
}
