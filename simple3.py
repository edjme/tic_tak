from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработчик команды /start
# НЕ РАБОТАЕТ


def start(update, context):
    update.message.reply_text('Привет! Я простой бот.')

# Обработчик неизвестных команд


def unknown(update, context):
    update.message.reply_text('Извините, не понимаю эту команду.')

# Обработчик текстовых сообщений после команды /text_mirror


def mirror_text(update, context):
    user_text = update.message.text
    # Убираем команду и отзеркаливаем текст
    mirrored_text = user_text.replace('/text_mirror', '')[::-1].strip()
    if mirrored_text:
        update.message.reply_text(f'Отзеркаливаем текст: {mirrored_text}')
    else:
        update.message.reply_text(
            'Пожалуйста, введите текст после команды /text_mirror.')


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

    # Регистрация обработчика текстовых сообщений после команды /text_mirror
    dp.add_handler(CommandHandler("text_mirror", mirror_text))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
