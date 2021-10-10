## Starting with ‘WHAT IS BOT’?
Bots are basically software applications that runs automated tasks or scripts over the internet.
## ‘WHAT IS TELEGRAM BOT’?
Telegram bots are telegram accounts operated by softwares or scripts rather than humans. They can do a variety of things, ranging from playing music, displaying pictures, news broadcasts, reminders, notifications and a lot more.

  
 Python libraries and modules we need to import and why:

1. Python-telegram-bot

This library provides a pure Python interface for the Telegram Bot API. It’s compatible with Python versions 3.6.8+.
  
2. Requests

The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
  
3. Re

A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

  Now let’s start with the process

### 1. Register our new bot in BotFather
If you want to make a bot in Telegram, you have to “register” your bot first. When we “register” our bot, we will get the token to access the Telegram API.
Botfather rules all other bots in Telegram.
- Type the command ‘/newbot’ to start creating your bot.
- Give justified name to your bot.
- Safely keep the token recieved.
  
###   2. Setting up the environment
`yum install python3`

`pip3 install python-telegram-bot`

`pip3 install requests`

Since we are going to write our code in Python, so the above packages needs to be installed.
### 3. Importing modules
`from telegram.ext import Updater, InlineQueryHandler, CommandHandler,  MessageHandler, Filters`

`import requests`

`import re`

The necessity of these modules have been discussed above
### 4. Creating functions for displaying images
` 
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
      
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)`
      
Using the requests library, we can access the API and get the json data.
      
`contents = requests.get('https://random.dog/woof.json').json()`
      
Get the image URL since we need that parameter to be able to send the image.
      
`image_url = contents['url']`

Wrap this code into a function called get_url() .
      
`def get_url():

    contents = requests.get('https://random.dog/woof.json').json()    
      
    url = contents['url']
    
    return url`
    
To send a message/image we need two parameters, the image URL and the recipient’s ID — this can be group ID or user ID.
      
We can get the image URL by calling our get_url() function.
      
`url = get_url()`

Get the recipient’s ID using this code:

`chat_id = update.message.chat_id`

After we get the image URL and the recipient’s ID, it’s time to send the message, which is an image.
  
`bot.send_photo(chat_id=chat_id, photo=url)`
  
Wrap that code in a function called dog, and make sure your code looks like this:

` def dog( update, context ):

    url = get_url()
      
    chat_id = update.message.chat_id
    
    bot.send_photo(chat_id=chat_id, photo=url)`
    
The above piece of code was for displaying random images of dog.
  
Similarly, by just changing the api /url we can get access to images of cats, pandas, birb etc.
