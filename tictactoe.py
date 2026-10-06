# Tic-Tac-Toe using Minimax Algorithm

# Display the board
def display_board(board):
    print()
    print(" | ".join(board[0:3]))
    print("--+---+--")
    print(" | ".join(board[3:6]))
    print("--+---+--")
    print(" | ".join(board[6:9]))
    print()


# Check whether the game is over
def terminal_test(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True

    return " " not in board


# Return utility value
def utility(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c]:
            if board[a] == "X":
                return 1
            elif board[a] == "O":
                return -1

    return 0


# Return available actions
def actions(board):
    return [i for i in range(9) if board[i] == " "]


# Generate the resulting state
def result(board, action, player):
    new_board = board.copy()
    new_board[action] = player
    return new_board


# MAX-VALUE function
def max_value(board):
    if terminal_test(board):
        return utility(board)

    v = float("-inf")

    for action in actions(board):
        new_board = result(board, action, "X")
        v = max(v, min_value(new_board))

    return v


# MIN-VALUE function
def min_value(board):
    if terminal_test(board):
        return utility(board)

    v = float("inf")

    for action in actions(board):
        new_board = result(board, action, "O")
        v = min(v, max_value(new_board))

    return v


# MINIMAX-DECISION function
def minimax_decision(board):
    best_value = float("-inf")
    best_action = None

    for action in actions(board):
        new_board = result(board, action, "X")
        value = min_value(new_board)

        if value > best_value:
            best_value = value
            best_action = action

    return best_action


# Main game
def play_game():
    board = [" "] * 9

    print("TIC-TAC-TOE")
    print("You are O, AI is X")
    print("Positions are:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        # AI's turn
        print("\nAI's turn...")
        ai_move = minimax_decision(board)
        board[ai_move] = "X"
        display_board(board)

        if terminal_test(board):
            break

        # Human's turn
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1

                if move in actions(board):
                    board[move] = "O"
                    break
                else:
                    print("Invalid move. Try again.")

            except ValueError:
                print("Please enter a number from 1 to 9.")

        display_board(board)

        if terminal_test(board):
            break

    # Display result
    score = utility(board)

    if score == 1:
        print("AI (X) wins!")
    elif score == -1:
        print("You (O) win!")
    else:
        print("It's a draw!")


# Start the game
play_game()
