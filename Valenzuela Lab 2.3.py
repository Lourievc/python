# Rock, paper, scissors game

import random 
num = random.randint(1,5)

def menu():
    print("[0] Exit game")
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    print("[4] Lizard")
    print("[5] Spock")

menu()
option = int(input("Enter your option: "))

def option1(): 
        if num == 4:
            print("You win! Rock crushes Lizard")
        elif num == 3:
            print("You win! Rock destroys Scissors")
        elif num == 2:
            print("You lose! Paper covers Rock")
        elif num == 5:
            print("You lose! Spock vaporizes Rock")
        else:
            print("It's a tie! Try again.")

def option2():
        if num == 5:
            print("You win! Paper disproves Spock")
        elif num == 1:
            print("You win! Paper covers Rock")
        elif num == 3:
            print("You lose! Scissors cuts Paper")
        elif num == 4:
            print("You lose! Lizard eats Paper")
        else:
            print("It's a tie! Try again.")

def option3():
        if num == 2:
            print("You win! Scissors cuts Paper")
        elif num == 4:
            print("You win! Scissors decapitates Lizard")
        elif num == 1:
            print("You lose! Rock destroys Scissors")
        elif num == 5:
            print("You lose! Spock smashes Scissors")
        else:
            print("It's a tie! Try again.")
            
def option4():
        if num == 2:
            print("You win! Lizard eats Paper")
        elif num == 5:
            print("You win! Lizard Poisons Spock")
        elif num == 1:
            print("You lose! Rock crushes Lizard")
        elif num == 3:
            print("You lose! Scissors decapitates Lizard")
        else:
            print("It's a tie! Try again.")

def option5():
        if num == 3:
            print("You win! Spock smashes Scissors")
        elif num == 1:
            print("You win! Spock vaporizes Rock")
        elif num == 2:
            print("You lose! Paper disproves Spock")
        elif num == 4:
            print("You lose! Lizard Poisons Spock")
        else:
            print("It's a tie! Try again.")

while option != 0:
    if option == 1:
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    else:
        print("Invalid response. Try again.")

    print()
    menu()
    option = int(input("Enter your option: "))

    print("Thanks for playing!")
