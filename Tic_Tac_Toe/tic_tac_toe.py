# Tic-Tac-Toe game by Ryan C. McDermott

import string

invalid_chars = string.ascii_letters + string.punctuation

# Game Rendering

#**********************************#

def create_board():
    ROW1 = ["|   ","|   ","|    |"]
    ROW2 = ["|   ","|   ","|    |"]
    ROW3 = ["|   ","|   ","|    |"]

    board = [ROW1,ROW2,ROW3]

    return board

def draw_board(board):
    UNDER_SCORE = " ---  ---  --- "
    print(UNDER_SCORE)
    print(board[0][0],board[0][1],board[0][2])
    print(UNDER_SCORE)
    print(board[1][0],board[1][1],board[1][2])
    print(UNDER_SCORE)
    print(board[2][0],board[2][1],board[2][2])
    print(UNDER_SCORE)

def update_board_X(board, x, y):
    if y == 2:
        board[x][y] = "| X  |"
    if y != 2:
        board[x][y] = "| X "
    return board

def update_board_O(board, x, y):
    if y == 2:
        board[x][y] = "| O  |"
    if y != 2:
        board[x][y] = "| O "
    return board

#**********************************#

# Board movement and occupied spots

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def player_move_X(board):
    input_user = input("Player X, Please select position to play: (in format: 'row column' from 1-3 e.g. '1 3'):\n>").replace(" ", "")
    while (len(input_user) != 2 or input_user[0].isalpha() == True or input_user[1].isalpha() == True or
    int(input_user[0]) > 3 or int(input_user[0]) < 0 or int(input_user[1]) > 3 or int(input_user[1]) < 0):
        print("Invalid input!")
        input_user = input("Player X, Please select position to play: (in format: 'row column' from 1-3 e.g. '1 3'):\n>").replace(" ", "")
    pos_x, pos_y = input_user[0], input_user[1]
    position_x = int(pos_x)-1
    position_y = int(pos_y)-1
    position = [position_x, position_y]
    return position

def player_move_O(board):
    input_user = input("Player O, please select position to play: (in format: 'row column' from 1-3 e.g. '1 3'):\n>").replace(" ", "")
    while (len(input_user) != 2 or input_user[0].isalpha() == True or input_user[1].isalpha() == True or
    int(input_user[0]) > 3 or int(input_user[0]) < 0 or int(input_user[1]) > 3 or int(input_user[1]) < 0):
        print("Invalid input!")
        input_user = input("Player O, Please select position to play: (in format: 'row column' from 1-3 e.g. '1 3'):\n>").replace(" ", "")
    pos_x, pos_y = input_user[0], input_user[1]
    position_x = int(pos_x)-1
    position_y = int(pos_y)-1
    position = [position_x, position_y]
    return position

def update_game(board, x, y):
    if board[x][y] == 0:
        board[x][y] = "CHECK"
    return board

def update_X(board, x, y):
    if board[x][y] == 0:
        board[x][y] = "X"
    return board

def update_O(board, x, y):
    if board[x][y] == 0:
        board[x][y] = "O"
    return board

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Winning conditions
def check_winner(game):
    win = False
    while win == False:
        if game[0][0] == game[1][1] == game[2][2] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][2] == game[1][1] == game[2][0] != 0:
            player = game[0][2]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][0] == game[0][1] == game[0][2] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[1][0] == game[1][1] == game[1][2] != 0:
            player = game[1][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[2][0] == game[2][1] == game[2][2] != 0:
            player = game[2][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][0] == game[1][0] == game[2][0] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][1] == game[1][1] == game[2][1] != 0:
            player = game[0][1]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][2] == game[1][2] == game[2][2] != 0:
            player = game[0][2]
            win = True
            print(f"Player {player} wins!")
            return False
        if any(0 in gm for gm in game) == False:
            print("It's a draw!")
            return False
        else:
            return True
            break


# Main game loop

def main():
    board = create_board()
    draw_board(board)
    occupied = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    play = True
    while play == True:
        pos_play_X = player_move_X(game)
        while occupied[pos_play_X[0]][pos_play_X[1]] == "CHECK":
            print("Space already occupied... Please try again:")
            pos_play_X = player_move_X(game)
        board = update_board_X(board, pos_play_X[0], pos_play_X[1])
        update_X(game, pos_play_X[0], pos_play_X[1])
        update_game(occupied, pos_play_X[0], pos_play_X[1])
        draw_board(board)
        play = check_winner(game)
        if play == False:
            break
        pos_play_O = player_move_O(game)
        while occupied[pos_play_O[0]][pos_play_O[1]] == "CHECK":
            print("Space already occupied... Please try again:")
            pos_play_O = player_move_O(game)
        board = update_board_O(board, pos_play_O[0], pos_play_O[1])
        update_O(game, pos_play_O[0], pos_play_O[1])
        update_game(occupied, pos_play_O[0], pos_play_O[1])
        draw_board(board)
        play = check_winner(game)
        if play == False:
            break


if __name__ == '__main__':
    main()
