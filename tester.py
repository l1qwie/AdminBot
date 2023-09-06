#from admin import DispatchPhrase, DateCheck, TimeCheck
import admin
import keyboards as nav
from dbfortests import TestDB
import database
import random

tdb = TestDB("..\\bot(for_all)\\test_database.db")


#Intermediate test

    

def T2():
    dates = database.GamesWithUsers('volleyball')
    times = database.TimeOfGamesWithUsers(738070596, dates[0])
    print(dates)
    print(times)

def TestingNamer (name: str, nick: str) -> str:
    return name + nick

def FindCrashes():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    tdb.DelAllInSch(738070596)
    first = ["dhjkfhjkdfhjkdfhjk", 1111111111, "volleyball", "volleyballll", "enything else", "football"]
    for fitem in first:
        tdb.Adjustment("schedule setting", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fitem)
        if fitem in ("volleyball", "football"):
            assert(text == "Напишите дату проведения игры\nОбязательно в таком формате: ДД-ММ-ГГГГ\n\n\n ОБЯЗАТЕЛЬНО между ДД, ММ и ГГГ поставьте следующие символы: '-' ',' '.' или пробел")
            assert(kbd == None)
            print("дада я")
        else:
            assert(text == "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ\n\nВыбрите вид спорта")
            assert(kbd == nav.MenuSports)
    tdb.CustomSport("volleyball", 738070596)
    second = ['asjhdahjksdhjkas', '11111111', 1111111, "14-07-2024", "06,02,2024", "20.12.2024", '04 02 2025', "66-27-2055", "76,27,2055" "56.57.2035", "33 55 2333", "15-07,2024", "24.07 2024"]
    for sitem in second:
        tdb.Adjustment("schedule setting", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sitem)
        if admin.DateCheck(sitem) == False:
            assert(text == "Вы ввели не дату или же дату, но она меньше чем сегодняшнее число\nНапишите дату\n\n\nОБЯЗАТЕЛЬНО между ДД, ММ и ГГГ поставьте следующие символы: '-' ',' '.' или пробел")
            assert(kbd == None)
        else:
            assert(text == "Напишите время проведения игры в формате: ЧЧ:ММ\n\n\nОБЯЗАТЕЛЬНО между ЧЧ и ММ поставьте следующие символы: '-' ',' '.' или пробел")
            assert(kbd == None)
            tdb.Adjustment("schedule setting", 1, 738070596)
    tdb.CustomDate("14-07-2024", 738070596)
    third = ["12:00", "22 02", "14.45" "12,15", "24:01", "00.00", "12", "12 6"]
    for thitem in third:
        tdb.Adjustment("schedule setting", 2, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, thitem)
        bruh, time = admin.TimeCheck(thitem)
        if bruh == False:
            assert(text == "Вы ввели не время\nНапишите мне время в формате: ЧЧ:ММ\n\n\nОБЯЗАТЕЛЬНО между ЧЧ и ММ поставьте следующие символы: '-' ',' '.' или пробел")
            assert(kbd == None)
        else:
            assert(text == "Напишите количетсво мест \n\n\nБоту нужно прислать число (однозначное, двузначное или трехзначное)")
            assert(kbd == None)
            tdb.Adjustment("schedule setting", 2, 738070596)
    tdb.CustomTime("12:00", 738070596)
    fourth = [1111, 2, "Тристо", 55, 12, "2 3", "4 56 77 zzzzz"]
    for fitem in fourth:
        tdb.Adjustment("schedule setting", 3, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fitem)
        if admin.IntCheck(fitem) == False:
            assert(text == "Вы ввели не число или же это число больше чем трехзначное значение\n\nПожалуйста, введите число, соблюдая все условия, а не что то еще\n\n\nБоту нужно прислать число (однозначное, двузначное или трехзначное)")
            assert(kbd == None)
        else:
            assert(text == "Расписание успешно обновлено\nДобро пожаловать в главное меню")
            assert(kbd == nav.MenuOptions)
            tdb.Adjustment("schedule setting", 3, 738070596)


