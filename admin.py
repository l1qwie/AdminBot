import datetime
import database
import keyboards as nav
import re

def failingNamer(name: str, nick:str):
    assert(False)


namer = failingNamer 

INITIAL = 1
INTRO1 = 2
OPTIONSMENU = 3




class Admin:
    id: int
    name: str
    surname: str
    username: str
    act: str
    sport_check_users: str
    date_check_users: int
    time_check_users: int
    user_id_check_users: int
    fromwhere_new_user: str
    name_new_user: str
    lastname_new_user: str
    language_new_user: str
    phonenum_new_user: str
    sport_schedule: str
    date_schedule: int
    time_schedule: int
    seats_schedule: int
    sport_reg_ad_us: str
    date_reg_ad_us: int
    time_reg_ad_us: int
    seats_reg_ad_us: int
    payment_reg_ad_us: str
    user_id_change_user: int
    action_change_user: str
    level: int


NEGATIVE = -1
START = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3
OPTIONS = 3
LEVEL4 = 4
LEVEL5 = 5



def DispatchPhrase (id: int, phrase: str):
    a = RetrieveAdmin(id)
    print('level =', a.level, 'phrase =', phrase, 'action =', a.act)
    if phrase == "MainMenu" or phrase == "/menu":
        text = "Главное меню"
        kbd = nav.MenuOptions
        prmode = None
        halt = None
        a.level = OPTIONS
        a.act = None
        spreadsheet = None
        fixed = None
    elif a.act == "registation":
       (text, kbd, prmode, halt, spreadsheet, fixed) = REG(a, id, phrase)
    elif a.act == "create new user":
        (text, kbd, prmode, halt, spreadsheet, fixed) = CreateNewUser(a, id, phrase)
    elif a.act == "view registered users":
        (text, kbd, prmode, halt, spreadsheet, fixed) = ViewWhoReg(a, id, phrase)
    elif a.act == "schedule setting":
        (text, kbd, prmode, halt, spreadsheet, fixed) = ChangeSchedule(a, id, phrase)
    elif a.act == "registration new user":
        (text, kbd, prmode, halt, spreadsheet, fixed) = RegistiredAdminUser(a, id, phrase)
    elif a.act == "сhange user":
        (text, kbd, prmode, halt, spreadsheet, fixed) = ChangeUsers(a, id, phrase)
    elif a.act == "divarication":
        if phrase in ('Узнать кто записался', 'Настроить расписание', 'Создать нового пользователя', 'Зарегестрировать пользователя', 'Настроить пользователя', 'Отчет'):
            if a.level == OPTIONS:
                (text, kbd, prmode, halt, spreadsheet, fixed) = MenuOptions(a, id, phrase)
        else:
            text = "!!!СЕЙЧАС Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!!!"
            kbd = nav.MenuOptions
            prmode = None
            halt = None
            a.level = OPTIONS
            a.act = "divarication"
            spreadsheet = None
            fixed = None
    RetainAdmin(a)
    print("a.act =", a.act)
    print("TEXT =", text)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def ChangeUsers(a: Admin, id: int, phrase: str):
    if a.level == START:
        (names_users, id_users) = database.AllUsers()
        text = "Выберите пользователя"
        kbd = nav.kbnames(names_users, id_users)
        a.level = LEVEL1
        a.action_change_user = phrase
    elif a.level == LEVEL1:
        if a.action_change_user == "setuser":
            (names_users, id_users) = database.AllUsers()
            text = "Выберите что вы хотите изменить"
            kbd = nav.Enumeration
            a.level = LEVEL2
            a.user_id_change_user = phrase
        elif a.action_change_user == "deluser":
            database.DelUs(int(phrase))
            text = "Пользователь удален. Все данные, все регистрации, вообще вся информация, которая могла быть в боте, благополучно удалена\n\n\nВозвращаю вас в главное меню"
            kbd = nav.MenuOptions
            a.level = OPTIONS
            a.act = "divarication"
    elif a.level == LEVEL2:
        if phrase == "fronwhere":
            a.fromwhere_new_user = "nextaction"
            text = "Выберите откуда пользователь"
            kbd = nav.MenuFrom
        elif phrase == "name":
            a.name_new_user = "nextaction"
            text = "Напишите имя"
            kbd = None
        elif phrase == "lastname":
            a.lastname_new_user = "nextaction"
            text = "Напишите фамилию"
            kbd = None
        elif phrase == "language":
            a.language_new_user = "nextaction"
            text = "Напишите предпочитаемый язык"
            kbd = None
        elif phrase == "phonenum":
            a.phonenum_new_user = "nextaction"
            text = "Напишите номер телефона"
            kbd = None
        a.level = LEVEL3
    elif a.level == LEVEL3:
        if a.fromwhere_new_user == "nextaction":
            a.fromwhere_new_user = phrase
            text = "Месенджер пользователя измененен"
        elif a.name_new_user == "nextaction":
            a.name_new_user = phrase
            text = "Имя изменено"
        elif a.lastname_new_user == "nextaction":
            a.lastname_new_user = phrase
            text = "Фамилия изменена"
        elif a.language_new_user == "nextaction":
            a.language_new_user = phrase
            text = "Язык изменен"
        elif a.phonenum_new_user == "nextaction":
            a.phonenum_new_user = phrase
            text = "Телефон изменен"
        a.level = LEVEL2
        kbd = nav.Enumeration
        database.UpdateInfAboutUs(a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user, a.user_id_change_user)
    prmode = None
    halt = None
    spreadsheet = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)
            


