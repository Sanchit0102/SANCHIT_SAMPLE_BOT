#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '6362281925:AAGSTs25eytppfuN-AF-IMKCtxrvtxhXWJ8'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.effective_user.first_name}! Welcome to File Rename Bot. Send me a file to rename.")

def rename_file(update, context):
    file_id = update.message.document.file_id
    new_file_name = update.message.document.file_name

    # Download the file
    file_path = os.path.join('downloads', file_id)
    context.bot.get_file(file_id).download(file_path)

    # Rename the file
    renamed_file_path = os.path.join('downloads', new_file_name)
    os.rename(file_path, renamed_file_path)

    # Reply with the renamed file
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(renamed_file_path, 'rb'))

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    rename_handler = MessageHandler(Filters.document, rename_file)
    dispatcher.add_handler(rename_handler)

    error_handler = MessageHandler(Filters.all, error)
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
