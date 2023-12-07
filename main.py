from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import asyncio
from requests_crypto import get_bitcoin_price, get_eth_price

API_TOKEN=""

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
  kb = [
		[types.KeyboardButton(text="Bitcoin")],
  	[types.KeyboardButton(text="Etherium")]
	]
  keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите криптовалюту")
  await message.reply("Привет!\nЯ бот от Itgenio\nЯ помогу тебе узнать сколько стоит криптовалюта",
                      reply_markup=keyboard)


@dp.message(F.text.lower() == "bitcoin")
async def bitcoin_price(message: types.Message):
    price = get_bitcoin_price()
    await message.answer(f"Стоимость криптовалюты равна {price}")


@dp.message(F.text.lower() == "etherium")
async def eth_price(message: types.Message):
    price = get_eth_price()
    await message.answer(f"Стоимость криптовалюты равна {price}")


async def main():
  await dp.start_polling(bot)
  
if __name__ == '__main__':
  asyncio.run(main())