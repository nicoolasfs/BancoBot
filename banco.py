import telegram                             # de la libreria telegram
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,Location
from telegram.ext import Updater, MessageHandler, Filters
from principal import *

class Bot:
    posicion = 0

    def __init__(self):
        self.datos = BancoBuilder() 
        self.updater = Updater("5361255801:AAFv_DNm3WWZLtGnF4MxE2l0tf1wsbfFdyo", use_context=True)
        # Despachador
        self.despachador = self.updater.dispatcher 
        self.despachador.add_handler(telegram.ext.CommandHandler("start", self.start))
        self.despachador.add_handler(telegram.ext.MessageHandler(Filters.text, self.mensajes))

    def start(self, update, context):
        global posicion 
        posicion = 0
        idChat = update.message.chat_id
        nombre = update.message.chat.first_name
        context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=idChat, text=f"Hola {nombre}, bienvenido al banco UdeC") # saludar


    def mensajes(self, update, context):
        global posicion
        mensaje = update.message.text
        idChat = update.message.chat_id
        if posicion == 0:
            context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
            context.bot.send_message(chat_id=idChat, text="Ingrese su numero de cuenta")
            posicion = 1
        elif posicion == 1:
            self.datos.set_numero_cuenta(int(mensaje))
            context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
            context.bot.send_message(chat_id=idChat, text="Ingrese su clave")
            posicion = 2
        elif posicion == 2:
            self.datos.set_codigo_seguridad(int(mensaje))
            context.bot.send_message(chat_id=idChat, parse_mode="HTML", text=f"<b>------MENÚ------</b> \n 1️⃣ Consulta tu saldo. \n 2️⃣ Retira dinero. \n 3️⃣ Deposita dinero")
            posicion = 20
        elif posicion == 20:
            if mensaje == "1":
                self.despachador.add_handler(telegram.ext.MessageHandler(Filters.text, self.consultar))
            elif mensaje == "2":
                context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
                context.bot.send_message(chat_id=idChat, text=f"Ingrese el monto a retirar")
                self.despachador.add_handler(telegram.ext.MessageHandler(Filters.text, self.retirar))
            elif mensaje == "3":
                self.despachador.add_handler(telegram.ext.MessageHandler(Filters.text, self.depositar))
            else:
                context.bot.send_message(chat_id=idChat, text=f"Opción inválida")
                posicion = 0
        
    def consultar(self, update, context):
        global posicion
        idChat = update.message.chat_id
        context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=idChat, text= {self.datos.build().consultar()})
        posicion = 2
    
    def retirar(self, update, context):
        global posicion
        idChat = update.message.chat_id
        context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=idChat, text= {self.datos.build().retirar_dinero(float(update.message.text))})
        posicion = 2
    
    def depositar(self, update, context):
        global posicion
        idChat = update.message.chat_id
        context.bot.send_chat_action(chat_id=idChat, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=idChat, text= {self.datos.build().depositar_dinero(float(update.message.text))})
        posicion = 2

    def startBot(self):
        self.updater.start_polling()
        self.updater.idle()

def main():
    bot.startBot()

    while True:
        pass

bot = Bot()

if __name__ == "__main__":
    main()