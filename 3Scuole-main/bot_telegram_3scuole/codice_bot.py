from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater, MessageHandler
from urllib.request import urlopen
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint
import time
import datetime
import json
# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open(r"C:\Users\Simone\Documents\GitHub\3scuole fork\3Scuole\3Scuole-main\bot_telegram_3scuole\token.txt", "r") as f:
    TOKEN = f.read()
    bot = telepot.Bot(TOKEN)
    #print("Il tuo token è ", TOKEN)

async def avvia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Il bot si è avviato! 
    Scrivi /help per tutti i comandi""")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /setlocation: metti il paese da dove vuoi cercare
        /settypepupr: metti se vuoi la scuola pubblica o privata
        /settypesc: metti che tipo di scuola vuoi. Es: asilo, elementari, ecc...
        /settypehs: metti il tipo di scuola secondaria che vuoi. Es: liceo classico, liceo lingustico, liceo delle scienze umane, ecc...
        /orientamento: rispondi a delle domande per capire che indirizzo di scuola superiore fa per te
        """)
"""
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Scegli il paese:
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
        11 Vigasio)
"""
async def paese(update: Update, context: ContextTypes.DEFAULT_TYPE):
    on_chat_message
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Bussolengo', callback_data='bussolengo'),
                     InlineKeyboardButton(text='Castelnuovo', callback_data='castelnuovo')],
                     [InlineKeyboardButton(text='Lazise', callback_data='lazise'),
                     InlineKeyboardButton(text='Mozzecane', callback_data='mozzecane')],
                     [InlineKeyboardButton(text='Pastrengo', callback_data='pastrengo'),
                     InlineKeyboardButton(text='Pescantina', callback_data='pescantina')],
                     [InlineKeyboardButton(text='Sommacampagna', callback_data='sommacampagna'),
                     InlineKeyboardButton(text='Sona', callback_data='sona')],
                     [InlineKeyboardButton(text='Valeggio', callback_data='valeggio'),
                     InlineKeyboardButton(text='Vigasio', callback_data='vigasio')],
                     [InlineKeyboardButton(text='Villafranca', callback_data='villafranca')]])
    bot.sendMessage(chat_id, 'Ciao, mi chiamo MonuVeronaBot!🤖 Ti aiuterò nella ricerca dei monumenti più interessanti dell\'ovest veronese!🧭\nScegli il comune tra l\'elenco:', reply_markup=keyboard)
def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)
  
    if query_data == 'bussolengo':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Bussolengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
    elif query_data == 'castelnuovo':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Castelnuovo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
    elif query_data == 'lazise':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Lazise!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
    elif query_data == 'mozzecane':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Mozzecane!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
      
    elif query_data == 'pastrengo':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pastrengo!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
    elif query_data == 'pescantina':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Pescantina!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
    elif query_data == 'sommacampagna':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sommacampagna!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
  
    elif query_data == 'sona':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Sona!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
    
    elif query_data == 'valeggio':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Valeggio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
 
    elif query_data == 'vigasio':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Vigasio!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
  
    elif query_data == 'villafranca':
        bot.sendMessage(chat_id, 'D\'accordo, hai scelto il comune di Villafrancaa!\nOra scegli il tipo di monumento che vorresti visitare tra l\'elenco:')
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
    app.add_handler(CommandHandler('start', avvia))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('setlocation', paese))
    app.add_handler(CommandHandler('settypesc', sc))
    app.add_handler(CommandHandler('settypepupr', pupr))
    app.add_handler(CommandHandler('settypehs', hs))
    app.add_handler(CommandHandler('orientamento', quiz))
    app.run_polling()

if __name__=='__main__':
   main()
