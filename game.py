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

# play(game_list, 0, X)
# play(game_list, 4, X)
# play(game_list, 5, X)
# play(game_list, 6, O)
# play(game_list, 7, O)
# play(game_list, 8, O)

turn = X
for i in range(9):
    display_board(game_list)

    pos = int(input("Που θες να παίξεις;"))
    #Όσο δεν δίνεται σωστή θέση ξαναδοκιμάζουμε
    while play(game_list, pos, turn) == False:
        pos = int(input("Λάθος θέση. Δοκίμασε ξανά:"))

    # Κώδικας αλλαγής σειράς
    if turn==X:
        turn = O
    else:
        turn = X
        
display_board(game_list)