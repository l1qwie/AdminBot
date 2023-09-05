import logging
import datetime
from aiogram.utils.markdown import hlink
from aiogram import Bot, Dispatcher, Router, types
import asyncio
from dbad import DataBase
import keyboards as nav
import re

TOKEN = "5841486224:AAFf3GSIIZIVYxnsXD31Hvy3nPJWdvzZxwo"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
db = DataBase("..\\bot(for_all)\database.db")

countKeyboards = [nav.whoreg, nav.mainGames, nav.inkb, nav.inkbtime]

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekDRus = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


# Порядок действий:
# 1. Првоерка точно ли это админ пользуется ботом
# 2. Выбор действия: 1)сделать расписание(дополнить) 2) посмотреть кто записался
# 1)
#   1. Выбор игры
#   2. Ввод даты
#   3. Ввод времени
#   4. Ввод кол-ва мест

#Начало

class Client:
    id: int
    level: int
    name: str

class NewDate:
    game: str
    lvl: int
    date: str
    game: str
    time: str
    seats: int
    payment: str

class WhoReg:
    game: str
    date: str
    time: str


def RetrieveClient (id: int) -> Client:
    res = Client()
    res.id = id
    #прочитать данные из бд, так чтобы все поля Client были заполнены
    db.RetrieveClient()
    return res

def IsPriviledged (cl: Client) -> bool:
    return False

def Retain(c: Client):
    # Сохраняет состояние клиента в базу данных

def DoVectorMes (msg: str, uid: int) -> [str]: #
    text = message.text
    cl = RetrieveClient(uid)
    if cl.level == 3:

    if message.text == '/start':
        start_comm(message)
    elif message.text == 'Узнать кто записался' or message.text == 'Настроить расписание' or message.text == 'Записать нового пользователя':
        await choice_direction(message)
    elif message.text == '/filled':
        await startwhoreg(message)
    elif message.text == '/schedule':
        await schedule_comm(message)
    elif message.text == '/newuser':
        await add_new_user(message)
    elif re.match(r"\d{1,2}-\d{1,2}-\d{4}", message.text):
        await dat(message, text, True)
    elif re.findall(r'\d{1,2}:\d{2}', message.text):
        await added_times(message, text, True)
    elif re.findall(r"\d{2}|\d{1}", message.text):
        if examination_schedule("users_from_admin", 5) == True:
            await num_of_seats(message, True)
        elif examination_schedule("users_from_admin", 7) == True:
            await num_phone(message, text)
        elif examination_schedule("users_from_admin", 8) == True:
            await end_new_us(message, text)
    elif message.text == 'Следующий шаг' or message.text == 'Назад':
        await step(message)
    elif re.match(r'^[A-Za-zА-Яа-я\s-]+$', message.text):
        await name(message, text, True)
    elif message.text == '💷 Наличные' or message.text == '💳 Перевод':
        await paymen_ad_us(message, text)
    else:
        await bot.send_message(message.from_user.id, text="ZzZzZzZzZzZ")

@router.message()
async def vector_mes(message: types.Message):
    responses = DoVectorMes(message.text, message.from_user.id)
    i = 0
    while 
        bot.send_message(message.from_user.id, text=response)

def test1():
    DoVectorMes('/start')
    ...
    DoVectorMes(12)
    ..


@router.callback_query()
async def vector_call(query: types.CallbackQuery):
    if query.data == "volleyball" or query.data == "football":
        text = query.data
        await call_back_games2(query, text, True)
    elif query.data[0] == "*":
        ch = query.data[1:] 
        await click_date(query, ch, True)
    elif query.data[0] == "9":
        ch = query.data[1:]
        await ckick_time(query, ch, True)
    elif query.data == "yes" or query.data == "no":
        await del_game(query)
    

async def start_comm(message: types.Message):
    if message.from_user.id == 738070596 or message.from_user.id == 1051812255:
        await bot.send_message(message.from_user.id, text="Привет! Ты как раз тот, кто мне нуджен) Покажу тебе всю информацию которая у меня есть по твоему желанию", reply_markup=countKeyboards[0])
        await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")    
    else:
        await bot.send_message(message.from_user.id, text="Бро, ты кто? \n иди-ка ты отсюда")

