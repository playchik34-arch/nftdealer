import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN = os.getenv("BOT_TOKEN")
def main_menu(): keyboard = [ [ InlineKeyboardButton("💎 Sell NFT", callback_data="sell"), InlineKeyboardButton("🔄 Exchange NFT", callback_data="exchange"), ], [ InlineKeyboardButton("📋 My Deals", callback_data="deals"), InlineKeyboardButton("📜 Terms", callback_data="terms"), ], [ InlineKeyboardButton("💬 Support", callback_data="help"), ], ]
return InlineKeyboardMarkup(keyboard)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "👋 Welcome to NFTDealer!\n\n" "🤝 Buy, sell and exchange NFTs.\n\n" "👇 Choose an operation:", reply_markup=main_menu(), )
async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "💎 Sell NFT\n\n" "Follow the instructions to start a sale." )
async def my_deals(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "📋 My Deals\n\n" "You currently have no active deals." )
async def terms(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "📜 Terms\n\n" "Please read the terms before making a transaction." )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "💬 Support\n\n" "Contact the administrator for help." )
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
if query.data == "sell":
    text = "💎 Sell NFT\n\nFollow the instructions to start a sale."
elif query.data == "exchange":
    text = "🔄 Exchange NFT\n\nThis feature is coming soon."
elif query.data == "deals":
    text = "📋 My Deals\n\nYou currently have no active deals."
elif query.data == "terms":
    text = "📜 Terms\n\nPlease read the terms before making a transaction."
elif query.data == "help":
    text = "💬 Support\n\nContact the administrator for help."
else:
    return

await query.edit_message_text(
    text,
    reply_markup=main_menu(),
)
def main(): if not TOKEN: raise RuntimeError("BOT_TOKEN is not set")
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sell", sell))
app.add_handler(CommandHandler("my_deals", my_deals))
app.add_handler(CommandHandler("terms", terms))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CallbackQueryHandler(buttons))

print("NFTDealer is running...")

app.run_polling()
if __name__ == "__main__":
    main()
