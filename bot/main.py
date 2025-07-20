import os
import asyncio
from aiogram import Bot, Dispatcher, types

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Пример команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я эхо-бот на aiogram.")

# Эхо-обработчик
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Точка входа
async def main():
    print("Бот запускается...")
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()
        print("Бот остановлен.")

if __name__ == '__main__':
    asyncio.run(main())
