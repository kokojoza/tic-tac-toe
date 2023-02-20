def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def get_move(player, board):
    while True:
        move = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
        if move < 0 or move > 8:
            print("Неверное число. Только (1-9)")
        elif board[move] != " ":
            print("Это место уже занято, пожалуйста, попробуйте еще раз.")
        else:
            return move


def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False


def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board)
    player = "X"
    while True:
        move = get_move(player, board)
        board[move] = player
        print_board(board)
        if check_win(board):
            print(f"Игрок {player} победил!")
            break
        if " " not in board:
            print("Ничья")
            break
        player = "O" if player == "X" else "X"


play_game()
