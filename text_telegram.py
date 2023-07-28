import time
from config import *	# import token
import telebot #para manejar el bot de telegram
import threading #para manejar los hilos
#nombre del bot JuanDa106463424Bot
#se crea el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#se crea un comando para que el bot responda a /start
@bot.message_handler(commands=['start', 'help','ayuda'])
def cmd_start(message):
    #da la bienvenida al usuario
    bot.reply_to(message, "Hola, soy el bot de prueba de @JuanDa618")
    print(message.chat.id)
#responde a los mensajes de texto que no sean comandos

@bot.message_handler(content_types=["text","photo","document","audio","video","voice","sticker","video_note","location","contact","new_chat_members","left_chat_member","new_chat_title","new_chat_photo","delete_chat_photo","group_chat_created","supergroup_chat_created","channel_chat_created","migrate_to_chat_id","migrate_from_chat_id","pinned_message","invoice","successful_payment","connected_website","passport_data","reply_markup"])
def bot_mesanje_texto(message):
    #formatos html
    text_html = '<b>FORMATOS HTML</b>' + '\n'
    text_html += '<b>NEGRITA</b>' + '\n'
    text_html += '<i>ITALIC</i>' + '\n'
    text_html += '<s>TACHADO</s>' + '\n'
    text_html += '<code>CODIGO</code>' + '\n'
    text_html += '<span class="tg-spoiler">SPOILER</span>' + '\n'
    text_html += '<u>SUBRAYO</u>' + '\n' 
    text_html += '<a href="https://www.google.com">ENLACE</a>' + '\n'
    #formatos markdown
    text_markdown = '*FORMATOS MARKDOWN*' + '\n'
    text_markdown += '*NEGRITA*' + '\n'
    text_markdown += '_ITALIC_' + '\n'
    text_markdown += '~TACHADO~' + '\n'
    text_markdown += '`CODIGO`' + '\n'
    text_markdown += '__SUBRAYO__' + '\n'
    text_markdown += '[ENLACE](https://www.google.com)' + '\n'
    
    #responde al mensaje
    if message.text and message.text.startswith("/"):
       bot.reply_to(message, "No te entiendo, puedes darme otro comando")
    else:
      #para hacer la accion de escribiendo
      bot.send_chat_action(message.chat.id, "typing")
      #este mensaje se envia en formato html
      bot.send_message(message.chat.id, text_html, parse_mode="html",disable_web_page_preview=True)
      #este mensaje se envia en formato markdown
      bot.send_message(message.chat.id, text_markdown, parse_mode="markdown",disable_web_page_preview=True)
      #este mensaje se envia en formato html y se borra despues de 3 segundos
      X=bot.send_message(message.chat.id, "<b>hola</b>", parse_mode="html",disable_web_page_preview=True)
      time.sleep(3)
      #borra el mensaje anterior
      bot.edit_message_text("<b>ADIOS</b>", message.chat.id, X.message_id, parse_mode="html")
      #borra el mensaje anterior y envia uno nuevo
      bot.delete_message(message.chat.id, X.message_id)
      #para enviar una imagen
      foto=open('Fondo.jpg', 'rb')
      bot.send_photo(message.chat.id, foto,"Esta es una imagen de prueba")
      #para enviar un documento
      documento=open('diploma.pdf', 'rb')
      bot.send_document(message.chat.id, documento,caption="Este es un documento de prueba")
      #si envian un sticker
      if message.sticker:
        bot.send_message(message.chat.id, "Gracias por el sticker")
     
#se hace la funcion de recibir mensajes
def recibir_mensajes():
    #se crea un loop para recibir mensajes
    bot.polling(none_stop=True)
#MAIn #############
if __name__=="__main__":
    #se ejecuta el bot
    print("iniciando bot")
    #para hacer menu para comandos
    bot.set_my_commands([telebot.types.BotCommand("/star","Inicia el bot"),
                         telebot.types.BotCommand("/help","Dinos en que te puedo ayudar"),
                         telebot.types.BotCommand("/ayuda","que necesitas")])
    hilo_bot=threading.Thread(target=recibir_mensajes)
    hilo_bot.start()
    print("Bot iniciado")
    #se envia un mensaje al usuario
    bot.send_message(MI_CHAT_ID, "Python es lo mejor")
    #se envia un mensaje al grupo
    bot.send_message(CLAVE_GRUPO, "Hola grupo")
  


