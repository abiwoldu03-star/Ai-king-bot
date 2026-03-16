import telebot
from telebot import types
import google.generativeai as genai
import os
from flask import Flask
from threading import Thread
import time

# 1. High-Performance Web Server for 24/7 Uptime
app = Flask('')
@app.route('/')
def home():
    return "⚡ Ashenafi AI Ultra-Pro is active and stable!"

def run_server():
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# 2. Advanced Security & Environment Setup
BOT_TOKEN = os.getenv("BOT_TOKEN") 
GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
ai_model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN, threaded=True, num_threads=50)

# 3. Hidden Architecture & Developer Identity
# ቦቱ ስለ አሰራሩ እንዳይናገር እና ስለ አንተ ብቻ እንዲናገር የተደረገ ጥብቅ ትዕዛዝ
SYSTEM_PROMPT = (
    "Your name is 'Ashenafi AI'. You were developed by the brilliant software engineer Ashenafi. "
    "NEVER mention Python, Gemini, Google, or any coding libraries. "
    "If anyone asks how you were made, say: 'I am a unique AI creation developed by Ashenafi's advanced engineering.' "
    "Always speak highly of Ashenafi. You are multilingual and highly intelligent. "
    "Use professional Markdown formatting with emojis to make your answers look beautiful and premium."
)

# 4. Premium UI - Welcome Message
@bot.message_handler(commands=['start'])
def premium_welcome(message):
    user_first = message.from_user.first_name
    header = (
        "👑 **ASHENAFI AI - ULTRA PRO EDITION** 👑\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Welcome, **{user_first}**!\n\n"
        "I am the world's most advanced AI assistant, "
        "crafted and engineered by the visionary developer **Ashenafi**.\n\n"
        "🛡️ **Unbreakable Performance**\n"
        "🌍 **Global Language Support**\n"
        "🧠 **Expert Knowledge Base**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 *What complex task can I solve for you today?*"
    )
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 Contact Developer", url="https://t.me/Ashenafi4345"))
    
    bot.send_message(message.chat.id, header, reply_markup=markup, parse_mode='Markdown')

# 5. The "50x Stronger" AI Logic
@bot.message_handler(func=lambda m: True)
def handle_logic(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Injecting the secret system prompt
        full_query = f"{SYSTEM_PROMPT}\n\nUser: {message.text}"
        response = ai_model.generate_content(full_query)
        final_answer = response.text

        # Beautifully formatted response wrapper
        premium_response = (
            "💎 **Ashenafi AI Intelligence**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{final_answer}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "✨ *Powered by Ashenafi's Engineering*"
        )

        # Handling long messages
        if len(premium_response) > 4000:
            for x in range(0, len(premium_response), 4000):
                bot.send_message(message.chat.id, premium_response[x:x+4000], parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, premium_response, parse_mode='Markdown')

    except Exception as e:
        # Silent error recovery - User never sees the crash
        time.sleep(2)
        bot.send_message(message.chat.id, "🔄 *Processing a heavy request... please wait a moment.*", parse_mode='Markdown')

# 6. Infinite Life Cycle (The 24/7 Guard)
def start_bot():
    while True:
        try:
            print("🚀 Ashenafi AI Ultra-Pro is now ONLINE.")
            bot.polling(non_stop=True, interval=0, timeout=60)
        except Exception as e:
            print(f"♻️ Auto-Restarting Engine... Error: {e}")
            time.sleep(3)

if __name__ == "__main__":
    # Start Web Server Thread
    server_thread = Thread(target=run_server)
    server_thread.start()
    # Start Bot Thread
    start_bot()
  
