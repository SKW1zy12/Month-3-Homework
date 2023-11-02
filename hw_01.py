# Наши импорты
import random
from aiogram import Bot, Dispatcher, types
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = random.randint(1, 3)
    await message.reply("Я загадал число от 1 до 3. Попробуйте угадать!")

@dp.message_handler(lambda message: message.text.isdigit())
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    user_guess = int(message.text)
    
    if user_id in user_data:
        correct_number = user_data[user_id]
        
        if user_guess == correct_number:
            await message.reply("Правильно, вы угадали!")
            await message.reply_photo(photo="https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
        else:
            await message.reply(f"Извините, вы не угадали. Я загадал число {correct_number}.")
            await message.reply_photo(photo="https://media.makeameme.org/created/sorry-you-lose.jpg")

user_data = {}

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
