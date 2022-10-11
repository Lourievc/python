import random as r
import string

def rand_letter():
    random = r.choice(string.ascii_letters)
    return random 

def rand_int():
    random = r.randint(1,9999)
    return random

def rand_float():
    random = round(r.uniform(0, 100000), 2)
    return random


def main():
    # Ask the user for the file name and open that file
    input_file = input('Enter a file: ')
    f = open(input_file, "a")
    
    # Start main loop, loop 20 times
    i1 = 1
    while i1 < 21:

        # Start sub-loop for characters, loop 5 times
        i2 = 1
        while i2 < 6:
            letter = rand_letter()
            f.write('{}'.format(letter))
            i2 += 1

        # Add space
        f.write(' ')

        # Write a random integer
        integer = rand_int()
        f.write('{}'.format(integer))

        # Add space
        f.write(' ')

        # Write a random float
        floater = rand_float()
        f.write('{}'.format(floater))

        # Add new line
        f.write('\n')

        # Increment loop
        i1 += 1

    # Loop file
    f.close()

main()