#Global test
def GlobalTest():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    tdb.ResetUser(738070596)
    StartRegistration()
    option_button, sport_button, from_where_button, payment_button, choice_button, changes_button = AllButtons()
    option_answers_text, sport_answers_text, fromwhere_answers_text, inf_answer_text, schedule_answer_text, create_new_user_answer_text, answers_about_updates = AnswersBot()
    option_answers_kb, sport_answers_kb, inf_answer_kb = KbAnswersBot()
    inf_about_user, inf_schedule, updated_inf = PotantionalAnswersofUser()
    #Main Action
    op = 0
    misstake = False
    while op < len(option_button):
        MenuOp(option_button[op], option_answers_text, option_answers_kb, op)
        sp = 0
        if op <= 2:
            while sp < len(sport_button):
                if op == 0:
                    if misstake is not True:
                        misstake = ViewWhoWaiting(sport_button[sp])
                    else:
                        sp += 1
                elif op == 1:
                    ChangeSchedule(sport_button[sp], inf_schedule, schedule_answer_text)
                elif op == 2:
                    RegForGameUser(sport_button[sp], payment_button)
                sp += 1
        elif op == 3:
            CreaterNewUser(from_where_button, inf_about_user, inf_answer_text)
        elif op == 4:
            ChangeUser(choice_button, changes_button, create_new_user_answer_text, answers_about_updates, updated_inf)
        elif op == 5:
            ReportWork(option_button[op])
        op += 1
    



def StartRegistration():
    #начало
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "sdhfkjdhjk")
    assert(text == "Приветсвую Вас в нашем боте! Этот бот возможно нужен вам, только в том случае, если вы купили его первую часть и вам нужна админская чаcть))\nЕсли да - то нажмите на конопку снизу")
    assert(kbd == nav.ComStartReg)
    #Начало регистриции
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "Зарегистрироваться")
    assert(text == "Введите пароль")
    #Окончательная регистрация
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "111")
    assert(text == """Вот пара рекомендаций, как мной пользоваться:
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
    
    
    
P.S. Если чо, то вот моя главная команда /menu она возвратит Вас из любой точки бота в главное меню, естсественно без сохранения прогресса""")
    assert(kbd == nav.Next)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "next")
    assert(text == "Вот опции которые вам дотупны:")
    assert(kbd == nav.MenuOptions)

def AllButtons():
    #Данные Меню опций
    options = ['Узнать кто записался', 'Настроить расписание', 'Зарегестрировать пользователя', 'Создать нового пользователя', "Настроить пользователя", "Отчет"]
    sports = ['volleyball', 'football']
    from_where = ['tg', 'whatsapp', 'viber', 'calls']
    payment = ['cash', 'card']
    choice = ["setuser", "deluser"]
    changes = ["fronwhere", "name", "lastname", "language", "phonenum"]

    return options, sports, from_where, payment, choice, changes

def AnswersBot():
    option_answers_text = ['Выберите вид спорта:', 'Выберите откуда он/она:', 'Выберите действие']
    sport_answers_text = ['Выберите дату:', 'Никого нет\nВыберите вид спорта:', 'Введите дату:']
    fromwhere_answers_text = ['Напишите как его зовут (Имя)']
    inf_answer_text = ['Напишите фамилию нового пользователя', 'Напишите предпочтительный язык нового пользователя', 'Напишите номер телефона нового пользователя', 'Новый пользователь успешно создан!\nВозвращаю вас в главное меню']
    schedule_answer_text = ["Напишите время проведения игры в форманте ЧЧ:ММ", "Напишите количетсво мест", "Расписание успешно обновлено\nДобро пожаловать в главное меню"]
    create_new_user_answer_text = ["Выберите откуда пользователь", "Напишите имя", "Напишите фамилию", "Напишите предпочитаемый язык", "Напишите номер телефона"]
    answers_about_updates = ["Месенджер пользователя измененен", "Имя изменено", "Фамилия изменена", "Язык изменен", "Телефон изменен"]

    return option_answers_text, sport_answers_text, fromwhere_answers_text, inf_answer_text, schedule_answer_text, create_new_user_answer_text, answers_about_updates


def KbAnswersBot():
    option_answers_kb = [nav.MenuSports, nav.MenuFrom, nav.Do]
    sport_answers_kb = [nav.kbdata(database.GamesWithUsers('volleyball')), nav.kbdata(database.GamesWithUsers('football')), nav.MenuSports]
    inf_answer_kb = [nav.MenuOptions]

    return option_answers_kb, sport_answers_kb, inf_answer_kb

