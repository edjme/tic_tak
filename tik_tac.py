def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


def check_winner(board):
    # Проверка по горизонтали и вертикали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Запрос хода у игрока
        while True:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(
                input(f"Player {current_player}, enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")

        # Выполнение хода
        board[row][col] = current_player

        # Проверка на победу
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Проверка на ничью
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
