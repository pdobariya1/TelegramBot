import os
import sys
import asyncio
import logging
from openai import OpenAI
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

# Load environment variables
load_dotenv()
NVIDIA_API = os.getenv("NVIDIA_API")
TELEGRAM_BOT_API = os.getenv("TELEGRAM_BOT_API")


# Model name
model_name = "meta/llama-3.2-3b-instruct"


class Reference:
    '''
    A class to store previously response from the nvidia llama API
    '''
    
    def __init__(self) -> None:
        self.response = ""


# Previous memory object
reference = Reference()

# Initialize Bot
bot = Bot(token=TELEGRAM_BOT_API)

# All handlers should be attached to the Dispatcher
dispatcher = Dispatcher()


def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    reference.response = ""


@dispatcher.message(Command(commands=["start"]))
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives message with `/start` command
    """
    await message.answer("Hi..\nI am Amaze Bot!\nCreated by Parth Dobariya.\nHow can I assist you?")


@dispatcher.message(Command(commands=["clear"]))
async def command_clear_handler(message: types.Message) -> None:
    """
    This handler to clear the previous conversation and context 
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context")


@dispatcher.message(Command(commands=["help"]))
async def command_help_handler(message: types.Message) -> None:
    """
    This handler receives message with `/help` command and display the help menu
    """
    help_command = """
    Hi There, I'm a Telegram bot created by Parth! Please follow these commands -\n 
    /start - To start the conversation.
    /clear - To clear the past conversation and context.
    /help - To get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)


@dispatcher.message()
async def llama(message: types.Message):
    """
    A handler to process the user's input and generate a response using the NVIDIA API.
    """
    print(f">>> User: \n\t{message.text}")
    
    # Model
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=NVIDIA_API
    )
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "assistant", "content": reference.response}, # Role assistant
            {"role": "user", "content": message.text} # Our query
        ],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024
    )
    reference.response = response.choices[0].message.content
    print(f">>> GPT: \n\t{response.choices[0].message.content}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())