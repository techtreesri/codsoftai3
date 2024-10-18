import math

# Initialize the Tic-Tac-Toe board
board = [['-' for _ in range(3)] for _ in range(3)]

# Function to print the current board
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Check if there are any moves left
def is_moves_left(board):
    for row in board:
        if '-' in row:
            return True
    return False

# Check the score of the board
def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2] != '-':
            return 1 if row[0] == 'O' else -1

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return 1 if board[0][col] == 'O' else -1

    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return 1 if board[0][0] == 'O' else -1
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return 1 if board[0][2] == 'O' else -1

    # No winner: return 0
    return 0

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # If AI has won the game, return the score
    if score == 1:
        return score

    # If Human has won the game, return the score
    if score == -1:
        return score

    # If no moves are left, it's a draw
    if not is_moves_left(board):
        return 0

    # If this is the maximizer's move (AI - 'O')
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = '-'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best

    # If this is the minimizer's move (Human - 'X')
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = '-'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = '-'
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Human's turn (Player 'X')
def human_move():
    while True:
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1
        if board[row][col] == '-':
            board[row][col] = 'X'
            break
        else:
            print("Invalid move. Try again.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and AI is 'O'.")
    print_board(board)

    while True:
        # Human's move
        print("Your turn:")
        human_move()
        print_board(board)
        if evaluate(board) == -1:
            print("You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI's turn:")
        move = find_best_move(board)
        board[move[0]][move[1]] = 'O'
        print_board(board)
        if evaluate(board) == 1:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

play_game()
