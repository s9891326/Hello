# 匯入相關套件
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# 設定 token
token = '5059538751:AAEo8NJ9gFcfZ5Tgl0KjDFRDMKAxJmrMZR8'

# 初始化bot
updater = Updater(token=token)

dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text('hello, {}'.format(update.message.from_user.first_name))

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