def RegistiredAdminUser(a: Admin, id: int, phrase: str):
    halt = False
    if a.level == START:
        if phrase in ("volleyball", "football"):
            schedule = database.FindDates()
            if schedule == 0:
                text = "Нет ни одной добавленной игры в расписании! Добавьте сначала игру в расписание, а уже потом регестрируйте пользователя\n\n\nГлавное меню"
                kbd = nav.MenuOptions
                a.act = "divarication"
                a.level = OPTIONS
            else:
                days = database.AllFreeDates(phrase)
                if days == []:
                    text = "В расписании нет дат на этот вид спорта\nВыберите другой вид спорта или создайте новоую игру"
                    kbd = nav.MenuSports
                else:
                    a.sport_reg_ad_us = phrase
                    text = "Выберете дату:"
                    kbd = nav.kbdata(database.AllFreeDates(phrase))
                    a.level = LEVEL1
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА ККНОПКУ\n\n\nВыберите вид спрота"
            kbd = nav.MenuSports
    elif a.level == LEVEL1:
        days = database.AllFreeDates(a.sport_reg_ad_us)
        list_for_comparison_dates = []
        for row in days:
            error, dateschedule = DateCheck(row)
            list_for_comparison_dates.append(dateschedule)
        halt, date = DateCheck(phrase)
        if halt == True:
            i = 0
            while i < len(list_for_comparison_dates):
                if date == list_for_comparison_dates[i]:
                    already = True
                    i = len(list_for_comparison_dates)
                else:
                    already = False
                i += 1
        else:
            already = False
        if already is not True:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА ККНОПКУ\n\n\nВыберите дату"
            kbd = nav.kbdata(database.AllFreeDates(a.sport_reg_ad_us))
        else:
            times = database.TimesOfFreeDates(phrase, a.sport_reg_ad_us)
            seats = database.SeatsofTimesofDateofSport(phrase, a.sport_reg_ad_us)
            a.date_reg_ad_us = dateschedule
            text = "Выберите время проведения игры"
            kbd = nav.kbtime(times, seats)
            a.level = LEVEL2
    elif a.level == LEVEL2:
        print("potantional error:", a.sport_reg_ad_us, a.date_reg_ad_us)
        times = database.TimesOfFreeDates(a.date_reg_ad_us, a.sport_reg_ad_us)
        print(times)
        halt, timeschedule = TimeCheck(phrase, a.date_reg_ad_us)
        list_for_comparison_times = []
        for row in times:
            error, dateschedule = TimeCheck(row, a.date_reg_ad_us)
            list_for_comparison_times.append(dateschedule)
        if halt == True:
            i = 0
            while i < len(list_for_comparison_times):
                if timeschedule == list_for_comparison_times[i]:
                    compare = True
                    i = len(list_for_comparison_times)
                else:
                    compare = False
                i += 1
        else:
            compare = False
        if compare is not True:
            seats = database.SeatsofTimesofDateofSport(a.date_reg_ad_us, a.sport_reg_ad_us)
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА ККНОПКУ\n\n\nВыберите время проведения игры"
            kbd = nav.kbtime(times, seats)
        else:
            a.time_reg_ad_us = timeschedule
            text = "Выберите или введите желаемое количетсво мест"
            kbd = nav.FrequentChoice
            a.level = LEVEL3
    elif a.level == LEVEL3:
        print("potantional error:", a.sport_reg_ad_us, a.date_reg_ad_us, a.time_reg_ad_us)
        if IntCheck(phrase):
            if SeatsCheck(id, phrase):
                a.seats_reg_ad_us = phrase
                text = "Выберите способ оплаты"
                kbd = nav.KbPay
                a.level = LEVEL4
            else:
                text = "Вы ввели не цифру или же вы ввели цифру котороая больше чем свободныйх мест на эту игру\n\n\nВыберите или введите желаемое количетсво мест"
                kbd = nav.FrequentChoice
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА ККНОПКУ ИЛИ ЖЕ СООБЩЕНИЕ СОСТОЯЩЕЕ ТОЛЬКО ИЗ ЧИСЛА\n\n\nВыберите или введите желаемое количетсво мест"
            kbd = nav.FrequentChoice
    elif a.level == LEVEL4:
            (names_users, id_users) = database.AllUsers()
            a.payment_reg_ad_us = phrase
            text = "Выберите пользователя"
            kbd = nav.kbnames(names_users, id_users)
            a.level = LEVEL5
    elif a.level == LEVEL5:
        a.payment_reg_ad_us = phrase
        RegAdUs(a, phrase)
        text = "Мои поздравления! Вы зарегестрировали этого пользователя на игру.\nВозвращаю Вас в главное меню"
        kbd = nav.MenuOptions
        a.level = OPTIONS
        a.act = "divarication"
    prmode = None
    spreadsheet = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)




