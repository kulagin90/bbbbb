from aiogram import types
from loader import dp


@dp.message_handler(text='/start')
async def command_start(message:types.Message):
    await message.answer(f'Привет {message.from_user.full_name}, я бот, который поможет найти машину на'+ 'https://cars.av.by/')
    await message.answer('для поиска автомобиля введи его название')