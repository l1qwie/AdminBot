from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.utils.markdown import hlink
from aiogram.types import BufferedInputFile
import database
from admin import EvPrevMsgId, DispatchPhrase, RetainPrevMsgId
import admin

TOKEN = "5841486224:AAFf3GSIIZIVYxnsXD31Hvy3nPJWdvzZxwo"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

def Namer(name: str, nick: str) -> str:
    return hlink(name, nick)



@router.message()
async def all_mes(message: types.Message):
    database.ConnectTo("..\\bot(for_all)\\database.db")
    if message.text == '/reset':
        database.ResetAll(message.from_user.id)
    await VecMess(message)

async def VecMess(message: types.Message):
    database.ConnectTo("..\\bot(for_all)\\database.db")
    admin.namer = Namer
    prev = EvPrevMsgId(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)    # Evaluate Previous Message ID
    if prev != None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=prev)
    (text, kbd, prmode, halt, spreadsheet, fixed) = DispatchPhrase(message.from_user.id, message.text)
    if spreadsheet is None:
        reply = await bot.send_message(message.from_user.id, text=text, reply_markup=kbd, parse_mode=prmode)
        if fixed is not None:
            await bot.pin_chat_message(message.from_user.id, message_id=reply.message_id)
            RetainPrevMsgId(message.from_user.id, None)
        else:
            RetainPrevMsgId(message.from_user.id, reply.message_id)
    else:
        if text is None:
            reply = await bot.send_document(message.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), reply_markup=kbd)
        else:
            print("ну тут я, тут")
            reply = await bot.send_document(message.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), caption=text, reply_markup=kbd)
        RetainPrevMsgId(message.from_user.id, reply.message_id)
        

@router.callback_query()
async def VecCallBack(query: types.CallbackQuery):
    database.ConnectTo("..\\bot(for_all)\\database.db")
    admin.namer = Namer
    prev = EvPrevMsgId(query.from_user.id, query.from_user.first_name, query.from_user.last_name, query.from_user.username)    # Evaluate Previous Message ID
    if prev != None:
        await bot.delete_message(chat_id=query.from_user.id, message_id=prev)
    print(query.data)
    (text, kbd, prmode, halt, spreadsheet, fixed) = DispatchPhrase(query.from_user.id, query.data)
    print(text, spreadsheet)
    if spreadsheet is None:
        reply = await bot.send_message(query.from_user.id, text=text, reply_markup=kbd, parse_mode=prmode)
        if fixed is not None:
            await bot.pin_chat_message(query.from_user.id, message_id=reply.message_id)
            RetainPrevMsgId(query.from_user.id, None)
        else:
            RetainPrevMsgId(query.from_user.id, reply.message_id)
    else:
        if text is None:
            reply = await bot.send_document(query.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), reply_markup=kbd)
        else:
            print("ну тут я, тут")
            reply = await bot.send_document(query.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), caption=text, reply_markup=kbd)
        RetainPrevMsgId(query.from_user.id, reply.message_id)


async def main():
    print("Запустился")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print("...")
    asyncio.run(main())