def ViewWhoReg(a: Admin, id: int, phrase: str):
    halt = False
    if a.level == START:
        prmode = None
        if phrase in ("volleyball", "football"):
            days_db = database.GamesWithUsers(phrase)
            days_ready = []
            db = 0
            if database.Nobody() == True:
                text = "Вообще никто не забронировал места на игры, так что нигде никого нет!\n\n\n\nВозвращаю вас в главное меню"
                kbd = nav.MenuOptions
                a.level = OPTIONS
                a.act = "divarication"
            elif days_db != []:
                while db < len(days_db):
                    year = days_db[db]//10000
                    month = (days_db[db]-(year*10000))//100
                    day = (days_db[db]-(year*10000)-(month*100))//1
                    date_str = f"{day}-{month}-{year}"
                    days_ready.append(date_str)
                    db += 1
                a.sport_check_users = phrase
                text = "Выберите дату:"
                kbd = nav.kbdata(days_ready)
                a.level = LEVEL1
            else:
                text = "Никого нет\nВыберите вид спорта:"
                kbd = nav.MenuSports
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВыберите вид спорта"
            kbd = nav.MenuSports
    elif a.level == LEVEL1:
        prmode = None
        halt, date = DateCheck(phrase)
        print("DATE =", date, "HALT =", halt)
        print("FAKE", database.CheckDate(date, a.sport_check_users))
        if halt is True:
            if database.CheckDate(date, a.sport_check_users) != 0:
                (times, seats) = database.TimeOfGamesWithUsers(a.id, date)
                if times != []:
                    times_ready = []
                    tm = 0
                    while tm < len(times):
                        hour = times[tm]//100
                        minute = (times[tm]-(hour*100))//1
                        time_str = f"{hour}:{minute}"
                        times_ready.append(time_str)
                        tm += 1
                    a.date_check_users = date
                    text = "Выберите время проведения игры:"
                    kbd = nav.kbtime(time_str, seats)
                    a.level = LEVEL2
                else:
                    text = "Почему-то тут никого нет\nВозвращаю вас в главное меню"
                    kbd = nav.MenuOptions
                    a.level = START
                    a.act = "divarication"
                    #database.Action(id, a.act)
            else:
                text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВыберите дату"
                db = 0
                days_ready = []
                days_db = database.GamesWithUsers(a.sport_check_users)
                while db < len(days_db):
                    year = days_db[db]//10000
                    month = (days_db[db]-(year*10000))//100
                    day = (days_db[db]-(year*10000)-(month*100))//1
                    date_str = f"{day}-{month}-{year}"
                    days_ready.append(date_str)
                    db += 1
                    kbd = nav.kbdata(days_ready)
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВыберите дату"
            db = 0
            days_ready = []
            days_db = database.GamesWithUsers(a.sport_check_users)
            while db < len(days_db):
                year = days_db[db]//10000
                month = (days_db[db]-(year*10000))//100
                day = (days_db[db]-(year*10000)-(month*100))//1
                date_str = f"{day}-{month}-{year}"
                days_ready.append(date_str)
                db += 1
                kbd = nav.kbdata(days_ready)
    elif a.level == LEVEL2:
        prmode = None
        halt, time = TimeCheck(phrase, a.date_check_users)
        print("TIME =", time)
        if halt is True:
            if database.CheckTime(a.date_check_users, a.sport_check_users, time) != 0:
                a.time_check_users = time
                (name_users, id_users) = database.UsersOfGamesWithUsers(id, time)
                text = f"На эту игру зарегестрировалось {len(name_users)}\nНажмите на имена ниже чтоб узнать потробную информацию:"
                kbd = nav.kbnames(name_users, id_users)
                a.level = LEVEL3
            else:
                text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВыберите дату"
                (times, seats) = database.TimeOfGamesWithUsers(a.id, a.date_check_users)
                times_ready = []
                tm = 0
                while tm < len(times):
                    hour = times[tm]//100
                    minute = (times[tm]-(hour*100))//1
                    time_str = f"{hour}:{minute}"
                    times_ready.append(time_str)
                    tm += 1
                kbd = nav.kbtime(times, seats)
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВыберите дату"
            (times, seats) = database.TimeOfGamesWithUsers(a.id, a.date_check_users)
            times_ready = []
            tm = 0
            while tm < len(times):
                hour = times[tm]//100
                minute = (times[tm]-(hour*100))//1
                time_str = f"{hour}:{minute}"
                times_ready.append(time_str)
                tm += 1
            kbd = nav.kbtime(times, seats)
    elif a.level == LEVEL3:
        prmode = None
        if database.CheckUser(phrase) != 0:
            a.user_id_check_users = int(phrase)
            (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(id, a.user_id_check_users)
            if username != "Информация отсутствует":
                prmode = "HTML"
                nick = (f"t.me/{username}")
                name = namer(name, nick)
            text = f"Вот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним"
            kbd = nav.BackorMenu
            a.level = LEVEL4
        else:
            (name_users, id_users) = database.UsersOfGamesWithUsers(id, a.time_check_users)
            text = f"Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ\n\nНа эту игру зарегестрировалось {len(name_users)}\nНажмите на имена ниже чтоб узнать потробную информацию:"
            kbd = nav.kbnames(name_users, id_users)
    elif a.level == LEVEL4:
        prmode = None
        if phrase == "back":
            (name_users, id_users) = database.UsersOfGamesWithUsers(id, a.time_check_users)
            text = f"На эту игру зарегестрировалось {len(name_users)}\nНажмите на имена ниже чтоб узнать потробную информацию:"
            kbd = nav.kbnames(name_users, id_users)
            a.level = LEVEL3
        elif phrase == "menuop":
            text = "Добро пожаловать в главное меню"
            kbd = nav.MenuOptions
            a.level = OPTIONS
            a.act = "divarication"
        else:
            (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(id, a.user_id_check_users)
            text = f"Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\nВот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним"
            kbd = nav.BackorMenu
    spreadsheet = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)

def ChangeSchedule(a: Admin, id: int, phrase: str):
    if a.level == START:
        if phrase in ("volleyball", "football"):
            a.sport_schedule = phrase
            text = "Напишите дату проведения игры\nОбязательно в таком формате: ДД-ММ-ГГГГ\n\n\n ОБЯЗАТЕЛЬНО между ДД, ММ и ГГГ поставьте следующие символы: '-' ',' '.' или пробел"
            kbd = None
            a.level = LEVEL1
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ\n\nВыбрите вид спорта"
            kbd = nav.MenuSports
    elif a.level == LEVEL1:
        halt, date = DateCheck(phrase)
        if halt == True:
            a.date_schedule = date
            text = "Напишите время проведения игры в формате: ЧЧ:ММ\n\n\nОБЯЗАТЕЛЬНО между ЧЧ и ММ поставьте следующие символы: '-' ',' '.' или пробел"
            kbd = None
            a.level = LEVEL2
        else:
            text = "Вы ввели не дату или же дату, но она меньше чем сегодняшнее число\nНапишите дату\n\n\nОБЯЗАТЕЛЬНО между ДД, ММ и ГГГ поставьте следующие символы: '-' ',' '.' или пробел"
            kbd = None
    elif a.level == LEVEL2:
        halt, time = TimeCheck(phrase, a.date_schedule)
        if halt == True:
            a.time_schedule = time
            text = "Напишите количетсво мест \n\n\nБоту нужно прислать число (однозначное, двузначное или трехзначное)"
            kbd = None
            a.level = LEVEL3
        else:
            text = "Вы ввели не время\nНапишите мне время в формате: ЧЧ:ММ\n\n\nОБЯЗАТЕЛЬНО между ЧЧ и ММ поставьте следующие символы: '-' ',' '.' или пробел"
            kbd = None
    elif a.level == LEVEL3:
        if IntCheck(phrase) == True:
            a.seats_schedule = phrase
            text = "Расписание успешно обновлено\nДобро пожаловать в главное меню"
            kbd = nav.MenuOptions
            database.NewScheduleGame(id, phrase)
            a.level = OPTIONS
            a.act = "divarication"
        else:
            text = "Вы ввели не число или же это число больше чем трехзначное значение\n\nПожалуйста, введите число, соблюдая все условия, а не что то еще\n\n\nБоту нужно прислать число (однозначное, двузначное или трехзначное)"
            kbd = None
    prmode = None
    halt = None
    spreadsheet = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)

