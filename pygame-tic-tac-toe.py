import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 300, 300
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Fonts
font = pygame.font.Font(None, 36)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_user_move():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // (HEIGHT // 3)
                col = x // (WIDTH // 3)
                return row, col

def get_computer_move(board):
   for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_winner(board, "O"):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "
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


def draw_board(board):
    screen.fill(WHITE)

    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, BLACK, (col * WIDTH // 3, row * HEIGHT // 3, WIDTH // 3, HEIGHT // 3), 1)

            text = font.render(board[row][col], True, BLACK)
            text_rect = text.get_rect(center=(col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6))
            screen.blit(text, text_rect)

    pygame.display.flip()

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["Player A", "Player B"]

    print("Welcome to Tic Tac Toe!")

    clock = pygame.time.Clock()

    for turn in range(9):
        current_player = players[turn % 2]
        print(f"\n{current_player}'s Turn:")
        draw_board(board)

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
            draw_board(board)
            print("Player A wins!")
            break
        elif check_winner(board, "O"):
            draw_board(board)
            print("Player B wins!")
            break
        elif is_board_full(board):
            draw_board(board)
            print("It's a tie!")
            break

        clock.tick(FPS)

if __name__ == "__main__":
    tic_tac_toe()
    pygame.quit()