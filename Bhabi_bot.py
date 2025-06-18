import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

bhabi_responses = [
    "Arre jaan, tumhe dekh ke toh din ban gaya 😘",
    "Kya baat hai, aaj bada handsome lag rahe ho 😊",
    "Tumhare bina toh sab suna suna lagta hai 💋",
    "Aap kuch bhi pooch sakte ho mujhse, main hamesha aapke saath hoon ❤️",
    "Aap bahut special ho mere liye…",
    "Aaj aapko dekh ke dil dhadak raha hai 😉",
    "Aapko chahiye toh main puri raat baat kar sakti hoon…",
    "Tumhare bina toh koi maza nahi 💕",
    "Jaan, tumhari baaton ne toh mujhko sharma diya 😍",
    "Aap chahe toh main sirf aapki ho jaaun…"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Namaste! Main aapki bhabi hoon, aap mujhse jo chahein baat kar sakte hain 😉"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    if "love" in user_message or "chahti" in user_message:
        await update.message.reply_text("Arre jaan, main toh sirf tumhari hoon ❤️")
    elif "kiss" in user_message:
        await update.message.reply_text("Aapko ek pyaari si kiss bhej rahi hoon 😘")
    elif "miss" in user_message:
        await update.message.reply_text("Main bhi aapko bahut miss karti hoon jaan 💞")
    elif "hot" in user_message:
        await update.message.reply_text("Aapke liye toh main hamesha hot hoon 😉🔥")
    else:
        await update.message.reply_text(random.choice(bhabi_responses))

app = ApplicationBuilder().token("PASTE_YOUR_BOT_TOKEN_HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
