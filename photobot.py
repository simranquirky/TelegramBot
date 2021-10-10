from telegram.ext import Updater, InlineQueryHandler, CommandHandler,  MessageHandler, Filters
import requests
import re

#---------------------------------------------------------------

#     FOR DOG IMAGES

#-------------------------------------------------------------------

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(update, context):
    print("reached dog")
    url = get_image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)

#-------------------------------------------------------------------------

#     FOR CAT IMAGES

#-------------------------------------------------------------------
def cat(update, context):
    print("reached cat")
    url1 = get_image_url1()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url1)

def get_url1():
    contents = requests.get('https://some-random-api.ml/img/cat').json()    
    url1 = contents['link']
    return url1

def get_image_url1():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url1 = get_url1()
        file_extension = re.search("([^.]*)$",url1).group(1).lower()
    return url1

#----------------------------------------------------------------------------

#     FOR PANDA IMAGES

#-------------------------------------------------------------------
def panda(update, context):
    print("reached panda")
    url2 = get_image_url2()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url2)

def get_url2():
    contents = requests.get('https://some-random-api.ml/img/panda').json()    
    url2 = contents['link']
    return url2

def get_image_url2():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url2 = get_url2()
        file_extension = re.search("([^.]*)$",url2).group(1).lower()
    return url2


#-----------------------------------------------------------------

#     FOR BIRB IMAGES

#-------------------------------------------------------------------
def birb(update, context):
    print("reached birb")
    url3 = get_image_url3()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url3)

def get_url3():
    contents = requests.get('https://some-random-api.ml/img/birb').json()    
    url3 = contents['link']
    return url3

def get_image_url3():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url3 = get_url3()
        file_extension = re.search("([^.]*)$",url3).group(1).lower()
    return url3


#-----------------------------------------------------------------

#     FOR MEME TEMPLATES

#-------------------------------------------------------------------
def meme(update, context):
    print("reached meme")
    url4 = get_image_url4()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url4)

def get_url4():
    contents = requests.get('https://some-random-api.ml/meme').json()    
    url4 = contents['image']
    return url4

def get_image_url4():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url4 = get_url4()
        file_extension = re.search("([^.]*)$",url4).group(1).lower()
    return url4


def start(update, context):
    print("conversation started")
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Bot Quirky welcomes you!")
    
    # on recieving /start command prints the message "Bot Quirky welcomes you!" on the telegram chat 
    # and prints "conversation started" message where the source code is running

def end(update, context):
    print("conversation ended")
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Bye! See you Again.")
    
    # on recieving /bye command prints the message "Bye! See you Again." on the telegram chat 
    # and prints "conversation ended" message where the source code is running
    

def unknown(update, context):
    print("retry")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Try another command.")
    
    # on recieving any unknown command prints the message "Sorry, I didn't understand that command. Try another command." on the telegram chat 
    # and prints "retry" message where the source code is running


def main():
    token='2097873912:AAEnxI65jpT3TRqup0vpamJgq6zB23faQh4'
    #replace the curly braces with your bot token
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    unknown_handler = MessageHandler(Filters.command, unknown)
    start_handler = CommandHandler('start', start)
    
    dispatcher.add_handler(CommandHandler('dog',dog))
    
    # handles the command /dog and on being called takes to function dog defined above
    
    dispatcher.add_handler(CommandHandler('cat',cat))
    
    # handles the command /cat and on being called takes to function cat defined above
    
    dispatcher.add_handler(CommandHandler('panda',panda))
    
    # handles the command /panda and on being called takes to function panda defined above
    
    dispatcher.add_handler(CommandHandler('birb',birb))
    
    # handles the command /birb and on being called takes to function birb defined above
    
    dispatcher.add_handler(CommandHandler('meme',meme))
    
    # handles the command /meme and on being called takes to function meme defined above
    
    
    dispatcher.add_handler(CommandHandler('bye',end))
    
    # handles the command /bye and on being called takes to function end defined above
    
    dispatcher.add_handler(start_handler)
    
    # handles the command /start and on being called takes to function start defined above
    
    dispatcher.add_handler(unknown_handler)
    
    # handles any command which is not listed and on being called takes to function unknown defined above
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
    # calls the main function if namespace is main

