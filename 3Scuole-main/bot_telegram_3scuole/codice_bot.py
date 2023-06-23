import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def avvia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Il bot si è avviato! 
    Scrivi /help per tutti i comandi""")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /setlocation: metti il paese da dove vuoi cercare
        /settypepupr: metti se vuoi la scuola pubblica o privata
        /settypesc: metti che tipo di scuola vuoi. Es: asilo, elementari, ecc...
        /settypehs: metti il tipo di scuola secondaria che vuoi. Es: liceo classico, liceo lingustico, liceo delle scienze umane, ecc...
        /disabilita: scuole con l'aiuto disabilità
        """)
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Sona", callback_data="1"),
            InlineKeyboardButton("Villafranca", callback_data="2")],
            [InlineKeyboardButton("Bussolengo", callback_data="3"),
            InlineKeyboardButton("Castelnuovo", callback_data="4")],
            [InlineKeyboardButton("Lazise", callback_data="5"),
            InlineKeyboardButton("Mozzecane", callback_data="6")],
            [InlineKeyboardButton("Pastrengo", callback_data="7"),
            InlineKeyboardButton("Pescantina", callback_data="8")],
            [InlineKeyboardButton("Sommacampagna", callback_data="9"),
            InlineKeyboardButton("Valeggio", callback_data="10")],
            [InlineKeyboardButton("Vigasio", callback_data="11")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Per favore scegli il paese:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Hai selezionato: {query.data}")

async def pupr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Pubblica", callback_data="1"),
            InlineKeyboardButton("Privata", callback_data="2"),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Scegli il tipo di scuola:", reply_markup=reply_markup)
async def sc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Nido", callback_data="1"),
            InlineKeyboardButton("Materna", callback_data="2")],
            [InlineKeyboardButton("Elementari", callback_data="3"),
            InlineKeyboardButton("Medie", callback_data="4")],
        [InlineKeyboardButton("Superiori", callback_data="5")]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Scegli il tipo di scuola:", reply_markup=reply_markup)
async def hs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Linguistico", callback_data="Linguistico"),
            InlineKeyboardButton("Classico", callback_data="Classico")],
            [InlineKeyboardButton("Scientifico", callback_data="Scientifico"),
            InlineKeyboardButton("Scienze applicate", callback_data="Scienze_applicate")],
            [InlineKeyboardButton("Scienze umane", callback_data="Scienze_umane"),
            InlineKeyboardButton("Economico sociale", callback_data="Economico_sociale")],
            [InlineKeyboardButton("Artistico", callback_data="Artistico"),
            InlineKeyboardButton("Telecomunicazioni", callback_data="Telecomunicazioni")],
            [InlineKeyboardButton("Automazione", callback_data="Automazione"),
            InlineKeyboardButton("Informatica", callback_data="Informatica")],
            [InlineKeyboardButton("ITI 4 Anni", callback_data="ITI_4_Anni"),
            InlineKeyboardButton("Turistico", callback_data="Turistico")],
            [InlineKeyboardButton("Web Community", callback_data="Web_Community"),
            InlineKeyboardButton("Finanza e Marketing", callback_data="Finanza_e_Marketing")],
            [InlineKeyboardButton("Relazioni per il Marketing", callback_data="Relazioni_per_il_Marketing"),
            InlineKeyboardButton("Tustico Sportivo", callback_data="Tustico_Sportivo")],
            [InlineKeyboardButton("Sistemi Aziendali", callback_data="Sistemi_Aziendali"),
            InlineKeyboardButton("Agrario", callback_data="Agrario")],
            [InlineKeyboardButton("Alberghiero", callback_data="Alberghiero"),
            InlineKeyboardButton("CFP", callback_data="CFP")],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Scegli l'indirizzo:", reply_markup=reply_markup)
async def di(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scuole con aiuto disabilità""")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6168563285:AAEULVLbJoXDZk8NHQ35AUdFnaKEY0b-nMY").build()

    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler('start', avvia))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('setlocation', paese))
    application.add_handler(CommandHandler('settypesc', sc))
    application.add_handler(CommandHandler('settypepupr', pupr))
    application.add_handler(CommandHandler('settypehs', hs))
    application.add_handler(CommandHandler('disabilita', di))
    #application.add_handler(CommandHandler('orientamento', quiz))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()