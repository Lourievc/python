
list1 = []
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
        list1 = list(set(list1))
        list1.sort()
        print('Here are the values of the list: ')
        print(list1)