#Выбор направления
async def choice_direction(message: types.Message):
    db.delete()
    db.delete_data()
    db.delete_prog_reg()
    if message.text == 'Настроить расписание':
        db.ff_step("schedule_data", 1)
    elif message.text == 'Узнать кто записался':
        db.ff_step("prog_who_reg", 1)
    elif message.text == 'Записать нового пользователя':
        db.ff_step("users_from_admin", 1)
    await bot.send_message(message.from_user.id, text="Выберете игру:", reply_markup=nav.InmainGames)

#Выбор: узнаем кто куда записался
async def startwhoreg(message: types.Message):
    db.delete_data()
    db.delete()
    db.delete_prog_reg()
    db.ff_step("prog_who_reg", 1)
    await bot.send_message(message.from_user.id, text="Выберете игру:", reply_markup=nav.InmainGames)

async def add_new_user(message: types.Message):
    db.delete_data()
    db.delete()
    db.delete_prog_reg()
    db.ff_step("users_from_admin", 1)
    await bot.send_message(message.from_user.id, text="Выберете игру для нового пользователя:", reply_markup=nav.InmainGames)

async def set_new_user(message: types.Message):
    db.delete_data()
    db.delete()
    db.update_column('game', 'NULL')
    clickdate = db.sel_admin_us('date', 1)[0]
    data_id = db.select_data_id_chek(clickdate)[0]
    time_id = db.sel_admin_us('time', 1)[0]
    game_id = db.select_game_id(data_id, time_id)[0]
    all_seats = db.select_seats(game_id)[0]
    us_seats = db.sel_admin_us('seats', 1)[0]
    new_seats = all_seats + us_seats
    db.update_seats(new_seats, game_id)
    await bot.send_message(message.from_user.id, text="Выберете игру для нового пользователя:", reply_markup=nav.InmainGames)

#Выбор: настройка расписания
#Вызов выбора игры
async def schedule_comm(message: types.Message):
    db.delete_data()
    db.delete()
    db.delete_prog_reg()
    db.ff_step("schedule_data", 1)
    await bot.send_message(message.from_user.id, text="Выберете игру:", reply_markup=nav.InmainGames)

