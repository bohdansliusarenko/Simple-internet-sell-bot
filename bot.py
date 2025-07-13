import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

mytoken = open('telegram_token.txt', 'r').read().strip()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "telegram_bot", "files", "product.pdf")

code_to_file = {
    "ABC123": file_path,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Please send your payment code.")

async def handle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    if code in code_to_file:
        with open(code_to_file[code], 'rb') as f:
            await update.message.reply_document(f)
    else:
        await update.message.reply_text("Invalid code. Please check and try again.")

app = ApplicationBuilder().token(mytoken).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_code))
app.run_polling()