from aiogram import types
from loader import dp


@dp.message_handler(text='старт')
async def command_hello(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}, я бот, который поможет найти машину на'+ 'https://cars.av.by/')
