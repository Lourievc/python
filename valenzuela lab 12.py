# Lourie Valenzuela
# initialize lists and import libraries
import re
zip_codes, phone_numbers, ssn = [], [], []

# find strings with 5 digits
with open("numbers2.txt") as file:
    for line in file:
        search = re.findall('^\d{5}$', line)
        zip_codes.append(search)

# find 3 digits, . or -, 3 digits, . ot hyphen again, the 4 digits
with open("numbers2.txt") as file:
    for line in file:
        search = re.findall('[(]?\d{3}[-.)]?[ ]?\d{3}[-.]?\d{4}', line)
        phone_numbers.append(search)

# find 3-2-4 digits, hyphen delimited
with open("numbers2.txt") as file:
    for line in file:
        search = re.findall('\d{3}\-\d{2}\-\d{4}', line)
        ssn.append(search)

# print the found zip codes
print('Here are the found zip codes:')
for line in zip_codes:
    if int(len(line)) > 0:
        print(line)

# find the found phone numbers
print('Here are the found phone numbers:')
for line in phone_numbers:
    if int(len(line)) > 0:
        print(line)

# find the found ssn's
print('Here are the found social security numbers:')
for line in ssn:
    if int(len(line)) > 0:
        print(line)

# close file
file.close()