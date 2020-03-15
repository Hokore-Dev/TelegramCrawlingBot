
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import telegram

bot = telegram.Bot(token = '')

for i in bot.getUpdates():
    print(i.message)

#bot.sendMessage(chat_id= , text="test")