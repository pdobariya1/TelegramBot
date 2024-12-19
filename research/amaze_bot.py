import os
import logging
import asyncio
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types


load_dotenv()
TELEGRAM_BOT_API = os.getenv("TELEGRAM_BOT_API")
# print(TELEGRAM_BOT_API)


# Configure logging
logging.basicConfig(level=logging.INFO)


# Dispatcher
dp = Dispatcher()


@dp.message(Command(commands=["start", "help"]))
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives message with `/start` OR `help` command
    """
    await message.answer("Hi\nI am Amaze Bot!\nPowered by Parth")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender
    
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Initialize Bot instance with default bot properties which will be passed to all API calls
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize bot
    bot = Bot(token=TELEGRAM_BOT_API)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())