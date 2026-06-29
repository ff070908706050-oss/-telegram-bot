import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID') 

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "බොට් සාර්ථකව ක්‍රියාත්මකයි!")

# උදේට මැසේජ් එක යවන තැන
@server.route('/send-gm')
def send_good_morning():
    try:
        bot.send_message(CHANNEL_ID, "☀️ සුභ උදෑසනක් වේවා! (Good Morning) 🌸")
        return "GM Message Sent!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

# රෑට මැසේජ් එක යවන තැන
@server.route('/send-gn')
def send_good_night():
    try:
        bot.send_message(CHANNEL_ID, "🌙 සුභ රාත්‍රියක්! (Good Night) ✨")
        return "GN Message Sent!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

@server.route("/")
def home():
    return "Bot is alive!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    server.run(host="0.0.0.0", port=port)
