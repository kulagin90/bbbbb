# from aiogram import Bot, Dispatcher, types
#
# from aiogram.utils import executor
#
# # Создание переменной
# bot = Bot(token= '5462982520:AAEkbPtg8vnRTyxo0H7p4uDXgJjVIHgUg8I')
#
# # Создание диспетчера
# dp=Dispatcher (bot)
#
# # Создание улавливателя сообщений
#
# @dp.message_handler()
# async def get_message(message:types.Message):
#     # chad_id=types.Message.chat.id
#     chat_id=message.chat.id
#     text=message.text
#     # text='HAllo'
#     await bot.send_message(chat_id=chat_id, text=text)
#
# executor.start_polling(dp)