def REG(a: Admin, id: int, phrase: str):
    halt = False
    if a.level == START:
        text = "Приветсвую Вас в нашем боте! Этот бот возможно нужен вам, только в том случае, если вы купили его первую часть и вам нужна админская чаcть))\nЕсли да - то нажмите на конопку снизу"
        kbd = nav.ComStartReg
        a.level = LEVEL1
        fixed = None
    elif a.level == LEVEL1:
        if phrase == "Зарегистрироваться":
            database.IntermediateAction(id, a.level)
            text = "Введите пароль"
            kbd = None
            a.level = LEVEL2
        else:
            text = "Приветсвую Вас в нашем боте! Этот бот возможно нужен вам, только в том случае, если вы купили его первую часть и вам нужна админская чаcть))\nЕсли да - то нажмите на конопку снизу"
            kbd = nav.ComStartReg
        fixed = None
    elif a.level == LEVEL2:
        value = CheckPassword(phrase)
        if value == False:
            text = "Пароль не верный! Попробуйте еще..."
            kbd = None
            fixed = None
        else:
            a.level = LEVEL3
            text = """Вот пара рекомендаций, как мной пользоваться:
1. Узнать кто записался:
        Вы выбираете вид спорта, дату, время и вам показывается кто зарегестрировался на эту игру, 
        так же именно через эту функцию вы сможите связаться с участником 
        (Если он зарегестрировался через бота, то можно будеть нажать на его имя и перейти с ним в диалог, 
        а если нет - то тогда просто посмотрите контактную информацию и свяжитесь с ним сами.)
2. Настроить расписание:
        С помощью этой функции бота Вы сможите настроить расписание, а именно: Добавить или Удалить
3. Создать нового пользователя:
        Нажав на эту кнопку вы сможете создать нового пользователя (как бы это странно не было).
        Данная функция предназначена для того, чтоб когда Вам звонят и просятся записать Вас их на игру, то для начала вы можите создать 
        профиль этому пользолвателю, но этим профилем сможите пользоватся только Вы
4. Зарегестрировать пользователя на игру:
        Это функция продолжение предыдущей и не только. Тут Вы можите записать ЛЮБОГО пользователя на игру, который уже есть в системе
5. Настроить/Удалить пользователя:
        Думаю, название этой кнопки все и так за себя говорит
6. Получить отчет о деятельности бота:
        Нажав на эту кнопку бот вышлет Вам html файл, который Вам надо будет открыть и там будет таблица из всей информации по расписанию
    
    
    
P.S. Если чо, то вот моя главная команда /menu она возвратит Вас из любой точки бота в главное меню, естсественно без сохранения прогресса"""
            
            kbd = nav.Next
            fixed = True
           # kbd = nav.MenuOptions
    elif a.level == LEVEL3:
        text = "Вот опции которые вам дотупны:"
        kbd = nav.MenuOptions
        a.level = OPTIONS
        fixed = None
        a.act = "divarication"
    prmode = None
    spreadsheet = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)

