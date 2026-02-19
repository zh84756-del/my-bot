import telebot
import requests
from flask import Flask
import threading
import os

TOKEN = "8432274497:AAFwdhTRgczKQ-XfHlkkoGwUrQzS52Sy1Jo"
GEMINI_KEY = "AIzaSyDzU29LyJcexRu64Tf27Jbmkcu_da2fSmk"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is Running!"

@bot.message_handler(func=lambda message: True)
def chat(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": message.text}]}]}
    try:
        r = requests.post(url, json=payload)
        ans = r.json()['candidates'][0]['content']['parts'][0]['text']
        bot.reply_to(message, ans)
    except:
        bot.reply_to(message, "Gemini responds: I am busy right now.")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
