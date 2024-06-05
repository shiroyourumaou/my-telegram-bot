import telebot

# Замените 'TOKEN' на токен вашего бота
TOKEN = '7033822246:AAHWxgXreZ3QbKZwy0Y059Fj_CyxWOpm5wo'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
# Отключаем webhook
bot.remove_webhook()

# Функция для пересылки сообщений из одного канала в другие
def forward_messages(update):
    # Пересылка сообщения в другие каналы (замените 'destination_channel_usernames' на юзернеймы целевых каналов)
    destination_channel_usernames = ['ForwardAutoPerm', 'fproperm', 'forwardchaikovskiy','forwardufa','forwardizhevskauction','forwardautovolgograd','ForwardAvtoTyumen','forwardnizhnevartovsk','forwardautosurgut','forwardomsk','ForwardPerm']
    for channel_username in destination_channel_usernames:
        try:
            # Проверяем, что chat_id канала не совпадает с chat_id исходного сообщения
            if update.chat.username != channel_username:
                bot.forward_message('@' + channel_username, update.chat.id, update.message_id)
            else:
                print(f"Сообщение уже из канала @{channel_username}. Пропускаем.")
        except telebot.apihelper.ApiTelegramException as e:
            if "message has protected content" in str(e):
                print("Сообщение содержит защищенный контент и не может быть переслано. Пропускаем.")
                continue
            else:
                raise e
# Обработчик для получения сообщений из каналов
@bot.channel_post_handler(content_types=['text', 'photo', 'video', 'document', 'audio'])
def handle_channel_post(update):
    forward_messages(update)

# Запускаем бота
bot.polling()