from telegram.ext import Updater, MessageHandler, Filters
import test

   
updater = Updater(token='664508254:AAGLGR1fz7_LOvU2Pal9_9CJuVm7IGi6Y_k' )
dispatcher = updater.dispatcher
updater.start_polling()


def handler(bot, update):
  text = update.message.text  
 
  chat_id = update.message.chat_id
  
 
  if  'start' in text:
    bot.sendMessage(chat_id=chat_id, text='매일매일 10개의 명언을 새로 들을 수 있습니다 명언을 들으시려면 "명언"으로 입력해주세요!')
  
  elif '안녕' in text:
      bot.sendMessage(chat_id=chat_id, text='안녕!')

  elif '명언' in text:
    bot.send_message(chat_id=chat_id, text= test.names[0] +'\n'+ test.talks[0] +'\n'+test.names[1] +'\n'+ test.talks[1] +'\n'+'\n'+test.names[2] +'\n'+ test.talks[2] +'\n'+'\n'+test.names[3] +'\n'+ test.talks[3] +'\n'+'\n'+test.names[4] +'\n'+ test.talks[4] +'\n'+'\n'+test.names[5] +'\n'+ test.talks[5] +'\n'+'\n'+test.names[6] +'\n'+ test.talks[6] +'\n'+'\n'+test.names[7] +'\n'+ test.talks[7] +'\n'+'\n'+test.names[8] +'\n'+ test.talks[8] +'\n'+'\n'+test.names[9] +'\n'+ test.talks[9] +'\n')

  else:
    bot.send_message(chat_id=chat_id, text='"start" 를 입력하셔서 다시 실행해주세요! ')
    
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)