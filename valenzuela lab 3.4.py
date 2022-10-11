colors = ['Black', 'White']
short_colors = {'Black': 'b', 'White': 'w'}
pieces = ['King', 'Queen', 'Bishop', 'Knight', 'Rook', 'Pawn']
short_names = {'King': 'k', 'Queen': 'q', 'Bishop': 'b', 'Knight': 'n', 'Rook': 'r', 'Pawn': 'p'}
max_pieces = {'King': 1, 'Queen': 1, 'Bishop': 2, 'Knight': 2, 'Rook': 2, 'Pawn': 8}
valid_x = [1,2,3,4,5,6,7,8]
valid_y = ['a','b','c','d','e','f','g','h']



while True:
    valid_color = False
    valid_piece = False
    valid_loc = False

    print('Please enter a Chess color. Choose from: ')
    for i in colors:
        print(i)
    check_color = input()
    if check_color == '':
        break
    if (check_color in colors or check_color in short_colors):
        valid_color = True

    print('Please enter a Chess piece. Choose from: ')
    for i in pieces:
        print(i)
    check_name = input()
    if check_name == '':
        break
    if (check_name in pieces or check_name in short_names):
        valid_piece = True

    loc = input('Please enter a coordinate in algebraic chess notation: ')
    if len(loc) == 2: 
        loc_int = int(loc[1:])
        if (loc[:1] in valid_y and loc_int in valid_x):
            valid_loc = True
    
    if (valid_color == True and valid_piece == True and valid_loc == True):
        print('\n ===== This is a valid Chess configuration =====\n')
    else:
        print('\n ===== This is not a valid Chess configuration =====\n')