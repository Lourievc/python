#This program deals with lists
from mytest import sortLow
from mytest import sortHigh

def menu():
    print("[0] Exit program")
    print("[1] Create a list")
    print("[2] Show list sorted from a to z")
    print("[3] Show list sorted from z to a")

menu()
option = int(input("Enter your option: "))

list1 = []
def option1():
    while True:
        print('Enter the value ' + str(len(list1) + 1) +
      ' of the list (Or hit enter to stop.):')
        value = input()
        if value == '':
         break
        list1 += [value]  # list concatenation
    if list1 == []:
     print('List is empty.')
    else:
        print("List updated.")
def option2():
    sortLow()
def option3():
    sortHigh()
while option != 0:
    if option == 1:
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    else:
        print("Invalid response. Try again.")

    print()
    menu()
    option = int(input("Enter your option: "))

    print("Thanks for playing!")