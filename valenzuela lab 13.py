from datetime import date
 
def numOfDays(date, input):
    return (date-input).days
     
# Driver program
dateNap = date(1796, 8, 15)
dateHar = date(1941, 12, 7)
dateWri = date(1903, 12, 17)
date1 = date.today()

print(" [1] The birthdate of Napoleon Bonaparte  \n [2] The bombing of Pearl Harbor \n [3] The Wright Brothers 1st flight ")
input = input("Please, select one of the historical events above to print the time that has passed since that time to today's date: ")

if input == "1":
    print(numOfDays(date1, dateNap), "days")

elif input == "2":
    print(numOfDays(date1, dateHar), "days")

elif input == "3":
    print(numOfDays(date1, dateWri), "days")

else:
    print("Invalid choice")