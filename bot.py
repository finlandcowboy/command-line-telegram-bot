from subprocess import check_output
import telebot, time
import sys
from telebot import types
token = ''
user_id = 0
if sys.argv[1] == '-token' and len(sys.argv) > 2:
    with open(sys.argv[2]) as token_file:
        config_lines = token_file.readlines()
        token = config_lines[0].replace('\n', '')
        user_id = int(config_lines[1].replace('\n', ''))
else:
    raise "Invalid token\nExample: python3 main.py -token 'your_token_file\nOr enter your token to config.txt'"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def main(message):
    if user_id == message.chat.id:
        command = message.text
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Повторить", callback_data=command)
        markup.add(button)
        try:
            bot.send_message(message.chat.id, check_output(command, shell=True))
        except:
            bot.send_message(message.chat.id, 'Invalid input')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    command = call.data 
    try:
        markup = types.InlineKeyboardMarkup() 
        button = types.InlineKeyboardButton(text="Повторить", callback_data=command) 
        markup.add(button)
        bot.send_message(user_id, check_output(command, shell = True), reply_markup = markup)
    except:
        bot.send_message(user_id, "Invalid input") 


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)

