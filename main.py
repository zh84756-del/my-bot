import telebot
import requests

TOKEN = "8432274497:AAFwdhTRgczKQ-XfHlkkoGwUrQzS52Sy1Jo"
GEMINI_KEY = "AIzaSyDzU29LyJcexRu64Tf27Jbmkcu_da2fSmk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def chat(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": message.text}]}]}
    try:
        r = requests.post(url, json=payload)
        ans = r.json()['candidates'][0]['content']['parts'][0]['text']
        bot.reply_to(message, ans)
    except Exception as e:
        bot.reply_to(message, "ခဏလေးနော်... Gemini က အလုပ်များနေလို့ပါ။")

if __name__ == "__main__":
    bot.infinity_polling()
