from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8601307163:AAF6NEFdC9IQHyrDJD04Y58U_B1QYzyoJww"

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url = "https://i.imgur.com/xxxxxxx.jpg"  # 🔥 remplace par ton image

    keyboard = [
        [InlineKeyboardButton("🚀 Commencer", callback_data="start")],
        [InlineKeyboardButton("📜 Menu", callback_data="menu")],
        [InlineKeyboardButton("👑 VIP", callback_data="vip")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=image_url,
        caption="🔥 Bienvenue sur LORD_ADKIS🚫\nBientôt disponible ⚡",
        reply_markup=reply_markup
    )

# ---------- BUTTONS ----------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start":
        await query.edit_message_caption("🚀 Bienvenue dans le système LORD ADKIS")
    elif query.data == "menu":
        await query.edit_message_caption("📜 Menu en construction ⚡")
    elif query.data == "vip":
        await query.edit_message_caption("👑 Zone VIP bientôt disponible 🔒")

# ---------- BOT SETUP ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("🔥 Bot en ligne...")
app.run_polling(poll_interval=1)