def PotantionalAnswersofUser():
    inf = ['Вова', 'Киров', 'русский', '+79034241133']
    inf_schedule = ["15-12-2023", "11:00", "11"]
    updated_inf = ["viber", "Александр", "Белый", "РУССКИЙ", "+11231231241"]

    return inf, inf_schedule, updated_inf
    op = 0
    #Данные вид спорта
    sp = 0
    dt = 0
    #Данные откуда пользователь
    fw = 0

    inf = ['Вова', 'Киров', 'русский', '+79034241133']
    inf_count = 0

    #Данные для заполнения расписания
    inf_schedule = ["15-12-2023", "11:00", "11"]

    #Данные для регистрации пользователя на игру
    dates = database.AllFreeDates
    times = database.TimesOfFreeDates
    free_seats = database.SeatsofTimesofDateofSport

    #Данные для настройки пользователя
    updated_inf = ["viber", "Александр", "Белый", "РУССКИЙ", "+11231231241"]


def ViewWhoWaiting(sport: str) -> bool:
    tdb.Adjustment("view registered users", 0, 738070596)
    tdb.DelAllInAct(738070596)
    dates = database.GamesWithUsers(sport)
    misstake = False
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sport)
    dt = 0
    if database.Nobody() == True:
        assert(text == "Вообще никто не забронировал места на игры, так что нигде никого нет!\n\n\n\nВозвращаю вас в главное меню")
        assert(kbd == nav.MenuOptions)
        misstake = True
    elif dates == []:
        assert(text == "Никого нет\nВыберите вид спорта:")
        assert(kbd == nav.MenuSports)
    else:
        while dt < len(dates):
            tdb.DelBeforeSport(738070596, 1)
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, dates[dt])
            assert(text == "Выберите время проведения игры:")
            (times, seats) = database.TimeOfGamesWithUsers(738070596, dates[dt])
            assert(kbd == nav.kbtime(times, seats))
            tm = 0
            print(times)
            while tm < len(times):
                tdb.DelBeforeDate(738070596, 2)
                (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, times[tm])
                name_users, id_users = database.UsersOfGamesWithUsers(738070596, times[tm])
                assert(text == f"На эту игру зарегестрировалось {len(name_users)}\nНажмите на имена ниже чтоб узнать потробную информацию:")
                assert(kbd == nav.kbnames(name_users, id_users))
                alllen = 0
                while alllen < (len(id_users)):
                    tdb.ChangeLvl(738070596, 3)
                    idishnik = id_users[alllen]
                    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, int(idishnik))
                    (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(738070596, int(idishnik))
                    if username != "Информация отсутствует":
                        assert(prmode == "HTML")
                        nick = (f"t.me/{username}")
                        name = TestingNamer(name, nick)
                    assert(text == f"Вот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним")
                    assert(kbd == nav.BackorMenu)
                    alllen += 1
                tm += 1 
            dt += 1
    return misstake

def ChangeSchedule(sport: str, inf: list, answer: list):
    tdb.Adjustment("schedule setting", 0, 738070596)
    tdb.DelAllInSch(738070596)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sport)
    assert(text =="Напишите дату проведения игры\nОбязательно в таком формате - ДД-ММ-ГГГГ")
    assert(kbd == None)
    sch = 0
    halt = True
    while sch < len(inf) and halt == True:
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, inf[sch])
        if sch == 0 and admin.DateCheck(inf[sch]) == False:
            assert(text == "Вы ввели не дату или же дату, но она меньше чем сегодняшнее число\nНапишите дату")
            halt = False
        elif sch == 1 and admin.TimeCheck(inf[sch]) == False:
            assert(text == "Вы ввели не время\nНапишите мне время в форманте ЧЧ:ММ")
            halt = False
        else:
            assert(text == answer[sch])
            if sch + 1 == len(inf):
                assert(kbd == nav.MenuOptions)
            else:
                assert(kbd == None)
        sch += 1

