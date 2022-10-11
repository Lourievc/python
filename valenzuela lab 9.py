
# Open the file and read the contents
f = open(input('Enter the original file name: '))
test = f.readlines()
lines = []
# Add lines to an array and strip off new line characters
for line in test:
    new_line = line[:-2]
    lines.append(new_line)
f.close

# Get the target file name
f2 = open(input('Enter the new file name: '))
i = 1
for line in lines:
    with open("myfile.txt", "a") as f:
        f.write('1' + '. ' + '{}' + ' sample'.format(line))
    i += 1
f2.close()

#with open("test.txt", "r") as f:
#    print(f.readlines([:-2]))