#Выбор игры/вызов ввода даты
async def call_back_games2(query: types.CallbackQuery, text, vector):
    if vector == True:
        vec = 1
    else:
        vec = 3
    if examination_schedule("schedule_data", vec) == False and examination_who_reg("prog_who_reg") == False and examination_schedule("users_from_admin", vec) == False:
        await bot.send_message(query.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(query.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")
    else:

        if examination_schedule("schedule_data", vec) == True:
            table = "schedule_data"
        elif examination_who_reg("prog_who_reg") == True:
            table = "prog_who_reg"
        elif examination_schedule("users_from_admin", vec) == True:
            table = "users_from_admin"
        game = text
        db.f_step(table, game, 2, 1)
        if table == "prog_who_reg":
            await kb_data(query)
        elif table == "schedule_data":
            await bot.send_message(query.from_user.id, text="Напишите дату проведения игры. \nПример: 20-02-2023")
        elif table == "users_from_admin":
            print('ya tut')
            if db.sel_set(2)[0] == None or db.sel_set(2)[0] == 'name':
                await bot.send_message(query.from_user.id, text="Ведите имя")
            else:
                print('ya tut')
                us_name = db.sel_admin_us("name", 2)[0]
                await name(query, us_name, True)

#Выбор даты/вызов ввода времени/ввод времени/вызов ввода кол-ва места/ввод кол-ва мест
async def dat(message: types.Message, text, vector):
    if vector == True:
        vec = 2
    else:
        vec = 4
    if examination_schedule("schedule_data", vec) == False:
        await bot.send_message(message.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")    
    else:
        valid_date = []
        date_pattern = r"\d{1,2}-\d{1,2}-\d{4}"
        date = re.findall(date_pattern, text)
        halt = True
        for item in date:
            day, month, year  = map(int, item.split('-'))
            today = datetime.date.today()
            year_today = today.year
            if year_today <= year <= 2050:
                if 1 <= month <= 12:
                    if month == 2:
                        if 1 <= day <= 28:
                            valid_date.append(item)
                        else:
                            await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                            halt = False
                    elif month % 2 == 0:
                        if 1 <= day <= 30:
                            valid_date.append(item)
                        else:
                            await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                            halt = False
                    elif month % 2 == 1:
                        if 1 <= day <= 31:
                            valid_date.append(item)
                        else:
                            await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                            halt = False
                    else:
                        await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                        halt = False
                else:
                    await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                    halt = False
            else:
                    await bot.send_message(message.from_user.id, text="Вы отправили мне несуществующую дату или вообще не дату")
                    halt = False
        date_str = ''.join(valid_date)
        if halt == True:
            user_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            if today > user_date:
                await bot.send_message(message.from_user.id, text="Эта дата меньше, чем сегодняшняя. Зачем вы пытаетесь добавить в расписание дату из прошлого? 🧐")
            else:
        # Дата прошла проверку

                if db.select("game", vec)[0] == "volleyball":
                    sel_game = "volleyball"
                else:
                    sel_game = "football"


                if db.chek_data(message.text, sel_game) != []:
                    await bot.send_message(message.from_user.id, text="Такая дата уже есть. Вы можете ее удалить")
                else:
                    db.add("data", message.text, 3, 2, sel_game)
                    await bot.send_message(message.from_user.id, text=f"Дата успешно добавлена!\nДанные, которые вы уже добавили:\nИгра: {sel_game}\nДата: {date_str}\nЕсли все верно - продолжайте, если нет - вернитесь назад", reply_markup=nav.kbstep)
        else:
            await bot.send_message(message.from_user.id, text="Вы ввели дату с ошибкой, или пытаетесь ввести вообще не дату")


# Выбор времени
async def added_times(message: types.Message, text, vector):
    db.delete_new_times()
    if vector == True:
        vec = 3
    else:
        vec = 5
    if examination_schedule("schedule_data", vec) == False:
        await bot.send_message(message.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")
    else:
        valid_times = []
        time_pattern = r"\d{1,2}:\d{2}"
        time = re.findall(time_pattern, text)
        for item in time:
            hour, minute = map(int, item.split(':'))
            if 0 <= hour <= 23 and 0 <= minute <= 60:
                valid_times.append(item)
                halt = True
            else:
                halt = False





        if halt == True:
            ms = ' '.join(valid_times)
            times = ms.split()
            bool = False
            for i in ms:
                if i == ":":
                    bool = True
                    break
            if bool == True:
                cc = 0
                data_id = db.select_data_id(vec)[0] # узнаю какая дата была выбрана
                while cc < len(times):
                    if bool == True:
                        db.insert_time(data_id, times[cc], 4)
                    cc += 1
                db.update_step(data_id, 4)
                count_games = db.count_games(4)[0]
                date = db.select_data(4)[0]
                game = db.select_game(4)[0]
                str_time = ' и '.join(valid_times)
                await bot.send_message(message.from_user.id, text=f"Вы добавили {count_games} игры\nНа дату: {date}\nПо игре: {game}\nНа время: {str_time}", reply_markup=nav.kbstep)



#Ввод места
async def num_of_seats(n: int): #message: types.Message, vector):
    if vector == True:
        vec = 4
    else:
        vec = 5
    if examination_schedule("schedule_data", vec) == False and examination_schedule("users_from_admin", vec+1) == False:
        await bot.send_message(message.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")    
    else:
        

        valid_seats = []
        seats_pattern = r"\d{2}|\d{1}"
        seats = re.findall(seats_pattern, message.text)
        mess = ''.join(message.text)
        if examination_schedule("users_from_admin", vec+1) == True:
            date = db.select_ad_data(5)[0]
            data_id = db.sel_data_id(date)[0]
            times = db.sel_admin_us('time', 5)[0]
            game_id = db.select_game_id(data_id, times)[0]
            all_seats = db.select_seats(game_id)[0]
            back_seats = db.sel_admin_us('seats', 5)[0]
            if int(seats[0]) > back_seats:
                await bot.send_message(message.from_user.id, text="Мест на эту игру больше нет! Вы можете выбрать другую игру или написать количетсво мест меньше чем у вас было или отавить все как есть)")
            else:  
                if db.sel_set(5)[0] == None:
                    if int(seats[0]) <= int(all_seats):
                        db.add_seats(int(seats[0]), 6, vec+1)
                        db.update_seats(int(all_seats) - int(seats[0]), game_id)
                        await bot.send_message(message.from_user.id, text="Выберете способ оплаты", reply_markup=nav.payment)
                    else:
                        await bot.send_message(message.from_user.id, text="Столько мест на эту игру нет. Введите другое число или выберете другое время")
                        db.update_lvl_admin(4, 6)
                else:
                    seat_us = db.sel_admin_us('seats', 5)[0]
                    print("seats_us =", seat_us)
                    print("all_seats + seats_us =", int(all_seats)+int(seat_us), "game_id =", game_id)
                    db.update_seats(int(all_seats)+int(seat_us), game_id)
                    new_seats = db.sel_admin_us('seats', 5)[0]
                    print("new_seats =", new_seats)
                    if int(seats[0]) <= int(all_seats):
                        db.add_seats(int(seats[0]), 6, vec+1)
                        db.update_seats(int(all_seats) - int(new_seats), game_id)
                        await bot.send_message(message.from_user.id, text="Данные успешно изменены")
                        await mes(message)
                    else:
                        await bot.send_message(message.from_user.id, text="Столько мест на эту игру нет. Введите другое число или выберете другое время")
                        await mes(message)
                        db.update_lvl_admin(4, 6)
        else:
            howmutch = db.select_new_games()[0]
            place = seats[:howmutch]
            if howmutch > len(place):
                await bot.send_message(message.from_user.id, text=f"Вы ввели места только на одну игру, а добавили {howmutch}. Пожалуйста введите места для всех игр сразу.\n!НАПОМИНАЮ!\nЗа места на игру учитываются любые цифры(однозначные и двузначные)")
            else:
                
                bool = False
                for i in mess:
                    if i == ":":
                        bool = True
                        break
                if bool == True:
                    text = ''.join([item[0] for item in db.select_times()])
                    await added_times(message, text, vector)
                else:
                    data_id = db.select_data_id(4)[0]
                    res = db.select_id(data_id)
                    hmid = [item[0] for item in res]
                    cc = 0
                    while cc < len(place):
                        db.add_place(place[cc], hmid[cc], data_id)
                        cc += 1
                    game = db.select_game(5)[0]
                    date = db.select_data(5)[0]
                    times = [item[0] for item in db.select_times()]
                    seats_list = []
        #           for item in place:
        #               seats_list.append(f"({item})")
                    combined_list = [f"{x} ({y})" for x, y in zip(times, place)]
                    str_time_and_seats = ' и '.join(combined_list)
        #            time_and_seats = [item for pair in zip(times, seats_list) for item in pair]
                    await bot.send_message(message.from_user.id, text=f"!Последний шаг перед завершением расписания!\nИгра: {game}\nДата: {date}\nВремя и места: {str_time_and_seats}", reply_markup=nav.kbstep)
    #            await bot.send_message(message.from_user.id, text="Вот две моих главные команды:\n/schedule - настроить расписание\n/whoreg - посмотреть кто куда записался и заодно связаться с ними")




#Выбор: узнаем кто куда записался

#Выбор даты
async def kb_data(message: types.Message):
    if examination_who_reg("prog_who_reg") == False:
        await bot.send_message(message.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")   
    else:
        days = []
        game = db.select_game_whor()[0]
        row = [date[0] for date in db.sel_all_data(game)]
        if row == []:
            await bot.send_message(message.from_user.id, text="У вас в расписании нет игр подходящих под эти критерии", reply_markup=nav.whoreg)
            await bot.send_message(message.from_user.id, text="Вот две моих главные команды:\n/schedule - настроить расписание\n/filled - посмотреть кто куда записался и заодно связаться с ними")
        else:
            for item in row:
                days.append(item)

            await bot.send_message(message.from_user.id, text="Выберете дату:", reply_markup=nav.kbdata(days))


#Узнаю какая дата выбрана
async def click_date(query: types.CallbackQuery, text, vector):
    if vector == True:
        vec = 3
    else:
        vec = 4
    if examination_who_reg("prog_who_reg") == False and examination_schedule("users_from_admin", vec) == False:
        await bot.send_message(query.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(query.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")    
    else:
        choice = text
        if examination_schedule("users_from_admin", vec) == True:
            db.add_date(choice, 4, 3)
        else:
            db.update("data", choice, 3, 2)
        times = []
        seats = []
        print(choice)
        data_id = db.sel_data_id(choice)[0]

        seat = [date[0] for date in db.sel_seats(data_id)]
        row = [date[0] for date in db.sel_time(data_id)]
        for item, count in zip(row, seat):
            times.append(item)
            seats.append(count)
        game = db.sel_admin_us('game', 4)[0]
        count_games = db.select_count_games(game)[0]
        if count_games == 1:
            await bot.send_message(query.from_user.id, text=f"Вы не можете выбрать другую игру, т.к. в расписании нет других игр по {game}, на эту дату")
            await mes(query)
        else:
            await bot.send_message(query.from_user.id, text="Выберете время:", reply_markup=nav.kbtime(times, seats))
            


#Узнаю какое время было выбрано
async def ckick_time(query: types.CallbackQuery, text, vector):
    if vector == True:
        vec = 4
    else:
        vec = 5
    if examination_who_reg("prog_who_reg") == False and examination_schedule("users_from_admin", vec) == False:
        await bot.send_message(query.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
        await bot.send_message(query.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")   
    else:
        choice = text
        if examination_schedule("users_from_admin", vec) == True:
            data = db.select_ad_data(vec)[0]
            data_id = db.select_data_id_chek(data)[0]
            game_id = db.select_game_id(data_id, choice)[0]
            db.add_time_admin(choice, 5, 4)
            if db.sel_set(5)[0] == None or db.sel_set(5)[0] == 'seats':
                await bot.send_message(query.from_user.id, text="Введите количество мест", reply_markup=nav.kbremove)
            else:
                us_seats = db.sel_admin_us('seats', 5)[0]
                open_seats = db.select_seats(game_id)[0]
                if open_seats < us_seats:
                    await bot.send_message(query.from_user.id, text="Количетсов мест, которые вы вводили до этого больше, чем количетсво свободных мест на вашей новой игре.\nПожалуйста, введите другое количество желаемых мест")
                else:
                    await bot.send_message(query.from_user.id, text="Данные успешно изменены")
                    await mes(query)
        else:
            data = db.select_data_whor()[0]
            data_id = db.select_data_id_chek(data)[0]
            game_id = db.select_game_id(data_id, choice)[0]
            reg_list = db.chek_guys(game_id)
            db.update("time", choice, 4, 3)
            if reg_list == []:
                await bot.send_message(query.from_user.id, text="Тут никого нет(((")
                await bot.send_message(query.from_user.id, text="Желаете удалить эту игру?", reply_markup=nav.kbyes)
            else:

                nicknames = await link_generetion(game_id)



                inf_list = ["Имя", "Сколько человек вместе с ним(ней)", "Способ оплаты"]
                message_text = "Вот кто зарегистрировался на эту игру: \n"
                i = 0
                j = 0
                while i < len(reg_list):
                    while j < 3:
                        text = reg_list[i][j]
                        if j == 0:
                            text = hlink(reg_list[i][j], nicknames[i])
                        message_text += f"<b>-{inf_list[j]}:</b>   <u>{text}</u>\n"
                        j += 1
                    i += 1
                    j = 0

                await bot.send_message(query.from_user.id, text=message_text, parse_mode="HTML")
                db.delete()



async def link_generetion(game_id):

    all_nicknames = [date[0] for date in db.sel_all_nickname(game_id)]
    message_text = []
    for item in all_nicknames:
        message_text.append(f"t.me/{item}")



    return message_text



#New user
async def name(message: types.Message, text, vector):
    print("ya teper tut")
    if text == "Завершить регистрацию":
        await end_new_us(message, text)
    else:
        if vector == True:
            vec = 2
        else:
            vec = 4
        if examination_schedule("users_from_admin", vec) == False:
            await bot.send_message(message.from_user.id, text="Если бы не мой хозяин, то я бы сейчас залагал, т.к. вы нарушили мои правила.\nНа всякий случай вышлю вам их еще раз:")
            await bot.send_message(message.from_user.id, text="Итак, вот несколько правил как мной пользоваться:\nЕсли вы решили что то посмотреть или дополнить расписание, то !ОБЯЗАТЕЛЬНО! начинайте все с самого начала, а если конкретнее, то с начальных кнопках клавиатуры. Или же используете спецальные команды, такие как:\n/schedule - любая правка расписания\n/filled - если хотите узнать кто куда зарегестрировался и для связи с игроками\n/newuser - Вы сами можете добавить нового пользователя")   
        else:
            db.add_name(text, 3, 2)
            res = db.select_name()[0]

            days = []
            game = db.select_game_admin(3)[0]
            row = [date[0] for date in db.sel_all_data(game)]
            if row == []:
                await bot.send_message(message.from_user.id, text="У вас в расписании нет игр подходящих под эти критерии", reply_markup=nav.whoreg)
                await bot.send_message(message.from_user.id, text="Вот три моих главные команды:\n/schedule - настроить расписание\n/filled - посмотреть кто куда записался и заодно связаться с ними\n/newuser - Вы сами можете добавить нового пользователя")
            else:
                for item in row:
                    days.append(item)
                if db.sel_set(3)[0] == 'game' or db.sel_set(3)[0] == 'date' or db.sel_set(3)[0] == None:
                    await bot.send_message(message.from_user.id, text="Выберете дату:", reply_markup=nav.kbdata(days))
                else:
                    await bot.send_message(message.from_user.id, text="Данные успешно изменены")
                    await mes(message)

async def paymen_ad_us(message: types.Message, text):
    if text == '💷 Наличные':
        pay = "Наличные"
    else:
        pay = "Перевод"
    db.add_payment(pay, 7, 6)
    if db.sel_set(7)[0] == None:
        await bot.send_message(message.from_user.id, text="Введите номер телефона (цифры, с кодом страны, без плюса)")
  #      await bot.send_message(message.from_user.id, text=f"Вот все данные нового пользователя:\nИгра: {list_inf[item][1]}\nИмя: {list_inf[item][3]}\nДата: {list_inf[item][2]}\nВремя проведение игры: {list_inf[item][4]}\nКоличество людей с ним(ней): {list_inf[item][5]}\nСпособ оплаты: {pay}")
  #      await bot.send_message(message.from_user.id, text="Если все данные верны - завершите регистрацию на игру нового пользователя\nЕсли нет - вернитесь назад\n\n\n1.Закончить регистрацию\n2.Вернуться и исправить данные", reply_markup=nav.admuser)
    else:
        await bot.send_message(message.from_user.id, text="Данные успешно изменены")
        await mes(message)

async def num_phone(message: types.Message, text):
    db.update_num(text, 7)
    list_inf = db.select_ad_us(7)
    item = 0

    await bot.send_message(message.from_user.id, text=f"Вот все данные нового пользователя:\nИгра: {list_inf[item][1]}\nИмя: {list_inf[item][3]}\nДата: {list_inf[item][2]}\nВремя проведение игры: {list_inf[item][4]}\nКоличество людей с ним(ней): {list_inf[item][5]}\nСпособ оплаты: {list_inf[item][6]}\nНомер телефона: +{text}")
    await bot.send_message(message.from_user.id, text="Если все данные верны - завершите регистрацию на игру нового пользователя\nЕсли нет - вернитесь назад\n\n\n1.Закончить регистрацию\n2.Вернуться и исправить данные", reply_markup=nav.admuser)
    db.update_lvl_admin(8, 7)


async def end_new_us(message: types.Message, text):
    if text == "1👍" or text == "Завершить регистрацию":
        inf = db.select_inf_ad(7)
        item = 0
        data_id = db.select_data_id_chek(inf[item][2])[0]
        game_id = db.select_game_id(data_id, inf[item][4])[0]

        #Заношу в базу данных нового пользователя
        db.add_new(inf[item][0], game_id, inf[item][5], inf[item][6])
        await bot.send_message(message.from_user.id, text="Новый пользователь успешно добавлен!")
        await bot.send_message(message.from_user.id, text="Вот три моих главные команды:\n/schedule - настроить расписание\n/filled - посмотреть кто куда записался и заодно связаться с ними\n/newuser - Вы сами можете добавить нового пользователя")
        db.update_lvl_admin(10, 7)
    else:
        if db.set() == False:
            db.up_set('start')
            await mes(message)
        else:
            if text == "1":
                db.up_set('game')
                db.update_lvl_admin(1, 7)
                await set_new_user(message)
            elif text == "2":
                db.up_set('name')
                db.update_lvl_admin(2, 7)
                await bot.send_message(message.from_user.id, text="Ведите имя")
            elif text == "3":
                db.up_set('date')
                db.update_lvl_admin(2, 7)
                db.update_column('settings', 'days')
                my_name = db.sel_admin_us('name', 2)[0]
                await name(message, my_name, True)
            elif text == "4":
                db.up_set('time')
                db.update_lvl_admin(3, 7)
                db.update_column('settings', 'time')
                date = db.sel_admin_us('date', 3)[0]
                await click_date(message, date, True)
            elif text == "5":
                db.up_set('seats')
                db.update_lvl_admin(4, 7)
                db.update_column('settings', 'seats')
                time = db.sel_admin_us('time', 4)[0]
                await ckick_time(message, time, True)
            elif text == "6":
                db.up_set('payment')
                db.update_lvl_admin(6, 7)
                await bot.send_message(message.from_user.id, text="Выберете способ оплаты", reply_markup=nav.payment)





async def mes(message: types.Message):
    await bot.send_message(message.from_user.id, text="Выберете данные которые хотите изменить:\n\n1.Игра\n2.Имя\n3.Дата проведения игры\n4.Время проведения игры\n5.Кол-во мест\n6.Способ оплаты", reply_markup=nav.chang_the_data)
    db.update_lvl_set(7)







def examination_who_reg(table):
    if db.w_is_inside(table) == False:
        ex = False
    else:
        ex = True
    return ex

def examination_schedule(table, lvl):
    if db.ex_step(table, lvl) == False:
        ex = False
    else:
        ex = True
    return ex

#Удаление игры
async def del_game(query: types.CallbackQuery):
    if query.data == 'yes':
        all_inf_game = db.inf_game()
        data_id = db.sel_data_id(all_inf_game[0][2])[0]
        count_games = db.hm_games(data_id)[0]
        game_id = db.select_game_id(data_id, all_inf_game[0][3])[0]
        if count_games == 1:
            db.del_game(game_id)
            db.del_data(all_inf_game[0][2], "schedule_data")
        else:
            db.del_game(game_id)
        await bot.send_message(query.from_user.id, text="Данная игра удалена")
        db.delete()
    else:
        await bot.send_message(query.from_user.id, text="Хорошо, тогда возвращаю вас в начало")
        await bot.send_message(query.from_user.id, text="Вот тве моих главные команды:\n/schedule - настроить расписание\n/filled - посмотреть кто куда записался и заодно связаться с ними\n/newuser - Вы сами можете добавить нового пользователя")
        
       

async def step(message: types.Message):
    all_lvls = [1, 2, 3, 4, 5, 10]
    i = 0
    table = db.name_table()[0]
    lvl = db.sel_lvl(table)[0]
    while lvl != all_lvls[i]:
        i += 1
    if message.text == 'Следующий шаг':
        next_lvl = all_lvls[i + 1]
        if lvl == 1:
   #         if table == "prog_who_reg":
    #            await kb_data(message)
    #            db.update_lvl_whor(next_lvl)
     #       else:
                pass
        elif lvl == 3:
        #    if table == "prog_who_reg":
         #       data = db.select_data_whor()[0]
         #       await click_date(message, data, False)
         #       db.update_lvl_whor(next_lvl)
            if table != "prog_who_reg":
                await bot.send_message(message.from_user.id, text="Введите время игры в следующем формате: 12:00 13:00 14:00 15:00")
        elif lvl == 4:
            if table != "prog_who_reg":
                await bot.send_message(message.from_user.id, text="Ведитен кол-во мест\nБот принимает значение только в цифрах и только в однозначных и дузначных.\nЕсли вам требуется указать места на больше чем одну игру, то пишите цифры через пробел")
        elif lvl == 5:
            if table != "prog_who_reg":
                await bot.send_message(message.from_user.id, text="Расписание завершено!", reply_markup=nav.whoreg)
                db.end()
                await bot.send_message(message.from_user.id, text="Вот две моих главные команды:\n/schedule - настроить расписание\n/filled - посмотреть кто куда записался и заодно связаться с ними")

    
    elif message.text == 'Назад':
        if lvl == 1:
            await bot.send_message(message.from_user.id, text="Это начало", reply_markup=None)
        back_lvl = all_lvls[i-1]
        if lvl == 2:
            if table == "prog_who_reg":
                await startwhoreg(message)
                db.update_lvl_whor(back_lvl)
            else:
                await schedule_comm(message)
                db.update_lvl(back_lvl, "schedule_data", "schedule_games")
        elif lvl == 3:
            if table == "prog_who_reg":
                await kb_data(message)
                db.update_lvl_whor(back_lvl)
            else:
                text = db.select_game(3)[0]
                await call_back_games2(message, text, False)
                db.update_lvl(back_lvl, "schedule_data", "schedule_games")
        elif lvl == 4:
            if table != "prog_who_reg":
                text = db.select_data(4)[0]
                db.delete_new_times()
                await dat(message, text, False)
                db.update_lvl(back_lvl, "schedule_data", "schedule_games")
        elif lvl == 5:
            if table != "prog_who_reg":
                text = ''.join([item[0] for item in db.select_times()])
                await added_times(message, text, False)
                db.update_lvl(back_lvl, "schedule_data", "schedule_games")

#        if db.sel_column(lvl) == True:
#            if now_lvl == 1:
#                await call_back_games2()
#            elif now_lvl == 2:
#            elif now_lvl == 3:
#            elif now_lvl == 4:
#            elif now_lvl == 5:
#    else:
#        pass
#async def what_date(message: types.Message):   
#    global weekDays
#    current_day = datetime.datetime.now().strftime("%A")  
#    logging.warning(current_day)
#    day = "Sunday"
#    i = 0
#    while weekDays[i] != current_day:
#        i += 1
#    j = i
#    while weekDays[j] != day:
#        j += 1
#    count = j - i
#    days = count
#    logging.warning(days)
#    future_date = datetime.datetime.now() + datetime.timedelta(days=days)
#    future_date_str = future_date.strftime("%Y-%m-%d")
#    await bot.send_message(message.from_user.id, text=future_date_str)




#    await bot.send_message(user.id, text="Напишите в какое время будет проходить игра через двоеточие и запятые. Например: 12:00,09:00,22:00 \n!БЕЗ ПРОБЕЛОВ!\nМаксимальное количество игр привязанное к одному дню - 4")


async def main():
    print("zzz")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print("wtf")
    asyncio.run(main())