def MenuOptions(a: Admin, id: int, phrase: str):
    halt = False
    if phrase in ('Узнать кто записался', 'Настроить расписание', 'Зарегестрировать пользователя'):
        text = "Выберите вид спорта:"
        kbd = nav.MenuSports
        if phrase == 'Узнать кто записался':
            a.act = "view registered users"
        elif phrase == 'Настроить расписание':
            a.act = "schedule setting"
        elif phrase == 'Зарегестрировать пользователя':
            a.act = "registration new user"
        a.level = START
        spreadsheet = None
    elif phrase == "Создать нового пользователя":
        a.act = "create new user"
        text = "Выберите откуда он/она:"
        kbd = nav.MenuFrom
        a.level = START
        spreadsheet = None
    elif phrase == "Настроить пользователя":
        a.act = "сhange user"
        text = "Выберите действие"
        kbd = nav.Do
        a.level = START
        spreadsheet = None
    elif phrase == "Отчет":
        a.act = "report table"
        text = None
        spreadsheet = CreateTable()
        kbd = nav.WatNext
    else:
        text = "!!!АЛЕ ДА, НА ДАННЫЙ МОМЕНТ Я ВОСПРИНИМАЮ ТОЛЬКО НАЖАТИЯ НА КНОПКИ!!!\n\n\nВыберите интересующю Вас опцию"
        kbd = nav.MenuOptions
    database.Action(id, a.act)
    prmode = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)    


