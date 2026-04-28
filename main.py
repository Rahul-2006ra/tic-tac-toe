import random

# Display the actual game board
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


# Display position guide (reference only)
def display_position_guide():
    print("\n📌 POSITION GUIDE (Reference Only)")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()


# Check winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


# Check draw
def is_draw(board):
    return " " not in board


# Player move
def player_move(board, player, name):
    while True:
        try:
            move = int(input(f"{name} ({player}), enter position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Choose a position between 1 and 9.")
            elif board[move] != " ":
                print("Position already occupied.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Please enter a valid number.")


# Computer move
def computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"
    print("Computer 🤖 chose position:", move + 1)


# Play one round
def play_round(mode, names):
    board = [" "] * 9
    current_player = "X"

    display_position_guide()

    while True:
        display_board(board)

        if current_player == "X":
            player_move(board, "X", names["X"])
        else:
            if mode == 1:
                player_move(board, "O", names["O"])
            else:
                computer_move(board)

        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 {names[current_player]} wins this round!")
            return current_player

        if is_draw(board):
            display_board(board)
            print("🤝 This round is a draw!")
            return "Draw"

        current_player = "O" if current_player == "X" else "X"


# Display scoreboard
def display_scoreboard(scores, names):
    print("\n📊 CURRENT SCOREBOARD")
    print("--------------------------------")
    print(f"{names['X']} (X) Wins : {scores['X']}")
    print(f"{names['O']} (O) Wins : {scores['O']}")
    print(f"Draws            : {scores['Draw']}")
    print("--------------------------------")


# Main game
def main():
    while True:
        print("\n🎮 TIC TAC TOE GAME")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 3:
            print("Thank you for playing! 😊")
            break

        if choice not in [1, 2]:
            print("Please choose a valid option.")
            continue

        # Get player names
        player_x = input("Enter name for Player X: ").strip()
        if not player_x:
            player_x = "Player X"

        if choice == 1:
            player_o = input("Enter name for Player O: ").strip()
            if not player_o:
                player_o = "Player O"
        else:
            player_o = "Computer 🤖"

        names = {"X": player_x, "O": player_o}
        scores = {"X": 0, "O": 0, "Draw": 0}
        round_number = 1

        # Multiple rounds
        while True:
            print(f"\n🔁 ROUND {round_number}")

            winner = play_round(choice, names)
            scores[winner] += 1

            # Show scoreboard after each round
            display_scoreboard(scores, names)

            try:
                cont = int(input("Play another round? (1 = Yes, 0 = No): "))
                if cont == 0:
                    break
                elif cont != 1:
                    print("Invalid choice! Enter 1 or 0.")
                    continue
            except ValueError:
                print("Please enter only 1 or 0.")
                continue

            round_number += 1

        # Final grand winner
        print("\n🏆 FINAL RESULT")
        if scores["X"] > scores["O"]:
            print(f"🎉 GRAND WINNER: {names['X']}")
        elif scores["O"] > scores["X"]:
            print(f"🎉 GRAND WINNER: {names['O']}")
        else:
            print("🤝 Overall match is a DRAW!")

        print("\nThanks for playing! 😊")


# Start game
main()
