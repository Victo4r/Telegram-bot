import asyncio
from pyrogram import Client, filters

async def message_handler(client_obj, message_obj, text):
    print("Сообщение получили, ждем 4 сек ...")
    await asyncio.sleep(4)
    await client_obj.read_history(message_obj.chat.id)
    print("Прочитали сообщения пользователя...")
    print("Имитируем ввод сообщения...")
    await asyncio.sleep(6)
    await client_obj.send_chat_action(message_obj.chat.id, "typing")
    await asyncio.sleep(1)
    await client_obj.send_message(message_obj.chat.id, text)
    print("Ответили пользователю..")

@Client.on_message(filters.text)
async def text_handler(client, message):
    print("Пользователь отправил текст: '{}'".format(message.text))
    await message_handler(client, message, "text")

@Client.on_message(filters.sticker)
async def sticker_handler(client, message):
    print("Пользователь отправил стикер: '{}'".format(message.text))
    await message_handler(client, message, "sticker")