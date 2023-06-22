from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open(r"C:\Users\Simone\Documents\GitHub\3scuole fork\3Scuole\3Scuole-main\bot_telegram_3scuole\token.txt", "r") as f:
    TOKEN = f.read()
    #print("Il tuo token è ", TOKEN)
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /setlingua: scegli la lingua, choose the language
        /setlocation: metti il paese da dove vuoi cercare
        /settypepupr: metti se vuoi la scuola pubblica o privata
        /settypesc: metti che tipo di scuola vuoi. Es: asilo, elementari, ecc...
        /settypehs: metti il tipo di scuola secondaria che vuoi. Es: liceo classico, liceo lingustico, liceo delle scienze umane, ecc...
        /orientamento: rispondi a delle domande per capire che indirizzo di scuola superiore fa per te
        """)
async def lingua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scegli la lingua/choose the language:
        1 per italiano
        2 for english""")
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scegli il paese:
        1 Sona
        2 Villafranca
        3 Bussolengo
        4 Castelnuovo
        5 Lazise
        6 Mozzecane
        7 Pastrengo
        8 Sommacampagna
        9 Pescantina
        10 Valeggio
        11 Vigasio""")
async def pupr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scegli tra le seguenti:
        1 scuola pubblica
        2 scuola privata""")
async def sc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scegli il grado della scuola:
        1 Nido
        2 Materna
        3 Elementari
        4 Medie
        5 Superiori""")
async def hs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Scegli il tipo di scuola secondiaria:
        1 Liceo classico
        2 Liceo delle scienze umane
        3 Liceo linguistico
        4 Tecnico Industriale
        ecc...""")
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Domandeh""")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('setlingua', lingua))
    app.add_handler(CommandHandler('setlocation', paese))
    app.add_handler(CommandHandler('settypesc', sc))
    app.add_handler(CommandHandler('settypepupr', pupr))
    app.add_handler(CommandHandler('settypehs', hs))
    app.add_handler(CommandHandler('orientamento', quiz))
    app.run_polling()

if __name__=='__main__':
   main()