def CreateTable():
    data = database.CreateTable()
    html_table = "<table>"
    html_table += "<tr><th>Вид спорта</th><th>Дата проведения</th><th>Время проведения</th><th>Свободные места</th></tr>"
    
    for row in data:
        sport, date, time, seats = row
        html_table += f"<tr><td>{sport}</td><td>{date}</td><td>{time}</td><td>{seats}</td></tr>"

    html_table += "</table>"

    with open("html.html", "w") as html_file:
        html_file.write("<html><body>")
        
        html_file.write('<style>table {margin: 0 auto; text-align: center;}</style>')
        html_file.write('<style>td {padding-top: 10px; padding-bottom: 10px;}</style>')
        html_file.write('<style>th {font-size: 25px; padding: 10px;}</style>')
        html_file.write("</head><body>")
        html_file.write(html_table)
        html_file.write("</body></html>")

    with open("html.html", "r") as html_file:
        return html_file.read()

    


def CreateNewUser(a: Admin, id: int, phrase: str):
    halt = False
    if a.level == START:
       # id_newuser = db.IdNewUser()
        text = "Напишите имя нового пользователя"
        kbd = None
        a.fromwhere_new_user = phrase
        a.level = LEVEL1
    elif a.level == LEVEL1:
        text = "Напишите фамилию нового пользователя"
        kbd = None
        a.name_new_user = phrase
        a.level = LEVEL2
    elif a.level == LEVEL2:
        text = "Напишите предпочтительный язык нового пользователя"
        kbd = None
        a.lastname_new_user = phrase
        a.level = LEVEL3
    elif a.level == LEVEL3:
        text = "Напишите номер телефона нового пользователя"
        kbd = None
        a.language_new_user = phrase
        a.level = LEVEL4
    elif a.level == LEVEL4:
        text = "Новый пользователь успешно создан!\nВозвращаю вас в главное меню"
        kbd = nav.MenuOptions
        a.phonenum_new_user = phrase
        database.CreateNewUser(id, phrase)
        a.act = "divarication"
        a.level = OPTIONS
    prmode = None
    spreadsheet = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)


    '''
    if a.level == START:
        #REG
        if a.act == "registation":
            text = "Приветсвую Вас в нашем боте! Этот бот возможно нужен вам, только в том случае, если вы купили его первую часть и вам нужна админская чаcть))\nЕсли да - то нажмите на конопку снизу"
            kbd = nav.ComStartReg
            a.level = LEVEL1
        #Reg For Game Users
        elif a.act == "view registered users":
            days = db.GamesWithUsers(phrase)
            if days == []:
                text == "Никого нет\nВыберите вид спорта:"
                kbd = nav.MenuSports
                a.level = START
                a.act = None
                db.Action(id, a.act)
            else:
                text = "Выберите дату:"
                kbd = nav.kbdata(days)
                db.NewTableInformation(id, phrase, a.level, a.act)
                a.level = LEVEL1
        #Change schedule
        elif a.act == "schedule setting":
            text = "Введите дату:"
            kbd = None
            a.level = LEVEL1
        #Create New User
        elif a.act == "create new user":
            CreateNewUser(a, id, phrase)
    elif a.level == LEVEL1:
        #REG
        if a.act == "registation":
            if phrase == "Зарегистрироваться":
                db.IntermediateAction(id, a.level)
                text = "Введите пароль"
                kbd = None
                a.level = LEVEL2
            else:
                text = "Приветсвую Вас в нашем боте! Этот бот возможно нужен вам, только в том случае, если вы купили его первую часть и вам нужна админская чаcть))\nЕсли да - то нажмите на конопку снизу"
                kbd = nav.ComStartReg
        #Reg For Game Users
        elif a.act == "view registered users":
            times = db.TimeOfGamesWithUsers()
        #Create New User
        elif a.act == "create new user":
            CreateNewUser(a, id, phrase)
    elif a.level == LEVEL2:
        #REG
        if a.act == "registation":
            value = CheckPassword(phrase)
            if value == False:
                text = "Пароль не верный! Попробуйте еще..."
                kbd = None
            else:
                a.level = LEVEL3
                text = "Вот опции которые вам дотупны:"
                kbd = nav.MenuOptions
        #Create New User
        elif a.act == "create new user":
            CreateNewUser(a, id, phrase)
    elif a.level == LEVEL3 or a.level == OPTIONS:
        #Create New User
        if a.act == "create new user":
            CreateNewUser(a, id, phrase)
        #Menu Options
        if phrase in ("Узнать кто записался", "Настроить расписание", "Зарегестрировать пользователя"):
            text = "Выберите вид спорта:"
            kbd = nav.MenuSports
            if phrase == "Узнать кто записался":
                a.act = "view registered users"
            elif phrase == "Настроить расписание":
                a.act = "schedule setting"
            elif phrase == "Зарегестрировать пользователя":
                a.act = "registration new user"
            a.level = START
            db.Action(id, a.act)
        elif phrase == "Создать нового пользователя":
            a.act = "create new user"
            text = "Выберите откуда он/она:"
            kbd = nav.MenuFrom
            a.level = START
            db.Action(id, a.act)
    elif a.level == LEVEL4:
        #Create New User
        if a.act == "create new user":
            CreateNewUser(a, id, phrase)
    '''



