from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
