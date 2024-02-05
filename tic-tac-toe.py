# Create a Terminal Game of TIC TAC TOE in Python by utilizing prompt engineering concepts

#High Level Features: 
#-Human Player turn
#-Computer Player Turn
#-Getting Human Player Input
#-Checking after every turn/move to see if someone has won 
#-Printing the board for the human player to see

#Features:

# Computer AI, we can do player vs computer like it to be smart, but can start with it being dumb and simple-- For now we will have it make random moves
#User input
#-Where they want to put their X or O
#-Whether they want to be X or O
#-Maybe we do this by user inputting row and column for their row

#Be able to display the board and update the visualization of the board with the moves that have been made

#Flow of Game
#-Who goes first? Player A
#-Player A makes their move
#-Now it's Player B's Turn, Player B makes their move
#- This continues until someone has a tic-tac-toe (3 spaces in a row, column or diagonally are all occupied by the same player's symbbol (X or O)) or all of the spaces are filled (tie)


#Player A: Human
#-Prompt for input for their move
#-We need to tell the user how to enter their move
#-Need to be able to see the board 
#-Need to prevent placing X's or O's in a space that is occupied already

#Computer Player
#-Needs to know what spaces are available on which to make moves and if their randomly generated move is valid or not
#


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_user_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    # Check for winning moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_winner(board, "O"):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "

    # Check for opponent winning moves and block them
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_winner(board, "X"):
                    board[row][col] = "O"
                    return row, col
                board[row][col] = " "

    # If no winning or blocking moves, make a random move
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["Player A", "Player B"]
    
    print("Welcome to Tic Tac Toe!")

    for turn in range(9):
        current_player = players[turn % 2]
        print(f"\n{current_player}'s Turn:")
        print_board(board)

        if current_player == "Player A":
            row, col = get_user_move()
        else:
            row, col = get_computer_move(board)

        if board[row][col] == " ":
            board[row][col] = "X" if current_player == "Player A" else "O"
        else:
            print("Invalid move. This space is already occupied.")
            turn -= 1  # Repeat the same turn

        if check_winner(board, "X"):
            print_board(board)
            print("Player A wins!")
            break
        elif check_winner(board, "O"):
            print_board(board)
            print("Player B wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()