def RegAdUs(a:Admin, phrase):
    database.RegAdUs(a.sport_reg_ad_us, a.date_reg_ad_us, a.time_reg_ad_us, a.seats_reg_ad_us, a.payment_reg_ad_us, phrase, a.id)


def SeatsCheck(id: int, seat: str) -> bool:
    free_seats = database.HowMutchSeats(id)
    if int(seat) > free_seats:
        halt = False
    else:
        update_seats = free_seats - int(seat)
        database.BalanceOfTheUniverse(update_seats, id)
        halt = True
    return halt




def DateCheck(date_click) -> bool:
    if isinstance(date_click, str):
        halt, date  = DateCheck2(date_click)
    else:
        new_date_click = str(date_click)
        halt, date = DateCheck2(new_date_click)
    return halt, date


def DateCheck2(date_click: str):
    date = None
    if re.findall(r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}', date_click):
        date_pattern = r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}'
        match = re.search(date_pattern, date_click)
        if match:
            date_match = match.group(0)
            components = re.findall(r'\d+', date_match)
            day, month, year = map(int, components)
            print(day, month, year)
            if ValidDate(day, month, year) and datetime.date(year, month, day) >= datetime.date.today():
                date = (day*1)+(month*100)+(year*10000)
                halt = True
            else:
                print("дада я тут")
                halt = False
        else:
            halt = False
    else:
        halt = False
    return halt, date


def ValidDate(d: int, m: int, y: int):
    try:
        _ = datetime.date(y, m, d)
        res = True
    except:
        res = False
    return res

