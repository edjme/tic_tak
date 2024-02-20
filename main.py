from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext, Filters
from telegram import Update
import random

# States for the conversation
CHOOSING, PLAYING = range(2)

# Information about the current game
games = {}


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hi! Let's play tic-tac-toe. Use the /play command to start a new game.")
    return CHOOSING


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


def check_winner(chat_id: int) -> bool:
    board = games[chat_id]['board']
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return True

    return False


def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "The game has been canceled. Come back when you want to play again!")
    return ConversationHandler.END


def main() -> None:
    updater = Updater("6958998414:AAF6sCtDz7qtlEi3-CmMcRnr0s_sMAiwNfY")

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [CommandHandler('play', play)],
            PLAYING: [MessageHandler(Filters.regex(r'^[1-9]$'), make_move)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
