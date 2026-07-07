import telebot
import random

TOKEN = "BOT_TOKENINGIZNI_BU_YERGA_YOZING"

bot = telebot.TeleBot(TOKEN)

animes = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Demon Slayer",
    "Jujutsu Kaisen",
    "Solo Leveling"
]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 👋 Men Anime botman.\n/anime yozing va anime tavsiya qilaman."
    )

@bot.message_handler(commands=["anime"])
def anime(message):
    bot.send_message(
        message.chat.id,
        "Sizga tavsiya: 🎬 " + random.choice(animes)
    )

bot.infinity_polling()
