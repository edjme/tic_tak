from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext, Filters
from telegram import Update

# Обработчик команды /start


def start(update, context):
    update.message.reply_text('Привет! Я простой бот.')

# Обработчик неизвестных команд


def unknown(update, context):
    update.message.reply_text('Извините, не понимаю эту команду.')


def main():
    # Замените 'YOUR_BOT_TOKEN' на полученный у @BotFather токен
    updater = Updater(
        '7127935648:AAGV-HZ6Mk96tvZ5NRUIfE4mW_U9cMy_uIw', use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчика команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрация обработчика неизвестных команд
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
