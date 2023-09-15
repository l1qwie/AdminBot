from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
defualtkb = []
#0
ComStartReg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Зарегистрироваться", callback_data="Зарегистрироваться")]])

#1
MenuOptions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Узнать кто записался', callback_data='Узнать кто записался')]
    ,[InlineKeyboardButton(text='Настроить расписание', callback_data='Настроить расписание')]
    ,[InlineKeyboardButton(text='Создать нового пользователя', callback_data='Создать нового пользователя')]
    ,[InlineKeyboardButton(text='Зарегестрировать пользователя на игру', callback_data='Зарегестрировать пользователя')]
    ,[InlineKeyboardButton(text="Настроить/удалить пользователя", callback_data="Настроить пользователя")]
    ,[InlineKeyboardButton(text="Получить отчет о деятельности бота", callback_data="Отчет")]
    ,[InlineKeyboardButton(text="Уведомления", callback_data="notification")]

    #,[InlineKeyboardButton(text='Зарегестрировать на игру пользователя', callback_data='Зарегестрировать на игру пользователя')]
])

Next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Продолжить", callback_data="next")]
])

Enumeration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Откуда? (messanger)", callback_data="fronwhere")],
    [InlineKeyboardButton(text="Имя?", callback_data="name")],
    [InlineKeyboardButton(text="Фамилия?", callback_data="lastname")],
    [InlineKeyboardButton(text="Предпочитаемый язык", callback_data="language")],
    [InlineKeyboardButton(text="Номер телефона", callback_data="phonenum")],
    [InlineKeyboardButton(text="Главное меню", callback_data="MainMenu")]
])


Do = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Настроить пользователя", callback_data="setuser")],
    [InlineKeyboardButton(text="Удалить пользователя", callback_data="deluser")],
    [InlineKeyboardButton(text="Главное меню", callback_data="MainMenu")]
])


#2
MenuSports = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Volleyball', callback_data='volleyball')],
    [InlineKeyboardButton(text='Football', callback_data='football')]
])

#3
MenuFrom = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', callback_data='tg')],
    [InlineKeyboardButton(text='WhatsApp', callback_data='whatsapp')],
    [InlineKeyboardButton(text='Viber', callback_data='viber')],
    [InlineKeyboardButton(text='Позвонили', callback_data='calls')]
])

def datenotif(days, status):
    keyboard = []
    for count, item in zip(days, status):
        if item == "del":
            stat = "Удалена"
        elif item == "changed":
            stat = "Изменена"
        button = InlineKeyboardButton(text=f"{count}  ({stat})", callback_data=f"{count}")
        keyboard.append([button])
    inkbnotif = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkbnotif

def kbdata(days):
    keyboard = []
    for day in days:
        button = InlineKeyboardButton(text=f"{day}", callback_data=f"{day}")
        keyboard.append([button])
    inkb1 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkb1

def kbtime(times, seats):
    keyboard = []
    for count, item in zip(times, seats):
        button = InlineKeyboardButton(text=f"{count}  ({item} мест)", callback_data=f"{count}")
        keyboard.append([button])

    inkb2 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkb2


def kbnames(name_tg, id_us):
    keyboard = []
    result_list = [' '.join(names) for names in name_tg]
    for us_name, idus in zip(result_list, id_us):
        button = InlineKeyboardButton(text=f"{us_name}", callback_data=f"{idus}")
        keyboard.append([button])
    inkbnames = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkbnames


BackorMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data="back")],
    [InlineKeyboardButton(text="Главное меню", callback_data="menuop")]
])

FrequentChoice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Он будет один", callback_data="1")],
    [InlineKeyboardButton(text="Их будет двое", callback_data="2")],
    [InlineKeyboardButton(text="Их будет трое", callback_data="3")]
])


KbPay = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Наличные", callback_data="cash")],
    [InlineKeyboardButton(text="Безналичный расчет", callback_data="card")]
])


WatNext = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="В главное меню", callback_data="MainMenu")]])

SetSchedule = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить новую игру", callback_data="new")],
    [InlineKeyboardButton(text="Редактировать игру", callback_data="setSche")],
    [InlineKeyboardButton(text="Удалить игру", callback_data="delSche")]
])


Notif = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Уведомлен", callback_data="Notif completed")],
    [InlineKeyboardButton(text="В главное меню", callback_data="MainMenu")]
])

UserDecision = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Решил(а) остаться",  callback_data="user wait")],
    [InlineKeyboardButton(text="Отменил(а) запись на игру", callback_data="user not wait")]
])

#3
btnin = InlineKeyboardButton(text='Пн', callback_data="Пн")
btnin2 = InlineKeyboardButton(text='Вт', callback_data="Вт")
btnin3 = InlineKeyboardButton(text='Ср', callback_data="Ср")
btnin4 = InlineKeyboardButton(text='Чт', callback_data="Чт")
btnin5 = InlineKeyboardButton(text='Пт', callback_data="Пт")
btnin6 = InlineKeyboardButton(text='Cб', callback_data="Сб")
btnin7 = InlineKeyboardButton(text='Вс', callback_data="Вс")

inkb = InlineKeyboardMarkup(row_width=7, inline_keyboard=[[btnin, btnin2, btnin3, btnin4, btnin5, btnin6, btnin7]])

#4

btnt = InlineKeyboardButton(text="12:00", callback_data="12:00")
btnt2 = InlineKeyboardButton(text="17:00", callback_data="17:00")
btnt3 = InlineKeyboardButton(text="20:30", callback_data="20:30")

inkbtime = InlineKeyboardMarkup(row_width=3, inline_keyboard=[[btnt, btnt2, btnt3]])

btningames = InlineKeyboardButton(text="Волейбол", callback_data="volleyball")
btningames2 = InlineKeyboardButton(text="Футбол", callback_data="football")

InmainGames = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[btningames, btningames2]])

btnyes = InlineKeyboardButton(text="Да", callback_data="yes")
btnno = InlineKeyboardButton(text="Нет", callback_data="no")

kbyes = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[btnyes, btnno]])


btndel = InlineKeyboardButton(text="Удалить дату", callback_data="del")
btnchange = InlineKeyboardButton(text="Поменять дату", callback_data="change")

kbset = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[btndel, btnchange]])


btnNext = KeyboardButton(text="Следующий шаг")
btnBack = KeyboardButton(text="Назад")

kbstep = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btnNext, btnBack]])


btn1 = KeyboardButton(text="1👍")
btn2 = KeyboardButton(text="2👎")
admuser = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btn1, btn2]])

btnCash = KeyboardButton(text='💷 Наличные')
btnCard = KeyboardButton(text='💳 Перевод')
defualtkb.append([btnCash])
defualtkb.append([btnCard])

payment = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
defualtkb.clear()

btn_1 = KeyboardButton(text='1')
btn_2= KeyboardButton(text='2')
btn_3 = KeyboardButton(text='3')
btn_4 = KeyboardButton(text='4')
btn_5 = KeyboardButton(text='5')
btn_6 = KeyboardButton(text='6')
btn_itsok = KeyboardButton(text='Завершить регистрацию')
defualtkb.append([btn_1, btn_2, btn_3])
defualtkb.append([btn_4, btn_5, btn_6])
defualtkb.append([btn_itsok])


chang_the_data = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
defualtkb.clear()


kbremove = ReplyKeyboardRemove()