# Information about the current game
games = {}

# ...

def play(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    games[chat_id] = {'board': [' '] * 9, 'player': 'X', 'winner': None}
    print_board(update)
    update.message.reply_text(
        f"The game has started! Your move, {games[chat_id]['player']}. Use numbers 1 to 9 for your move.")
    return PLAYING

def print_board(update: Update):
    chat_id = update.message.chat_id
    board = games[chat_id]['board']
    message = f"\n{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n"
    update.message.reply_text(message)

def make_move(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    move = int(update.message.text)

    if 1 <= move <= 9 and games[chat_id]['board'][move - 1] == ' ' and not games[chat_id]['winner']:
        games[chat_id]['board'][move - 1] = games[chat_id]['player']

        if check_winner(chat_id):
            games[chat_id]['winner'] = games[chat_id]['player']
            update.message.reply_text(
                f"The game is over! Player {games[chat_id]['winner']} wins!")
            print_board(update)
            return ConversationHandler.END
        elif ' ' not in games[chat_id]['board']:
            update.message.reply_text("The game is over! It's a draw.")
            print_board(update)
            return ConversationHandler.END

        games[chat_id]['player'] = 'O' if games[chat_id]['player'] == 'X' else 'X'
        print_board(update)
        update.message.reply_text(f"Player {games[chat_id]['player']}'s turn.")
    else:
        update.message.reply_text("Invalid move. Try again.")
