X = "X"
O = "O"
KENO = " "

game_list = [KENO]*9

def display_board(board):
    print('', board[0], '|', board[1], '|', board[2])
    print('---+---+---')
    print('', board[3], '|', board[4], '|', board[5])
    print('---+---+---')
    print('', board[6], '|', board[7], '|', board[8])

def play(board, position, symbol):
    '''Η συνάρτηση αυτή δέχεται έναν πίνακα παιχνιδιού, τη θέση και το σύμβολο που πρέπει να παιχτεί.
    Κάνει έλεγχο ορίων, καθώς και έλεγχο για άδεια θέση.
    Aν μπορεί τοποθετεί το σύμβολο στη θέση και επιστρέφει True.
    Αν προκύψει κάποιο σφάλμα επιστρέφει False.
    '''
    if position >= len(board) or position < 0:
        return False 
    if board[position] != KENO:
        return False
    
    board[position] = symbol
    return True

def check_win(board):
    if (board[0] == board[1] == board[2]) and board[0]!=KENO:
        return board[0]
    if (board[3] == board[4] == board[5]) and board[3]!=KENO:
        return board[3]
    if (board[6] == board[7] == board[8]) and board[6]!=KENO:
        return board[6]
    if (board[0] == board[3] == board[6]) and board[0]!=KENO:
        return board[0]
    if (board[1] == board[4] == board[7]) and board[1]!=KENO:
        return board[1]
    if (board[2] == board[5] == board[8]) and board[2]!=KENO:
        return board[2]
    if (board[0] == board[4] == board[8]) and board[0]!=KENO:
        return board[0]
    if (board[2] == board[4] == board[6]) and board[2]!=KENO:
        return board[2]
    return KENO 

lines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def ai_play(board, symbol):

    # επίθεση
    for line in lines:
        count_s = 0 
        for pos in line:
            if board[pos] == symbol:
                count_s += 1
                
        if count_s == 2:
            hole = 0
            for pos in line:
                if board[pos] == KENO:
                    hole = pos
                    break
                
            play(board, hole, symbol)
            break

    # άμυνα
    if symbol == X:
        enemy_symbol = O
    # ??????
    
    enemy_symbol = -1 # ?????
    for line in lines:
        count_s = 0 
        for pos in line:
            if board[pos] == enemy_symbol:
                count_s += 1
                
        if count_s == 2:
            hole = 0
            for pos in line:
                if board[pos] == KENO:
                    hole = pos
                    break
                
            play(board, hole, symbol)
            break

    # tyxaio


# play(game_list, 0, X)
# play(game_list, 4, X)
# play(game_list, 5, X)
# play(game_list, 6, O)
# play(game_list, 7, O)
# play(game_list, 8, O)


turn = X
for i in range(9):
    display_board(game_list)

    if i == 4:
        ai_play(game_list, turn)
    else:
        pos = int(input("Που θες να παίξεις;"))
        # Όσο δεν δίνεται σωστή θέση ξαναδοκιμάζουμε
        while play(game_list, pos, turn) == False:
            pos = int(input("Λάθος θέση. Δοκίμασε ξανά:"))

   
    winner = check_win(game_list)

    if winner!=KENO:
        break

     # Κώδικας αλλαγής σειράς
    if turn==X:
        turn = O
    else:
        turn = X

display_board(game_list)

if winner!=KENO:
    print("Νίκησε ο", winner) 
