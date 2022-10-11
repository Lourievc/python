#Lourie Valenzuela
# initialize lists
phone_numbers, ssn, zip_codes = [], [], []

# loop through the lines of the file, remove symbols, append to list
def isPhoneNumber(line):
    output = ''
    line_str = str(line)
    if len(line_str) == 15:
        for i in line_str:
            if i.isnumeric():
                output += i
    phone_numbers.append(output)

# loop through the lines of the file, check for expected hyphens, check that everything else is a number
def isSSN(text):
    if len(text) != 12:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            return False
        if text[6] != '-':
            return False
        for i in range(7,9):
            if not text[i].isdecimal():
                return False
    return True

# find lines that are 5 digits long
def find_raw_zip(text):
    if len(text) == 6:
        zip_codes.append(text)

# loop through ssn list, print lines that are not empty, remove newline char
print('Here are the SSN\'s that were found: ')
with open("numbers.txt") as file:
    for line in file:
        if isSSN(line) == True:
            ssn.append(line)
for line in ssn:
    print(line[:-2])

# loop through file, call find_raw_zip(), print lines minus newline char
print('Here are the zip codes that were found: ')
with open("numbers.txt") as file:
    for line in file:
        find_raw_zip(line)
for line in zip_codes:
    print(line[:-1])

# loop through file, call isPhoneNumber, print lines in phone_numbers[] that are not empty
print('Here are the phone numbers that were found: ')
with open("numbers.txt") as file:
    for line in file:
        isPhoneNumber(line)
for line in phone_numbers:
    if int(len(line)) > 0:
        print(line)

# close file
file.close()