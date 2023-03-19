import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("🛒Товар в наличии🛒", callback_data="Тут будет товар"),
            InlineKeyboardButton("✅Написать о покупке✅", callback_data="О покупке писать: @lun1337"),
        ],
        [InlineKeyboardButton("🤖Поддержка бота🤖", callback_data="Возникла проблема? Пиши @lun1337")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет! Выбери что хочешь посмотреть:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"{query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Используй /start чтобы узнать мои опции.")


def main() -> None:
    application = Application.builder().token("5993089249:AAE-9cN1OY_EEFX65XnQPicqx4k3c5elo10").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling()

if __name__ == "__main__":
    main()