def RegForGameUser(sport: str, payment: list):
    #Registired Admin User
    tdb.Adjustment("registration new user", 0, 738070596)
    tdb.DelAllRegAdUs(738070596)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sport)
    assert(text == "Выберете дату:")
    assert(kbd == nav.kbdata(database.AllFreeDates(sport)))
    dt = 0
    datesofsport = database.GamesWithUsers(sport)
    while dt < len(datesofsport):
        tdb.DelBeforeSportreg_ad(1, 738070596)
        timeofdateofsport = database.TimesOfFreeDates(datesofsport[dt], sport)
        seatsofdateofsport = database.SeatsofTimesofDateofSport(datesofsport[dt], sport)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, datesofsport[dt])
        assert(text == "Выберите время проведения игры")
        assert(kbd == nav.kbtime(timeofdateofsport, seatsofdateofsport))
        tm = 0
        while tm < len(timeofdateofsport):
            tdb.DelBeforeDatereg_ad(2, 738070596)
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, timeofdateofsport[tm])
            assert(text == "Выберите или введите желаемое количетсво мест")
            assert(kbd == nav.FrequentChoice)
            random_number = random.randint(1, 10)
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, random_number)
            if halt == True:
                assert(text == "Выберите способ оплаты")
                #(names_users, id_users) = database.db.AllUsers()
                assert(kbd == nav.KbPay)#kbnames(names_users, id_users))
            else:
                assert(text == "Вы ввели не цифру или же вы ввели цифру котороая больше чем свободныйх мест на эту игру")
                assert(kbd == None)
            p = 0
            while p < len(payment) and halt == True:
                tdb.DelBeforePaymentreg_ad(4, 738070596)
                (names_users, id_users) = database.AllUsers()
                (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, payment[p])
                assert(text == "Выберите пользователя")
                assert(kbd == nav.kbnames(names_users, id_users))
                us = 0
                while us < len(id_users):
                    print("меня тут нет")
                    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, id_users[us])
                    assert(text == "Мои поздравления! Вы зарегестрировали этого пользователя на игру.\nВозвращаю Вас в главное меню")
                    assert(kbd == nav.MenuOptions)
                    tdb.Updatelvl(738070596, 5)
                    database.DelRegAdUs(738070596, id_users[us])
                    print("All is Okay")
                # db.DelBeforePaymentreg_ad(5, 738070596)
                    us += 1
                p += 1
            tm += 1
        dt += 1


def CreaterNewUser(from_where: list, inf: list, inf_answer_text: list):
    #Create New User
    fw = 0
    cnu = 0
    while fw < len(from_where):
        tdb.Adjustment("create new user", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, from_where[fw])
        assert(text == "Напишите имя нового пользователя")
        assert(kbd == None)
        cnu = 0
        while cnu < len(inf):
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, inf[cnu])
            assert(text == inf_answer_text[cnu])
            if cnu + 1 == len(inf):
                assert(kbd == nav.MenuOptions)
            else:
                assert(kbd == None)
            cnu += 1
        fw += 1


def ChangeUser(choice: list, answers_changes: list, trumpet_call: list, answers_about_updates: list, updated_inf: list):
    ch = 0
    while ch < len(choice):
        tdb.Adjustment("сhange user", 0, 738070596)
        tdb.DelAllchus(738070596)
        (names_users, id_users) = database.AllUsers()
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, choice[ch])
        assert(text == "Выберите пользователя")
        assert(kbd == nav.kbnames(names_users, id_users))
        print(len(id_users), id_users)
        uid = 0
        if ch == 0:
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, id_users[uid])
            assert(text == "Выберите что вы хотите изменить")
            assert(kbd == nav.Enumeration)
            chang = 0
            while chang < len(answers_changes):
            # tdb.Updatelvl(738070596, 2)
                (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, answers_changes[chang])
                assert(text == trumpet_call[chang])
                if chang == 0:
                    assert(kbd == nav.MenuFrom)
                else:
                    assert(kbd == None)
                (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, updated_inf[chang])
                assert(text == answers_about_updates[chang])
                assert(kbd == nav.Enumeration)
                chang += 1
        else:
            (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, id_users[uid])
            assert(text == "Пользователь удален. Все данные, все регистрации, вообще вся информация, которая могла быть в боте, благополучно удалена\n\n\nВозвращаю вас в главное меню")
            assert(kbd == nav.MenuOptions)
        ch += 1


def ReportWork(option: str):
    #Report
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    html_file = admin.CreateTable()
    tdb.Adjustment("divarication", 3, 738070596)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, option)
    html_file = admin.CreateTable()
    assert(spreadsheet == html_file)
    assert(kbd == nav.WatNext)

def MenuOp(option: str, op_answers_text: list, op_answers_kb: list, op: int):
    tdb.ResetOptions(738070596)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, option)
    if op < 3:
        print("!!!!", op_answers_text[0])
        assert(text == op_answers_text[0])
        assert(kbd == op_answers_kb[0])
    elif op == 3:
        assert(text == op_answers_text[1])
        assert(kbd == op_answers_kb[1])
    elif op == 4:
        assert(text == op_answers_text[2])
        assert(kbd == op_answers_kb[2])
