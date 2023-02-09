import logging
import aiogram.utils.markdown as md
import asyncio
import logging
import sys
from asyncio import CancelledError, Future, Lock
from typing import Any, AsyncGenerator, Dict, List, Optional, Union
from aiogram import Bot, F, Router, html
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.exceptions import TelegramAPIError
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.methods.edit_message_text import EditMessageText
from aiogram.methods.edit_message_reply_markup import EditMessageReplyMarkup
from aiogram.methods.send_chat_action import SendChatAction
from aiogram.dispatcher.event.event import EventObserver
import os
from google_functions import *
from keyboard import *
import openai
import psycopg2
from urllib.parse import urlparse
import aioschedule
from connect_db import *
import json
from wishes import *
from pytz import timezone
import time
from classes_modified import *


async def send_main_menu_settings(message, state):
    if type(message) == types.Message:
        await message.answer_sticker("CAACAgIAAxkBAAEc7r1j4zwg8DSy3wnrdeWHSg5qA9N5KgACJhMAAujW4hIfQm23Xqw9ZC4E")
        inline_keyboard = await build_inline_keyboard(['Service Feedback', 'Wishes', 'Remind Me SF!', 'Remember Me!'])
        await message.answer('Welcome to /Name/ Bot!\n\n Please be patient with me!\nIf you feel like I\'m not listening to you, or want to get out of stuff, type /restart! \n\n If you have encountered any bugs, please inform my creator at @/name/!', reply_markup=inline_keyboard)
        await (state.set_state(State_menu.starting))
    elif type(message) == types.CallbackQuery:
        inline_keyboard = await build_inline_keyboard(['Service Feedback', 'Wishes', 'Remind Me SF!', 'Remember Me!'])
        await message.message.edit_text('Welcome to /Name/ Bot!\n\n Please be patient with me!\nIf you feel like I\'m not listening to you, or want to get out of stuff, type /restart! \n\nIf you have encountered any bugs, please inform my creator at @/name/!', reply_markup=inline_keyboard)
        await (state.set_state(State_menu.starting))


def main():
    pass


if __name__ == "__main__":
    main()
