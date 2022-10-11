# Selection of Mathematical Functions.
import math
def menu():
    print("\n[0] Exit selection")
    print("[1] Calculate the area of a circle with diameter")
    print("[2] Calculate MPG for a vehicle")
    print("[3] Calculate the total number of hours worked in a week")
    print("[4] Calculate total order of a taco truck")
    print("[5] Check card balance after a purcase")

menu()
option = int(input("Enter your option: "))

def option1():
    #Calculate the area of a circle with diameter
    print("\nCalculate the area of a circle with diameter.\n")
    diameter = float(input("Enter the diameter of a circle: "))
    area = (1/4) * math.pi * diameter * diameter
    print("Area of a circle = %.2f" %area, end= '\n')

def option2():
    #Calculate MPG for a vehicle
    print('\nCalculate MPG for a vehicle.\n')
    distance = float(input('Enter distance traveled in miles: '))
    fuel = float(input('Enter the amount of fuel used in galons: '))
    mpg = distance / fuel
    print('Miles per galon =', mpg, end='\n')

def option3():
    #Calculate the total number of hours worked in a week
    print('\nCalculate the total number of hours worked in a week.\n')
    mon = float(input('Enter the total of hours worked on Monday: '))
    tue = float(input('Enter the total of hours worked on Tuesday: '))
    wed = float(input('Enter the total of hours worked on Wednesday: '))
    thu = float(input('Enter the total of hours worked on Thursday: '))
    fri = float(input('Enter the total of hours worked on Friday: '))
    oth = float(input('If you worked more days during the week, please enter the total hours worked that day. Otherwise, input a "0": '))
    tHours = mon + tue + wed + thu + fri + oth
    print("\nTotal hours worked in a week = %.0f", tHours, end='\n')

def option4():
    #Calculate taco prices at the taco truck
    print('\nCalculate total order of a taco truck.')
    tPrice = float(input('\nEnter price: '))
    tQuantity = int(input('Enter the number of tacos: '))
    totalOrder = tPrice * tQuantity
    print('\nTotal of the order: ',totalOrder, end= '\n')

def option5():
    #Checking card balance after a purchase
    print('\nCheck card balance after a purcase.')
    cBalance = float(input('\nEnter your current card balance: '))
    qSpent = float(input('Enter the quantity spent on your purchase: '))
    cardB = cBalance - qSpent
    print('Your current balance is: ',cardB,end= '\n')

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