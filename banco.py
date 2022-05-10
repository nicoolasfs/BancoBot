from turtle import position
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Location, Update
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "5361255801:AAFv_DNm3WWZLtGnF4MxE2l0tf1wsbfFdyo"
updater = Updater(TOKEN, use_context=True)
#class Bot:
    
def start(update, context):
    idChat = update.message.chat_id
    context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=idChat, text=f"Hola {update.message.chat.first_name}, bienvenido al banco UdeC")
    context.bot.send_message(chat_id=idChat, parse_mode="HTML", text=f"<b>-----MENÚ-----</b> \n 1️⃣ Consulta tu saldo. \n 2️⃣ Retira dinero. \n 3️⃣ Deposita dinero")
def mensajes(update, context):
    mensaje= update.message.text
    idChat = update.message.chat_id
    despachador= updater.dispatcher
    if(mensaje=="1"):
        despachador.add_handler(telegram.ext.MessageHandler(Filters.text, consultar))
        despachador.add_handler(telegram.ext.CommandHandler("start", start))
    elif (mensaje=="2"):
        despachador.add_handler(telegram.ext.MessageHandler(Filters.text, retira))
        despachador.add_handler(telegram.ext.CommandHandler("start", start))
    elif (mensaje=="3"):
        despachador.add_handler(telegram.ext.MessageHandler(Filters.text, deposita))
        despachador.add_handler(telegram.ext.CommandHandler("start", start))
    else: context.bot.send_message(chat_id=idChat, text=f"Opción inválida")
    print(mensaje)
def consultar(update, context):
    pass
def retira(update, context):
    pass
def deposita(update, context):
    pass
def main():
    despachador= updater.dispatcher
    despachador.add_handler(telegram.ext.CommandHandler("start", start))
    despachador.add_handler(telegram.ext.MessageHandler(Filters.text, mensajes))
   # despachador.add_handler(telegram.ext.MessageHandler(Filters.location, posicion))

    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()