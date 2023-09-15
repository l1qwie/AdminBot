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
    act_schedule: str
    game_id_schedule: int
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
    gid_notification: int
    uid_notification: int
    condition_notification: str
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
        a.act = "divarication"
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
    elif a.act == "notify the user":
        (text, kbd, prmode, halt, spreadsheet, fixed) = Notification(a, id, phrase)
    elif a.act == "report table":
        (text, kbd, prmode, halt, spreadsheet, fixed) = HTMLTable()
    elif a.act == "divarication":
        if phrase in ('Узнать кто записался', 'Настроить расписание', 'Создать нового пользователя', 'Зарегестрировать пользователя', 'Настроить пользователя', 'Отчет', 'notification'):
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
    print("TEXT =", text)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def HTMLTable():
    text = None
    kbd = nav.WatNext
    prmode = None
    halt = None
    fixed = None
    spreadsheet = CreateTable()
    return text, kbd, prmode, halt, spreadsheet, fixed


def Notification(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd = NotificationStart(a, phrase)
    elif a.level == LEVEL1:
        if a.condition_notification == "DELETE":
            text, kbd = NotificationDel(a, phrase)
        else:
            text, kbd = NotificationLevel1(a, phrase)
    elif a.level == LEVEL2:
        text, kbd = NotificationLevel2(a, phrase)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def NotificationStart(a: Admin, phrase: str):
    if IDNotifCheck(a.id, phrase):
        a.uid_notification = phrase
        (name, last_name, language, phone_number) = database.InfOfUser(int(phrase))
        (game_id, sport, date, time, status) = database.InfAboutGameofUser(int(phrase))
        a.gid_notification = game_id
        a.condition_notification = status
        if status == "DELETE":
            text = f"""Вот информация по этому пользователю:
- Имя: {name}
- Фамилия(если есть): {last_name}
- Предпочтительный язык: {language}
- Номер телефона(если был указан): {phone_number}



Информация об игре, которую вы редактировали или удалили, а у этого пользователя была запись на эту игру (это уже измененные данные):
- Вид спорта: {sport}
- Дата: {date}
- Время: {time}
- Состояние: {status}

Как только вы уведомите этого пользователя об изменеиях в расписании, то нажмите на кнопку 'Уведомлен', но так же
вы можите спокойно пойти и заниматься чем угодно другим, а бот напомнит вам об этом чуть позже. Так как это удаленная игра,
то никаких дальнейших к вам вопросов по поводу пользователя не будет."""
        else:
            text = f"""Вот информация по этому пользователю:
- Имя: {name}
- Фамилия(если есть): {last_name}
- Предпочтительный язык: {language}
- Номер телефона(если был указан): {phone_number}



Информация об игре, которую вы редактировали или удалили, а у этого пользователя была запись на эту игру (это уже измененные данные):
- Вид спорта: {sport}
- Дата: {date}
- Время: {time}
- Состояние: {status}

Как только вы уведомите этого пользователя об изменеиях в расписании, то нажмите на кнопку 'Уведомлен', но так же
вы можите спокойно пойти и заниматься чем угодно другим, а бот напомнит вам об этом чуть позже.


Как только вы уведомите этого пользователя об изменеиях в расписании, то нажмите на кнопку 'Уведомлен', но так же
вы можите спокойно пойти и заниматься чем угодно другим, а бот напомнит вам об этом чуть позже. 
Дальше я задам вам следующий вопрос: решил ли остаться пользователь на этой игре (уже измененной) или же отменил запись? 
Так что рекомендую задать этот же вопрос пользователю."""
        kbd = nav.Notif
        a.level = LEVEL1
    else:
        names, id_user = database.WhoNeedNotif(a.id)
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите пользователя."
        kbd = nav.kbnames(names, id_user)
    return text, kbd

def NotificationLevel1(a: Admin, phrase: str):
    if phrase == "Notif completed":
        text = "Что выбрал пользователь?"
        kbd = nav.UserDecision
        a.level = LEVEL2
    else:
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите действие."
        kbd = nav.Notif
    return text, kbd 

def NotificationDel(a: Admin, phrase: str):
    if phrase == "Notif completed":
        database.ChangeStatusUser()
        text = "Прекрасно! Возвращаю вас в Главное Меню"
        kbd = nav.MenuOptions
        a.level == OPTIONS
        a.act == "divarication"
    else:
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите действие."
        kbd = nav.Notif
    return text, kbd

def NotificationLevel2(a: Admin, phrase: str):
    if phrase in ("user wait", "user not wait"):
        if phrase == "user wait":
            database.SetupUs(a.id, "allright")
            text = "Ура! Пользователь решил оставить запись на эту игру!\n\n\nДобро пожаловать в Главное Меню"
        elif phrase == "user not wait":
            database.SetupUs(a.id, "DELETE")
            database.SeatsBack(a.id)
            text = "Ну что ж. Жаль. Но ничего не поделаешь\n\n\nДобро пожаловать в Главное Меню"
        kbd = nav.MenuOptions
        a.level = OPTIONS
        a.act = "divarication"
    else:
        text = "Я жду от вас нажатия на кнопку.\n\n\nЧто выбрал пользователь?"
        kbd = nav.UserDecision
    return text, kbd
        


def ChangeUsers(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd = ChangeUsersStart(a, id, phrase)
    elif a.level == LEVEL1:
        text, kbd = ChangeUserslvl1(a, id, phrase)
    elif a.level == LEVEL2:
        text, kbd = ChangeUserslvl2(a, id, phrase)
    elif a.level == LEVEL3:
        text, kbd = ChangeUserslvl3(a, id, phrase)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def ChangeUsersStart(a: Admin, id: int, phrase: str):
    if phrase in ("setuser", "deluser"):
        (names_users, id_users) = database.AllUsers()
        text = "Выберите пользователя"
        kbd = nav.kbnames(names_users, id_users)
        a.level = LEVEL1
        a.action_change_user = phrase
    else:
        text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\n\nВыберите действие"
        kbd = nav.Do
    return text, kbd


def ChangeUserslvl1(a: Admin, id: int, phrase: str):
    if IDCheck(phrase):
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
    else:
        text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\n\nВыберите пользователя"
        (names_users, id_users) = database.AllUsers()
        kbd = nav.kbnames(names_users, id_users)
    return text, kbd


def ChangeUserslvl2(a: Admin, id: int, phrase: str):
    if phrase in ("fronwhere", "name", "lastname", "language", "phonenum"):
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
    else:
        text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\n\nВыберите что вы хотите изменить"
        kbd = nav.Enumeration
    return text, kbd

def ChangeUserslvl3(a: Admin, id: int, phrase: str):
    if "nextaction" in (a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user):
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
    else:
        text = "Возникла каккая то непредвиденная ошибка, если она повториться - сообщите разработкику"
        a.act = "divarication"
        a.level = OPTIONS
        kbd = nav.MenuOptions
    return text, kbd
            


def RegistiredAdminUser(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd = RegistiredAdminUserStart(a, id, phrase)
    elif a.level == LEVEL1:
        text, kbd = RegistiredAdminUserlevel1(a, id, phrase)
    elif a.level == LEVEL2:
        text, kbd = RegistiredAdminUserlevel2(a, id, phrase)
    elif a.level == LEVEL3:
        text, kbd, halt = RegistiredAdminUserlevel3(a, id, phrase)
    elif a.level == LEVEL4:
        text, kbd = RegistiredAdminUserlevel4(a, id, phrase)
    elif a.level == LEVEL5:
        text, kbd = RegistiredAdminUserlevel5(a, id, phrase) 
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def RegistiredAdminUserStart(a: Admin, id: int, phrase: str):
    if phrase in ("volleyball", "football"):
        schedule = database.FindDates()
        if schedule == 0:
            text = "Нет ни одной добавленной игры в расписании! Добавьте сначала игру в расписание, а уже потом зарегистрируйте пользователя. \n\n\nГлавное меню"
            kbd = nav.MenuOptions
            a.act = "divarication"
            a.level = OPTIONS
        else:
            days = database.AllFreeDates(phrase)
            if days == []:
                text = "В расписании нет дат на этот вид спорта. Выберите другой вид спорта или создайте новую игру."
                kbd = nav.MenuSports
            else:
                a.sport_reg_ad_us = phrase
                text = "Выберите дату:"
                kbd = nav.kbdata(CreateDateList(days))
                a.level = LEVEL1
    else:
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите вид спорта."
        kbd = nav.MenuSports
    return text, kbd

def CreateTimeList(time: list) -> list:
    times_ready = []
    tm = 0
    while tm < len(time):
        hour = time[tm]//100
        minute = (time[tm]-(hour*100))//1
        time_str = f"{hour}:{minute}"
        times_ready.append(time_str)
        tm += 1
    return times_ready

def CreateDateList(days: list) -> list:
    list_for_dates = []
    dy = 0
    while dy < len(days):
        year = days[dy]//10000
        month = (days[dy]-(year*10000))//100
        day = (days[dy]-(year*10000)-(month*100))//1
        date_str = f"{day}-{month}-{year}"
        list_for_dates.append(date_str)
        dy += 1
    return list_for_dates

def RegistiredAdminUserlevel1(a: Admin, id: int, phrase: str):
    halt, date = DateCheck(phrase)
    if halt is not True:
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите дату."
        list_for_dates = CreateDateList(database.AllFreeDates(a.sport_reg_ad_us))
        kbd = nav.kbdata(list_for_dates)
    else:
        if date in (database.AllFreeDates(a.sport_reg_ad_us)):
            seats = database.SeatsofTimesofDateofSport(date, a.sport_reg_ad_us)
            a.date_reg_ad_us = date
            text = "Выберите время проведения игры"
            kbd = nav.kbtime(CreateTimeList(database.TimesOfFreeDates(date, a.sport_reg_ad_us)), seats)
            a.level = LEVEL2
        else:
            text = "Вы выбрали дату, но, к сожалению, это не подходящая дата для вас. Выберите ту, которая показана на кнопках"
            kbd = nav.kbdata(CreateDateList(database.AllFreeDates(a.sport_reg_ad_us)))
    return text, kbd

def RegistiredAdminUserlevel2(a: Admin, id: int, phrase: str):
    times = database.TimesOfFreeDates(a.date_reg_ad_us, a.sport_reg_ad_us)
    halt, timeschedule = TimeCheck(phrase, a.date_reg_ad_us)
    seats = database.SeatsofTimesofDateofSport(a.date_reg_ad_us, a.sport_reg_ad_us)
    if halt is True:
        if timeschedule in times:
            a.time_reg_ad_us = timeschedule
            text = "Выберите или введите желаемое количетсво мест."
            kbd = nav.FrequentChoice
            a.level = LEVEL3
        else:
            text = "Вы прислали мне время, но, к сожалению, это не то время, которое я вам предложил на кнопках. Выберите, пожалуйста, то, что на кнопках."
            kbd = nav.kbtime(CreateTimeList(times), seats)
    else:
        text = "Я жду от вас нажатия на кнопку.\n\n\nВыберите время проведения игры."
        kbd = nav.kbtime(CreateTimeList(times), seats)
    return text, kbd

def RegistiredAdminUserlevel3(a: Admin, id: int, phrase: str):
    halt = None
    if IntCheck(phrase):
        halt, upd_seats  = SeatsCheck(id, phrase)
        if halt is True:
            a.seats_reg_ad_us = int(phrase)
            text = "Выберите способ оплаты."
            kbd = nav.KbPay
            a.level = LEVEL4
            database.BalanceOfTheUniverse(upd_seats, id)
        else:
            text = "Вы ввели не цифру или ввели цифру, которая больше, чем количество свободных мест на эту игру.\n\n\nВыберите или введите желаемое количество мест."
            kbd = nav.FrequentChoice
    else:
        text = "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите или введите желаемое количество мест."
        kbd = nav.FrequentChoice
    return text, kbd, halt

def RegistiredAdminUserlevel4(a: Admin, id: int, phrase: str):
    if phrase in ("cash", "card"):
        (names_users, id_users) = database.AllUsers()
        a.payment_reg_ad_us = phrase
        text = "Выберите пользователя."
        kbd = nav.kbnames(names_users, id_users)
        a.level = LEVEL5
    else:
        text = "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите способ оплаты."
        kbd = nav.KbPay
    return text, kbd

def RegistiredAdminUserlevel5(a: Admin, id: int, phrase: str):
    if IDCheck(phrase):
        RegAdUs(a, phrase)
        text = "Мои поздравления! Вы зарегистрировали этого пользователя на игру.\nВозвращаю Вас в главное меню."
        kbd = nav.MenuOptions
        a.level = OPTIONS
        a.act = "divarication"
    else:
        text = "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите пользователя."
        (names_users, id_users) = database.AllUsers()
        kbd = nav.kbnames(names_users, id_users)
    return text, kbd

def ViewWhoReg(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd = ViewWhoRegStart(a, id, phrase)
    elif a.level == LEVEL1:
        text, kbd = ViewWhoReglevel1(a, phrase)
    elif a.level == LEVEL2:
        text, kbd, halt = ViewWhoReglevel2(a, id, phrase)
    elif a.level == LEVEL3:
        text, kbd, prmode = ViewWhoReglevel3(a, phrase)
    elif a.level == LEVEL4:
        text, kbd, prmode = ViewWhoReglevel4(a, id, phrase)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def ViewWhoRegStart(a: Admin, id: int, phrase: str):
    if phrase in ("volleyball", "football"):
        days_db = database.GamesWithUsers(phrase)
        if database.Nobody() == True:
            text = "Вообще никто не забронировал места на игры, так что нигде никого нет!\n\n\nВозвращаю Вас в главное меню."
            kbd = nav.MenuOptions
            a.level = OPTIONS
            a.act = "divarication"
        elif days_db != []:
            a.sport_check_users = phrase
            text = "Выберите дату:"
            kbd = nav.kbdata(CreateDateList(days_db))
            a.level = LEVEL1
        else:
            text = "Никого нет\nВыберите вид спорта:"
            kbd = nav.MenuSports
    else:
        text = "Я жду от Вас нажатия на кнопку!\n\nВыберите вид спорта."
        kbd = nav.MenuSports
    return text, kbd

def ViewWhoReglevel1(a: Admin, phrase: str):
    halt, date = DateCheck(phrase)
    if halt is True:
        if database.CheckDate(date, a.sport_check_users) != 0:
            (times, seats) = database.TimeOfGamesWithUsers(a.id, date)
            if times != []:
                a.date_check_users = date
                text = "Выберите время проведения игры:"
                kbd = nav.kbtime(CreateTimeList(times), seats)
                a.level = LEVEL2
            else:
                text = "Почему-то тут никого нет.\n\nВозвращаю Вас в главное меню."
                kbd = nav.MenuOptions
                a.level = START
                a.act = "divarication"
                #database.Action(id, a.act)
        else:
            text = "Вы прислали мне дату, но, к сожалению, мне нужна только дата, которую я вам предлагаю на кнопках"
            kbd = nav.kbdata(CreateDateList(database.GamesWithUsers(a.sport_check_users)))
    else:
        text = "Я жду от вас нажатия на кнопку!\n\nВыберите дату."
        kbd = nav.kbdata(CreateDateList(database.GamesWithUsers(a.sport_check_users)))
    return text, kbd


def ViewWhoReglevel2(a: Admin, id: int, phrase: str):
    halt, time = TimeCheck(phrase, a.date_check_users)
    (times, seats) = database.TimeOfGamesWithUsers(a.id, a.date_check_users)
    if halt is True:
        if database.CheckTime(a.date_check_users, a.sport_check_users, time) != 0:
            a.time_check_users = time
            (name_users, id_users) = database.UsersOfGamesWithUsers(id, time)
            text = f"На эту игру зарегистрировалось {len(name_users)}.\nНажмите на имена ниже, чтобы узнать подробную информацию:"
            kbd = nav.kbnames(name_users, id_users)
            a.level = LEVEL3
        else:
            text = "Вы прислали мне время, но, к сожалению, я жду от вас время, которое я вам предлагаю на кнопках\n\nВыберите время."
            kbd = nav.kbtime(CreateTimeList(times), seats)
    else:
        text = "Я жду от вас нажатия на кнопку!\n\nВыберите время."
        kbd = nav.kbtime(CreateTimeList(times), seats)
    return text, kbd, halt

def ViewWhoReglevel3(a: Admin, phrase: str):
    prmode = None
    if database.CheckUser(phrase) != 0:
        a.user_id_check_users = int(phrase)
        (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(a.id, a.user_id_check_users)
        if username != "Информация отсутствует":
            prmode = "HTML"
            nick = (f"t.me/{username}")
            name = namer(name, nick)
        text = f"Вот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним"
        kbd = nav.BackorMenu
        a.level = LEVEL4
    else:
        (name_users, id_users) = database.UsersOfGamesWithUsers(a.id, a.time_check_users)
        text = f"Я жду от Вас нажатия на кнопку!\n\nНа эту игру зарегистрировалось {len(name_users)}.\nНажмите на имена ниже, чтобы узнать подробную информацию:"
        kbd = nav.kbnames(name_users, id_users)
    return text, kbd, prmode

def ViewWhoReglevel4(a: Admin, id: int, phrase: str):
    prmode = None
    if phrase == "back":
        (name_users, id_users) = database.UsersOfGamesWithUsers(id, a.time_check_users)
        text = f"На эту игру зарегистрировалось {len(name_users)}.\nНажмите на имена ниже, чтобы узнать подробную информацию:"
        kbd = nav.kbnames(name_users, id_users)
        a.level = LEVEL3
    elif phrase == "menuop":
        text = "Добро пожаловать в Главное Меню"
        kbd = nav.MenuOptions
        a.level = OPTIONS
        a.act = "divarication"
    else:
        (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(id, a.user_id_check_users)
        if username != "Информация отсутствует":
            prmode = "HTML"
            nick = (f"t.me/{username}")
            name = namer(name, nick)
        text = f"Я жду от вас нажатия на кнопку!\n\nВот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним"
        kbd = nav.BackorMenu
    return text, kbd, prmode


def ChangeSchedule(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd, spreadsheet = ChangeScheduleStart(a, phrase)
    elif a.level == LEVEL1:
        if a.act_schedule == "new":
            text, kbd = ChangeSchedulelevel1(a, phrase, LEVEL2)
        elif a.act_schedule in ("setSche", "delSche"):
            text, kbd, spreadsheet = ChangeScheduleBegin(a, id, phrase)
    elif a.level == LEVEL2:
        if a.act_schedule == "new":
            text, kbd, halt = ChangeSchedulelevel2(a, phrase, LEVEL3)
        elif a.act_schedule == "setSche":
            text, kbd = ChangeSchedulelevel1(a, phrase, LEVEL3)
    elif a.level == LEVEL3:
        if a.act_schedule == "new":
            text, kbd, halt = ChangeSchedulelevel3(a, phrase, LEVEL4)
        elif a.act_schedule == "setSche":
            text, kbd, halt = ChangeSchedulelevel2(a, phrase, LEVEL4)
    elif a.level == LEVEL4:
        if a.act_schedule == "new":
            text, kbd = ChangeSchedulelevel4(a, id, phrase)
        elif a.act_schedule == "setSche":
            text, kbd, halt = ChangeSchedulelevel3(a, phrase, LEVEL5)
    elif a.level == LEVEL5:
        text, kbd = ChangeScheduleAlmostEnd(a, id, phrase)
    return (text, kbd, prmode, halt, spreadsheet, fixed)


def ChangeScheduleStart(a: Admin, phrase: str):
    spreadsheet = None
    if phrase in ("new", "setSche", "delSche"):
        a.act_schedule = phrase
        a.level = LEVEL1
        if phrase == "new":
            text = "Дальше бы будете создавать новую игру\n\n\nВыберите вид спорта."
            kbd = nav.MenuSports
        elif phrase in ("setSche", "delSche"):
            text = "Дальше вы будете редактировать ранее сделанное расписание на игру. Для этого вам нужно будет открыть файл, который я вам прислал, и выбрать игру, которую вы хотите изменить. Мне нужен только её порядковый номер."
            kbd = nav.WatNext
            spreadsheet = CreateTable()
            a.level = LEVEL1
    else:
        text = "Я жду от вас нажатия на кнопку!\n\nВыберите, что вас интересует."
        kbd = nav.SetSchedule
    return text, kbd, spreadsheet

def ChangeSchedulelevel1(a: Admin, phrase: str, level: int):
    if phrase in ("volleyball", "football"):
        a.sport_schedule = phrase
        text = "Напишите дату проведения игры.\nБот примет за дату любое ваше сообщение, которое будет соответствовать следующему условию: \nПервые 1 или 2 цифры в сообщении будут расцениваться как число. Вторые 1 или 2 цифры будут расцениваться как месяц. И дальше, 4 следующие цифры, которые будут идти подряд, будут расцениваться как год."
        kbd = None
        a.level = level
    else:
        text = "Я жду от вас нажатия на кнопку.\n\nВыберите вид спорта."
        kbd = nav.MenuSports
    return text, kbd


def ChangeScheduleBegin(a: Admin, id: int, phrase: str):
    if GameIdCheck(phrase):
        spreadsheet = None
        a.game_id_schedule = int(phrase)
        if a.act_schedule == "setSche":
            text = "Прекрасно! Вы выбрали номер игры, и теперь можете приступить к ее изменениям!\n\n\nВыберите вид спорта"
            kbd = nav.MenuSports
            a.level = LEVEL2
        else:
            (text, kbd) = ChangeScheduleEnd(a)
            database.ShadowRemoveGame(a.game_id_schedule)
    else:
        text = "Вы ввели не номер игры, а что то еще. Напоминаю, мне нужен только номер, т.е. мне нужно одно сообщение от вас содержащее только одну цифру."
        spreadsheet = CreateTable()
        kbd = nav.WatNext
    return text, kbd, spreadsheet


def ChangeSchedulelevel2(a: Admin, phrase: str, level: int):
    halt, date = DateCheck(phrase)
    if halt == True:
        a.date_schedule = date
        text = "Напишите время проведения игры. \nБот примет за время любое ваше сообщение, которое будет соответствовать следующему условию:\n Первые 1 или 2 цифры в сообщении будут расцениваться как часы. А вторые 1 или 2 цифры будут расцениваться как минуты."
        kbd = None
        a.level = level
    else:
        text = "Вы ввели не дату или дату, которая меньше сегодняшнего числа.\nНапишите дату."
        kbd = None
    
    return text, kbd, halt

def ChangeSchedulelevel3(a: Admin, phrase: str, level: int):
    halt, time = TimeCheck(phrase, a.date_schedule)
    if halt == True:
        a.time_schedule = time
        text = "Напишите количество мест.\n\nБоту нужно прислать число (однозначное или двузначное)."
        kbd = None
        a.level = level
    else:
        text = "Вы ввели не время.\nНапишите время."
        kbd = None
    return text, kbd, halt

def ChangeSchedulelevel4(a: Admin, id: int, phrase: str):
    if IntCheck(phrase) == True:
        a.seats_schedule = phrase
        text = "Расписание успешно обновлено.\nДобро пожаловать в Главное Меню."
        kbd = nav.MenuOptions
        database.NewScheduleGame(id, phrase)
        a.level = OPTIONS
        a.act = "divarication"
    else:
        text = "Похоже, вы ввели не количество мест, или же вы ввели число, которое больше, чем максимальное значение двузначного числа. Введите, пожалуйста, нужное вам количество мест."
        kbd = None
    return text, kbd

def ChangeScheduleAlmostEnd(a: Admin, id: str, phrase: str):
    if IntCheck(phrase):
        a.seats_schedule = phrase
        database.ChangeGame(id, phrase)
        (text, kbd) = ChangeScheduleEnd(a)
    else:
        text = "Похоже, вы ввели не количество мест, или же вы ввели число, которое больше, чем максимальное значение двузначного числа. Введите, пожалуйста, нужное вам количество мест."
        kbd = None
    return text, kbd


def ChangeScheduleEnd(a: Admin):
    countusers, adminusers = database.CountTGUsers(a.id)
    print("будтье так добры блять", countusers, adminusers, a.id)
    if adminusers != 0:
        database.UserWhoNeedNotif(a.id)
    if countusers == 0 and adminusers == 0:
        text = "Эту игру никто еще не ждет, так что уведомлять об изменениях пока что никого не нужно"
    else:    
        if countusers == 1:
            if adminusers == 1:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователю. Но также есть еще {adminusers} пользователь, который нуждается в том, чтобы вы его предупредили сами. (Он будет находиться в Главном Меню под кнопкой 'Уведомления')."
            elif adminusers > 1:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователю. Но также есть еще {adminusers} пользователей, которые нуждаются в том, чтобы вы предупредили их сами. (Они будут находиться в Главном Меню под кнопкой 'Уведомления')."
            else:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователю. Все пользователи уведомлены, и я ожидаю ответа."
        elif countusers > 1:
            if adminusers == 1:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователям. Но также есть еще {adminusers} пользователь, который нуждается в том, чтобы вы его предупредили сами. (Он будет находиться в Главном Меню под кнопкой 'Уведомления')."
            elif adminusers > 1:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователям. Но также есть еще {adminusers} пользователей, которые нуждаются в том, чтобы вы предупредили их сами. (Они будут находиться в Главном Меню под кнопкой 'Уведомления')."
            else:
                text = f"Расписание успешно обновлено. А также я уже выслал уведомление с просьбой пересмотреть свою запись на измененную игру {countusers} пользователям. Все пользователи уведомлены, и я ожидаю ответа."
        else:
            if adminusers == 1:
                text = f"Расписание успешно обновлено. Нет ни одного пользователя, который записался на игру через бота, так что мне некого уведомлять. Но также есть еще {adminusers} пользователь, который нуждается в том, чтобы вы его предупредили сами. (Он будет находиться в Главном Меню под кнопкой 'Уведомления')."
            elif adminusers > 1:
                text = f"Расписание успешно обновлено. Нет ни одного пользователя, который записался на игру через бота, так что мне некого уведомлять. Но также есть еще {adminusers} пользователей, которые нуждаются в том, чтобы вы предупредили их сами. (Они будут находиться в Главном Меню под кнопкой 'Уведомления')."
    kbd = nav.MenuOptions
    a.level = OPTIONS
    a.act = "divarication"
    return text, kbd

def REG(a: Admin, id: int, phrase: str):
    halt = None
    prmode = None
    spreadsheet = None
    fixed = None
    text = None
    kbd = None
    if a.level == START:
        text, kbd = REGStart(a)
    elif a.level == LEVEL1:
        text, kbd = REGlevel1(a, id, phrase)
    elif a.level == LEVEL2:
        text, kbd, fixed = REGlevel2(a, id, phrase)
    elif a.level == LEVEL3:
        text, kbd = REGlevel3(a, id, phrase)
    return (text, kbd, prmode, halt, spreadsheet, fixed)

def REGStart(a: Admin):
    text = "Добро пожаловать в нашего бота! Этот бот может пригодиться вам, если вы приобрели его первую часть и вам требуется административная часть. Если это ваш случай, то нажмите на кнопку снизу."
    kbd = nav.ComStartReg
    a.level = LEVEL1
    return text, kbd

def REGlevel1(a: Admin, id: int, phrase: str):
    if phrase == "Зарегистрироваться":
        database.IntermediateAction(id, a.level)
        text = "Введите пароль."
        kbd = None
        a.level = LEVEL2
    else:
        text = "Добро пожаловать в нашего бота! Этот бот может пригодиться вам, если вы приобрели его первую часть и вам требуется административная часть. Если это ваш случай, то нажмите на кнопку снизу."
        kbd = nav.ComStartReg
    return text, kbd

def REGlevel2(a: Admin, id: int, phrase: str):
    value = CheckPassword(phrase)
    fixed = None
    if value == False:
        text = "Пароль не верный! Попробуйте еще..."
        kbd = None
    else:
        a.level = LEVEL3
        text = """Вот пара рекомендаций о том, как пользоваться этим ботом:

1. Узнать, кто записался:
   - Выберите вид спорта, дату и время, чтобы увидеть, кто зарегистрировался на эту игру. Вы сможете связаться с участником через эту функцию. Если пользователь зарегистрировался через бота, то можно нажать на его имя и перейти в диалог с ним. Если нет, то вы можете просмотреть контактную информацию и связаться с ним самостоятельно.

2. Настроить расписание:
   - С помощью этой функции вы можете настроить расписание, добавив или удалив игры.

3. Создать нового пользователя:
   - Нажав на эту кнопку, вы можете создать нового пользователя. Эта функция предназначена для того, чтобы удобно записывать пользователей на игры.

4. Зарегистрировать пользователя на игру:
   - Это продолжение предыдущей функции. Здесь вы можете записать любого пользователя на игру, который уже есть в системе.

5. Настроить/Удалить пользователя:
   - Эта функция предназначена для настройки и удаления пользователей из системы.

6. Получить отчет о деятельности бота:
   - Нажав на эту кнопку, бот отправит вам HTML-файл, в котором будет таблица с информацией о расписании.

7. Уведомления:
   - Тут будут храниться пользователи, которые нуждаются в вашем уведомлении. Но это будет только в том случае, если до этого вы меняли или удаляли какие-то игры из расписания.

P.S. Если что-то пойдет не так, вы всегда можете использовать команду /menu, чтобы вернуться в главное меню без сохранения прогресса. 
В самом крайнем случае, когда что то случиться с ботом и он зависнет, но вам нужно будет срочно что то сделать, то напишите ему команду /reset .
Это команда опасна для вас же самих, так как это полностью удалит всю информацию в боте о вас и вам придется делать все сначала. Но она все же дает 
второй шанс для того что бы закончить начатое. Большая просьба, если вы все же прибегли к такому виду перезагрузки бота, задокументируйте, 
сфоткайте или еще что то сделаете и отправтье сведения об ошибке разработчику.""" 
        kbd = nav.Next
        fixed = True
    return text, kbd, fixed

def REGlevel3(a: Admin, id: int, phrase: str):
    text = "Вот опции, которые вам доступны:"
    kbd = nav.MenuOptions
    a.level = OPTIONS
    a.act = "divarication"
    return text, kbd

def MenuOptions(a: Admin, id: int, phrase: str):
    halt = False
    if phrase in ('Узнать кто записался','Зарегестрировать пользователя'):
        text = "Выберите вид спорта:"
        kbd = nav.MenuSports
        if phrase == 'Узнать кто записался':
            a.act = "view registered users"
        elif phrase == 'Зарегестрировать пользователя':
            a.act = "registration new user"
        a.level = START
        spreadsheet = None
    elif phrase == 'Настроить расписание':
        text = "Выберите, что вас интересует."
        a.act = "schedule setting"
        kbd = nav.SetSchedule
        halt = None
        spreadsheet = None
        a.level = START
    elif phrase == "Создать нового пользователя":
        a.act = "create new user"
        text = "Выберите, откуда он/она:"
        kbd = nav.MenuFrom
        a.level = START
        spreadsheet = None
    elif phrase == "Настроить пользователя":
        a.act = "сhange user"
        text = "Выберите действие."
        kbd = nav.Do
        a.level = START
        spreadsheet = None
    elif phrase == "Отчет":
        a.act = "report table"
        text = None
        spreadsheet = CreateTable()
        kbd = nav.WatNext
        a.level = START
    elif phrase == "notification":
        names, id_user = database.WhoNeedNotif(id)
        print(id_user, "ну я да и что")
        if id_user != []:
            a.act = "notify the user"
            text = "Вот пользователи, которые нуждаются в том, чтобы вы их оповестили об изменении расписания."
            kbd = nav.kbnames(names, id_user)
            a.level = START
        else:
            a.act = "divarication"
            text = "Вы не меняли и не удалили ни одной игры, следовательно, нет пользователей, которым нужно было бы отправить уведомление. Или же вы меняли, но пользователи не ожидали игру, которую вы меняете."
            kbd = nav.MenuOptions
        spreadsheet = None
    else:
        text = "На данный момент я воспринимаю только нажатия на кнопки!\n\nВыберите интересующую вас опцию."
        kbd = nav.MenuOptions
    database.Action(id, a.act)
    prmode = None
    fixed = None
    return (text, kbd, prmode, halt, spreadsheet, fixed)    


def CreateTable():
    data = database.CreateTable()
    html_table = "<table>"
    html_table += "<tr><th>Уникальный номер</th><th>Вид спорта</th><th>Дата проведения</th><th>Время проведения</th><th>Свободные места</th></tr>"
    
    for row in data:
        game_id, sport, date, time, seats = row

        year = date//10000
        month = (date-(year*10000))//100
        day = (date-(year*10000)-(month*100))//1
        date_str = f"{day}-{month}-{year}"

        hour = time//100
        minute = (time-(hour*100))//1
        time_str = f"{hour}:{minute}"

        html_table += f"<tr><td>{game_id}</td><td>{sport}</td><td>{date_str}</td><td>{time_str}</td><td>{seats}</td></tr>"
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
        if phrase in ("tg", "whatsapp", "viber", "calls"):
            text = "Напишите имя нового пользователя.\n\nP.S. Небольшая памятка: во всех следующих действиях вы будете отправлять информацию боту. Т.к. бот не в силах проверить на достоверность информацию, которую вы ему пришлете (потому что имя, фамилия, номер телефона и т.д. могут быть любыми у пользователя, которого вы регистрируете), то БОЛЬШАЯ ПРОСЬБА перепроверять информацию перед отправкой, иначе вам придется удалять пользователя или же дополнительно его настраивать (уже не тут)."
            kbd = None
            a.fromwhere_new_user = phrase
            a.level = LEVEL1
        else:
            text = "Я ЖДУ ОТ ВАС НАЖАТИЕ НА КНОПКУ!\n\n\nВыьерите откуда пользователь"
            kbd = nav.MenuFrom
    elif a.level == LEVEL1:
        text = "Напишите фамилию нового пользователя."
        kbd = None
        a.name_new_user = phrase
        a.level = LEVEL2
    elif a.level == LEVEL2:
        text = "Напишите предпочтительный язык нового пользователя."
        kbd = None
        a.lastname_new_user = phrase
        a.level = LEVEL3
    elif a.level == LEVEL3:
        text = "Напишите номер телефона нового пользователя."
        kbd = None
        a.language_new_user = phrase
        a.level = LEVEL4
    elif a.level == LEVEL4:
        text = "Новый пользователь успешно создан!\nВозвращаю вас в главное меню."
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


def IDCheck(uid) -> bool:
    all_id = database.SelAllUid()

    i = 0
    while i < len(all_id):
        if uid == str(all_id[i]):
            find = True
            i = len(all_id)
        else:
            find = False
        i += 1
    return find

def IDCheck2(uid) -> bool:
    all_id = database.SelAdmUs()
    i = 0
    while i < len(all_id):
        if uid == str(all_id[i]):
            find = True
            i = len(all_id)
        else:
            find = False
        i += 1
    return find

def SeatsCheck(id: int, seat: str) -> bool:
    free_seats = database.HowMutchSeats(id)
    update_seats = None
    if int(seat) > free_seats:
        halt = False
    else:
        update_seats = free_seats - int(seat)
        halt = True
    return halt, update_seats


def IDNotifCheck(adid: int, something):
    notifuid = database.IdNotifUsers(adid)
    i = 0
    while i < len(notifuid):
        if something == str(notifuid[i]):
            find = True
            i = len(notifuid)
        else:
            find = False
        i += 1
    return find

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
            if ValidDate(day, month, year) and datetime.date(year, month, day) >= datetime.date.today():
                date = (day*1)+(month*100)+(year*10000)
                halt = True
            else:
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

def GameIdCheck(gid) -> bool:
    all_gid = database.SelGid()
    i = 0
    while i < len(all_gid):
        if gid == str(all_gid[i]):
            find = True
            i = len(all_gid)
        else:
            find = False
        i += 1
    return find



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
    a.act_schedule = None
    a.game_id_schedule = None
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
    a.gid_notification = None
    a.uid_notification = None
    a.condition_notification = None

    a.level = None
    (a.id, a.name, a.surname, a.username, a.act, a.sport_check_users, a.date_check_users, a.time_check_users, a.user_id_check_users,
    a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user,
    a.act_schedule, a.game_id_schedule, a.sport_schedule, a.date_schedule, a.time_schedule, a.seats_schedule, a.sport_reg_ad_us, a.date_reg_ad_us,
    a.time_reg_ad_us, a.seats_reg_ad_us, a.payment_reg_ad_us, a.user_id_change_user, a.action_change_user, a.gid_notification, a.uid_notification, a.condition_notification,  a.level) = database.RecallAdmin(uid)
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
    a.fromwhere_new_user, a.name_new_user, a.lastname_new_user, a.language_new_user, a.phonenum_new_user, a.act_schedule, a.game_id_schedule, a.sport_schedule, a.date_schedule, a.time_schedule, a.seats_schedule, 
    a.sport_reg_ad_us, a.date_reg_ad_us, a.time_reg_ad_us, a.seats_reg_ad_us, a.payment_reg_ad_us, a.user_id_change_user, a.action_change_user, a.gid_notification, a.uid_notification, a.condition_notification, a.level, a.id)
    #db.UpdateAdmin(a.id, a.level, a.data_act, a.act)