
'''
#for deployment
script_id = 'AKfycbylIxeQohmbDl2ZPXw1BI7ES0IytBx1KDaQ5vFNz3y1vpBkC-fBiSGpg8zKTG2l8fes'
assert (API_TOKEN := os.environ.get('TOKEN'))
assert (REDIS_URL := os.environ.get('REDIS_URL'))
assert (DATABASE_URL := os.environ.get('DATABASE_URL'))
storage = RedisStorage_custom.from_url(REDIS_URL)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)
openai.api_key = "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"
database_url = urlparse(DATABASE_URL)
conn = psycopg2.connect(
    host=database_url.hostname,
    user=database_url.username,
    password=database_url.password,
    port=database_url.port)
'''

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
from classes_modified import *


'''
#for deployment
script_id = ''
assert (API_TOKEN := os.environ.get('TOKEN'))
assert (REDIS_URL := os.environ.get('REDIS_URL'))
assert (DATABASE_URL := os.environ.get('DATABASE_URL'))
storage = RedisStorage_custom.from_url(REDIS_URL)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)
database_url = urlparse(DATABASE_URL)
conn = psycopg2.connect(
    host=database_url.hostname,
    user=database_url.username,
    password=database_url.password,
    port=database_url.port)
'''
#for testing
script_id = ''
API_TOKEN = ''
REDIS_URL = ''
DATABASE_URL = ""
storage = RedisStorage_custom.from_url(REDIS_URL)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)
database_url = urlparse(DATABASE_URL)
conn = psycopg2.connect(
    host=database_url.hostname,
    user=database_url.username,
    password=database_url.password,
    port=database_url.port)

def main():
    pass


if __name__ == "__main__":
    main()