def TimeCheck(time_click, date) -> bool:

    year = date//10000
    month = (date-(year*10000))//100
    day = (date-(year*10000)-(month*100))//1
    date_str = f"{day}-{month}-{year}"


    if isinstance(time_click, str):
        halt, time = TimeCheck2(time_click, date_str)
    else:
        new_time_click= str(time_click)
        halt, time = TimeCheck2(new_time_click, date_str)
    return halt, time


def TimeCheck2(time_click: str, date: str):
    halt = False
    time = None
    print("TIME =",time_click, "DATE =", date)
    if re.findall(r'\d{1,2}[^0-9]+\d{1,2}', time_click):
        time_pattern = r'\d{1,2}[^0-9]+\d{1,2}'
        match = re.search(time_pattern, time_click)
        if match:
            time_match = match.group(0)
            components = re.findall(r'\d+', time_match)
            hour, minute = map(int, components)
            
            if re.findall(r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}', date):
                date_pattern = r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}'
                match = re.search(date_pattern, date)
                if match:
                    date_match = match.group(0)
                    components = re.findall(r'\d+', date_match)
                    day, month, year = map(int, components)
                    print(hour, minute, day, month, year)
                    
                    if ValidTime(hour, minute) and datetime.datetime(year, month, day, hour, minute) > datetime.datetime.now():
                        halt = True
                        time = (hour * 100) + minute
        else:
            halt = False
    
    return halt, time

def ValidTime(hr: int, min: int):
    try:
        _ = datetime.time(hr, min)
        res = True
    except:
        res = False
    return res

def IntCheck(mes) -> bool:
    if isinstance(mes, str):
        halt = IntCheck2(mes)
    else:
        new_mes= str(mes)
        halt = IntCheck2(new_mes)
    return halt

def IntCheck2(mes: str) -> bool:
    if re.fullmatch(r'^\d{1,2}$', mes):
        halt = True
    else:
        halt = False
    return halt


def EvPrevMsgId(uid: int, name: str, lname: str, usname: str):
    mes_id = database.RecognizeExMesID(uid, name, lname, usname)
    return mes_id

def RetainPrevMsgId(uid: int, m_id: int):
    database.AddNewMesID(uid, m_id)

def RetrieveAdmin(uid: int) -> Admin:
    a = Admin()
    a.id = uid
    a.name = None
    a.surname = None
    a.username = None
    a.act = None
    a.sport_check_users = None
    a.date_check_users = None
    a.time_check_users = None
    a.user_id_check_users = None
    a.fromwhere_new_user = None
    a.name_new_user = None
    a.lastname_new_user = None
    a.language_new_user = None
    a.phonenum_new_user = None
    a.sport_schedule = None
    a.date_schedule = None
    a.time_schedule = None
    a.seats_schedule = None
    a.sport_reg_ad_us = None
    a.date_reg_ad_us = None
    a.time_reg_ad_us = None
    a.seats_reg_ad_us = None
    a.payment_reg_ad_us = None
    a.user_id_change_user = None
    a.action_change_user = None

    a.level = None
    (a.id, a.name, a.surname, a.username, a.act, a.sport_check_users, a.date_check_users, a.time_check_users, a.user_id_check_users,
    a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user,
    a.sport_schedule, a.date_schedule, a.time_schedule, a.seats_schedule, a.sport_reg_ad_us, a.date_reg_ad_us,
    a.time_reg_ad_us, a.seats_reg_ad_us, a.payment_reg_ad_us, a.user_id_change_user, a.action_change_user, a.level) = database.RecallAdmin(uid)
    if a.level == NEGATIVE:
        a.level = START
    return a

    #else:
     #   a.level = db.LevelAdmin(uid, "value")
    #return a


def CheckPassword(text: str) -> bool:
    if database.Password(text) == None:
        value = False
    else:
        value = True
    return value


def RetainAdmin(a: Admin):
    database.RetainAdmin(a.id, a.name, a.surname, a.username, a.act, a.sport_check_users, a.date_check_users, a.time_check_users, a.user_id_check_users,
    a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user, a.sport_schedule, a.date_schedule, a.time_schedule, a.seats_schedule, 
    a.sport_reg_ad_us, a.date_reg_ad_us, a.time_reg_ad_us, a.seats_reg_ad_us, a.payment_reg_ad_us, a.user_id_change_user, a.action_change_user, a.level, a.id)
    #db.UpdateAdmin(a.id, a.level, a.data_act, a.act)