import random


def addLetters():
    import string
    print(random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters))

addLetters()

def addIntegers():
    randomlist = random.sample(range(0, 999), 4)
    print(randomlist)
addIntegers()

def addFloat():
    floatrandom = round(random.uniform(0, 100000), 2)
    print(floatrandom)
addFloat()

L = addLetters()
I = addIntegers()
F = addFloat()

f = open("notmyfile.txt", "a")
f.write(L + I + L + F)
f.close()

f = open("notmyfile.txt", "r")
print(f.read())