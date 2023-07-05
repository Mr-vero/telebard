# !pip install bardapi 
# !pip install python-telegram-bot==12.8
import bardapi
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
import time


# Set your __Secure-1PSID value to key
token = 'YOUR_TELEGRAM_TOKEN'
token_bard = 'YOUR_BARD_TOKEN'

from telegram import Update

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, there 👋🏻!")

def answer(update, context):
    input_text = update.message.text

    # Show typing animation
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(2)  # Simulating some processing time

    # Perform API request and get the response
    response = bardapi.core.Bard(token_bard).get_answer(input_text)

    if 'content' in response:
        response_text = response['content']
    else:
        response_text = 'No response found.'

    # Send text response
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

    # Send code response if available
    if 'code' in response:
        code = response['code']
        if len(code) > 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"```{code}```")

    # Send up to 5 image responses if links are available
    if 'links' in response:
        links = response['links']
        image_count = 0
        for link in links:
            if link.endswith('.jpg') or link.endswith('.jpeg') or link.endswith('.png'):
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=link)
                image_count += 1
                if image_count >= 5:
                    break
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text=link)


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(Filters.text & ~Filters.command, answer)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(answer_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
