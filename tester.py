#from admin import DispatchPhrase, DateCheck, TimeCheck
import admin
import keyboards as nav
from dbfortests import TestDB
import database
import random

tdb = TestDB("..\\bot(for_all)\\test_database.db")


#Intermediate test
def TestCreateDateList(days: list):
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

def TestCreateTimeList(time: list):
    times_ready = []
    tm = 0
    while tm < len(time):
        hour = time[tm]//100
        minute = (time[tm]-(hour*100))//1
        time_str = f"{hour}:{minute}"
        times_ready.append(time_str)
        tm += 1
    return times_ready
    






def T2():
    dates = database.GamesWithUsers('volleyball')
    times = database.TimeOfGamesWithUsers(738070596, dates[0])

def TestingNamer (name: str, nick: str) -> str:
    return name + nick


def GlobalT():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    #tdb.ResetUser(738070596)
    #These functions I need to test
    #StartRegistration()+
    #FindCrashesRegUs()+
    #FindCrashesViewWhoReg()+
    #FindCrashesSchedule()+
    #FindCrashesScheduleSet()+
    #Next function work if the fuction before doesn't work
    #FindCrashesScheduleDel()+
    FindCrashesNotif()
    #In another functions, data which arrive from Admin, doesn't need to test, because lies at the Admins's conscience. And I can't test anything



def FindCrashesNotif():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    first = ["adjkliojeioj", 22, "-66"]
    second = ["ajshdhjkahjkd", 3341, "Notif completed"]
    third = ["234jjkl3kl", 1213123145, "user wait"]
    tdb.CreateNotifUser()
    FirstStepNotif(first)
    if tdb.SelStatus(738070596) == "DELETE":
        DelStepNotif(second)
    else:
        SecondtStepNotif(second)
        ThirdStepNotif(third)


def FirstStepNotif(f: list):
    i = 0
    while i < len(f):
        tdb.Adjustment("notify the user", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, f[i])
        if admin.IDNotifCheck(738070596, f[i]):
            (name, last_name, language, phone_number) = database.InfOfUser(int(f[i]))
            (game_id, sport, date, time, status) = database.InfAboutGameofUser(int(f[i]))
            if status == "DELETE":
                assert(text == f"""Вот информация по этому пользователю:
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
то никаких дальнейших к вам вопросов по поводу пользователя не будет.""")
            else:
                assert(text == f"""Вот информация по этому пользователю:
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
Так что рекомендую задать этот же вопрос пользователю.""")
            assert(kbd == nav.Notif)
        else:
            names, id_user = database.WhoNeedNotif(738070596)
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите пользователя.")
            assert(kbd == nav.kbnames(names, id_user))
        i += 1


def DelStepNotif(dd: list):
    i = 0
    while i < len(dd):
        tdb.Adjustment2("notify the user", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, dd[i])
        if dd[i] == "Notif completed":
            assert(text == "Прекрасно! Возвращаю вас в Главное Меню")
            assert(kbd == nav.MenuOptions)
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите действие.")
            assert(kbd == nav.Notif)
        i += 1


def SecondtStepNotif(s: list): 
    i = 0
    while i < len(s):
        tdb.Adjustment2("notify the user", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, s[i])
        if s[i] == "Notif completed":
            assert(text == "Что выбрал пользователь?")
            assert(kbd == nav.UserDecision)
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите действие.")
            assert(kbd == nav.Notif)
        i += 1

def ThirdStepNotif(th: list):
    i = 0
    while i < len(th):
        tdb.Adjustment2("notify the user", 2, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, th[i])
        if th[i] in ("user wait", "user not wait"):
            if th[i] == "user wait":
                assert(text == "Ура! Пользователь решил оставить запись на эту игру!\n\n\nДобро пожаловать в Главное Меню")
            elif th[i] == "user not wait":
                assert(text == "Ну что ж. Жаль. Но ничего не поделаешь\n\n\nДобро пожаловать в Главное Меню")
            assert(kbd == nav.MenuOptions)
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nЧто выбрал пользователь?")
            assert(kbd == nav.UserDecision)
        i += 1


def FindCrashesRegUs():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    tdb.DelAllInSch(738070596)
    first = ["dhjkfhjkdfhjkdfhjk", 1111111111, "volleyball", "volleyballll", "enything else", "football"]
    second = ['asjhdahjksdhjkas', '11111111', 1111111, "20-02-2024", "14-07-2024", "15-12-2023", "06,02,2024", "20.12.2024", '04 02 2025', "66-27-2055", "76,27,2055" "56.57.2035", "33 55 2333", "15-07,2024", "24.07 2024"]
    third = ["12:00", "22 02", "14.45" "12,15", "24:01", "00.00", "12", "12 6", "14 00"]
    fourth = [1111, 2, "Тристо", 55, 12, "2 3", "4 56 77 zzzzz"]
    fifth = ["adhbhjasdghjkas", 1231231231231, "наличные", "Наличные", "cash", "card"]
    sixth = ['-124']
    FirstStepRegUs(first)
    SecondStepRegUs(second)
    ThirdStepRegUs(third)
    FourthStepRegUs(fourth)
    FifthStepRegUs(fifth)
    SixthStepRegUs(sixth)

def FirstStepRegUs(first: list):
    i = 0
    while i < len(first):
    #for fitem in first:
        tdb.Adjustment("registration new user", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, first[i])
        if first[i] in ("volleyball", "football"):
            schedule = database.FindDates()
            if schedule == 0:
                assert(text == "Нет ни одной добавленной игры в расписании! Добавьте сначала игру в расписание, а уже потом зарегистрируйте пользователя. \n\n\nГлавное меню")
                assert(kbd == nav.MenuOptions)
            else:
                days = database.AllFreeDates(first[i])
                if days == []:
                    assert(text == "В расписании нет дат на этот вид спорта. Выберите другой вид спорта или создайте новую игру.")
                    assert(kbd == nav.MenuSports)
                else:
                    assert(text == "Выберите дату:")
                    assert(kbd == nav.kbdata(TestCreateDateList(days)))
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите вид спорта.")
            assert(kbd == nav.MenuSports)
        i += 1


def SecondStepRegUs(second: list):
    i = 0
    while i < len(second):
        tdb.Adjustment("registration new user", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, second[i])
        bruh, date = admin.DateCheck(second[i])
        sport = tdb.SelSport(738070596)
        if bruh is True:
            if date in (database.AllFreeDates(sport)):
                seats = database.SeatsofTimesofDateofSport(date, sport)
                assert(text == "Выберите время проведения игры")
                assert(kbd == nav.kbtime(TestCreateTimeList(database.TimesOfFreeDates(date, sport)), seats))
            else:
                assert(text == "Вы выбрали дату, но, к сожалению, это не подходящая дата для вас. Выберите ту, которая показана на кнопках")
                assert(kbd == nav.kbdata(TestCreateDateList(database.AllFreeDates(sport))))
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите дату.")
            assert(kbd == nav.kbdata(TestCreateDateList(database.AllFreeDates(sport))))
        i += 1

def ThirdStepRegUs(third: list):         
    cc = 0
    while cc < len(third):
        tdb.Adjustment("registration new user", 2, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, third[cc])
        sport = tdb.SelSport(738070596)
        date = tdb.SelDate(738070596)
        times = database.TimesOfFreeDates(date, sport)
        seats = database.SeatsofTimesofDateofSport(date, sport)
        bruh, timeschedule = admin.TimeCheck(third[cc], date)
        if bruh is True:
            if timeschedule in times:
                assert(text == "Выберите или введите желаемое количетсво мест.")
                assert(kbd == nav.FrequentChoice)
            else:
                assert(text == "Вы прислали мне время, но, к сожалению, это не то время, которое я вам предложил на кнопках. Выберите, пожалуйста, то, что на кнопках.")
                assert(kbd == nav.kbtime(TestCreateTimeList(times), seats))
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\n\nВыберите время проведения игры.")
            assert(kbd == nav.kbtime(TestCreateTimeList(times), seats))
        cc += 1


def FourthStepRegUs(fourth: list):
    i = 0
    while i < len(fourth):
        tdb.Adjustment("registration new user", 3, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fourth[i])
        if admin.IntCheck(fourth[i]):
            if halt is True:
                assert(text == "Выберите способ оплаты.")
                assert(kbd == nav.KbPay)
            else:
                assert(text == "Вы ввели не цифру или ввели цифру, которая больше, чем количество свободных мест на эту игру.\n\n\nВыберите или введите желаемое количество мест.")
                assert(kbd == nav.FrequentChoice)
        else:
            assert(text == "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите или введите желаемое количество мест.")
            assert(kbd == nav.FrequentChoice)
        i += 1

def FifthStepRegUs(fifth: list):
    i = 0
    while i < len(fifth):
        tdb.Adjustment("registration new user", 4, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fifth[i])
        if fifth[i] in ("cash", "card"):
            (names_users, id_users) = database.AllUsers()
            assert(text == "Выберите пользователя.")
            assert(kbd == nav.kbnames(names_users, id_users))
        else:
            assert(text == "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите способ оплаты.")
            assert(kbd == nav.KbPay)
        i += 1

def SixthStepRegUs(sixth: list):
    i = 0
    while i < len(sixth):
        tdb.Adjustment("registration new user", 5, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sixth[i])
        if admin.IDCheck(sixth[i]):
            assert(text == "Мои поздравления! Вы зарегистрировали этого пользователя на игру.\nВозвращаю Вас в главное меню.")
            assert(kbd == nav.MenuOptions)
            print("ВСЕ ПРОШЛО УСПЕШНО! ПОЛЬЗОВАТЕЛЬ ЗАРЕГЕСТРИРОАВН НА ИГРУ")
            tdb.DelNewRegUsToGame(sixth[i])
        else:
            assert(text == "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите пользователя.")
            (names_users, id_users) = database.AllUsers()
            assert(kbd == nav.kbnames(names_users, id_users))
        i += 1





def FindCrashesSchedule():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    div = [1111, 22, "aiskldjlaksdjkl", "new"]
    first = ["dhjkfhjkdfhjkdfhjk", 1111111111, "5" "volleyball", "volleyballll", "enything else", "football"]
    second = ['asjhdahjksdhjkas', '11111111', 1111111, "14-07-2024", "06,02,2024", "20.12.2024", '04 02 2025', "66-27-2055", "76,27,2055" "56.57.2035", "33 55 2333", "15-07,2024", "24.07 2024"]
    third = ["12:00", "22 02", "14.45" "12,15", "24:01", "00.00", "12", "12 6"]
    fourth = [11111, "2", "Тристо", "55", "12", "2 3", "4 56 77 zzzzz"]
    Divarication(div)
    FirstStepSchedule(first, 1)
    SecondStepSchedule(second, 2)
    ThirdStepSchedule(third, 3)
    FourthStepSchedule(fourth, 4)

def FindCrashesScheduleSet():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    div = [1111, 22, "aiskldjlaksdjkl", "setSche"]
    beginer = [11, 232, "22", "2"]
    first = ["dhjkfhjkdfhjkdfhjk", 1111111111, "5" "volleyball", "volleyballll", "enything else", "football"]
    second = ['asjhdahjksdhjkas', '11111111', 1111111, "14-07-2024", "06,02,2024", "20.12.2024", '04 02 2025', "66-27-2055", "76,27,2055" "56.57.2035", "33 55 2333", "15-07,2024", "24.07 2025"]
    third = ["12:00", "22 02", "14.45" "12,15", "24:01", "00.00", "12", "12 10"]
    fourth = [1111, 2123123, "Тристо", "212312312233", "423123 5126 1277 zzzzz", "44"]
    Divarication(div)
    BeginStepSchedule(beginer)
    FirstStepSchedule(first, 2)
    SecondStepSchedule(second, 3)
    ThirdStepSchedule(third, 4)
    EndofSetSche(fourth, 5)

def FindCrashesScheduleDel():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    div = [1111, 22, "aiskldjlaksdjkl", "delSche"]
    beginer = [11, 232, "22", "5"]
    Divarication(div)
    BeginStepSchedule(beginer)
    

def Divarication(div: list):
    tdb.DelAllInSch(738070596)
    i = 0
    while i < len(div):
        tdb.Adjustment("schedule setting", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, div[i])
        if div[i] in ("new", "setSche", "delSche"):
            if div[i] == "new":
                assert(text == "Дальше бы будете создавать новую игру\n\n\nВыберите вид спорта.")
                assert(kbd == nav.MenuSports)
            elif div[i] in ("setSche", "delSche"):
                assert(text == "Дальше вы будете редактировать ранее сделанное расписание на игру. Для этого вам нужно будет открыть файл, который я вам прислал, и выбрать игру, которую вы хотите изменить. Мне нужен только её порядковый номер.")
                assert(kbd == nav.WatNext)
        else:
            assert(text == "Я жду от вас нажатия на кнопку!\n\nВыберите, что вас интересует.")
            assert(kbd == nav.SetSchedule)
        i += 1


def FirstStepSchedule(first: list, level: int):
    i = 0
    while i < len(first):
        tdb.Adjustment("schedule setting", level, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, first[i])
        if first[i] in ("volleyball", "football"):
            assert(text == "Напишите дату проведения игры.\nБот примет за дату любое ваше сообщение, которое будет соответствовать следующему условию: \nПервые 1 или 2 цифры в сообщении будут расцениваться как число. Вторые 1 или 2 цифры будут расцениваться как месяц. И дальше, 4 следующие цифры, которые будут идти подряд, будут расцениваться как год.")
            assert(kbd == None)
        else:
            assert(text == "Я жду от вас нажатия на кнопку.\n\nВыберите вид спорта.")
            assert(kbd == nav.MenuSports)
        i += 1


def BeginStepSchedule(beg: list):
    i = 0
    while i < len(beg):
        tdb.Adjustment("schedule setting", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, beg[i])
        act = tdb.SelActSch(738070596)
        tdb.Podgonka(738070596)
        if admin.GameIdCheck(beg[i]):
            if act == "setSche":
                assert(text == "Прекрасно! Вы выбрали номер игры, и теперь можете приступить к ее изменениям!\n\n\nВыберите вид спорта")
                (kbd == nav.MenuSports)
            else:
                assert(text == testEndSchedule())
                assert(kbd == nav.MenuOptions)
                print("ВСЕ ХОРОШО! ФУНКЦИЯ УДАЛЕНИЯ ПРОШЛА УСПЕШНО!")
        else:
            assert(text == "Вы ввели не номер игры, а что то еще. Напоминаю, мне нужен только номер, т.е. мне нужно одно сообщение от вас содержащее только одну цифру.")
            assert(kbd == nav.WatNext)
        i += 1

def testEndSchedule():
    countusers, adminusers = database.CountTGUsers(738070596)
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
    return text


def SecondStepSchedule(second: list, level: int):
    i = 0
    while i < len(second):
        tdb.Adjustment("schedule setting", level, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, second[i])
        act = tdb.SelActSch(738070596)
        if act in ("new", "setSche"):
            if act == "new":
                bruh, date = admin.DateCheck(second[i])
                if bruh == False:
                    assert(text == "Вы ввели не дату или дату, которая меньше сегодняшнего числа.\nНапишите дату.")
                    assert(kbd == None)
                else:
                    assert(text == "Напишите время проведения игры. \nБот примет за время любое ваше сообщение, которое будет соответствовать следующему условию:\n Первые 1 или 2 цифры в сообщении будут расцениваться как часы. А вторые 1 или 2 цифры будут расцениваться как минуты.")
                    assert(kbd == None)
            else:
                if admin.GameIdCheck(second[i]):
                    assert(text == "Игра с этим номером существует. Введите желаемую дату (если хотите, то можно не менять дату, но нужно написать в любом случае, любую дату).")
                    assert(kbd == None)
                
        i += 1
    """         
        elif act == "delSche":
            if admin.IDCheck2(second[i]):
                (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(738070596, int(second[i]))
                assert(text == f"Вот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}")
                assert(kbd == nav.Notif)"""

def ThirdStepSchedule(third: list, level: int):
    i = 0
    while i < len(third):
        tdb.Adjustment("schedule setting", level, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, third[i])
        act= tdb.SelActSch(738070596)
        if act in ("new", "setSche"):
            date = tdb.SelDateSch(738070596)
            bruh, time = admin.TimeCheck(third[i], date)
            if bruh == False:
                assert(text == "Вы ввели не время.\nНапишите время.")
                assert(kbd == None)
            else:
                assert(text == "Напишите количество мест.\n\nБоту нужно прислать число (однозначное или двузначное).")
                assert(kbd == None)
        i += 1
        
        
        """elif act == "delSche":
            if third[i] in ("Notif completed", "Notif later"):
                if third[i] == "Notif completed":
                    gid = tdb.SelNitifGameId(738070596)
                    #counter = database.SelUsWhoNeedNotif(gid)
                    counter = database.CountUsWhoNeedNotif(gid)
                    if counter != 0:
                        assert(text == f"Прекрасно! у вас осталось еще {counter} пользователей, которых нужно уведомить по этой игре. Скажите пожалуйста, пользователь решил остаться, на перенесенной вами игре, или же отменил запись?")
                        assert(kbd == nav.UserDecision)
                    else:
                        assert(text == "Великолепно! Все польователи уведомлены!")
                        assert(kbd == nav.MenuOptions )
                else:
                    assert(text == "Ну ничего страшного! Но чтобы вы не забыли я через некоторое время вам напомню об них")
                    assert(kbd == nav.MenuOptions)
            else:
                uid = tdb.SelUsId(738070596)
                (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(738070596, int(uid))
                assert(text == f"Я ЖДУ ОТ ВАС НАЖАТИЕ НАА КНОПКУ!\n\n\nВот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}")
                assert(kbd == nav.Notif)"""

def FourthStepSchedule(fourth: list, level: int):
    for fitem in fourth:
        tdb.Adjustment("schedule setting", level, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fitem)
        if admin.IntCheck(fitem) == False:
            assert(text == "Похоже, вы ввели не количество мест, или же вы ввели число, которое больше, чем максимальное значение двузначного числа. Введите, пожалуйста, нужное вам количество мест.")
            assert(kbd == None)
        else:
            assert(text == "Расписание успешно обновлено.\nДобро пожаловать в Главное Меню.")
            assert(kbd == nav.MenuOptions)
            print("ВСЕ ХОРОШО! РАСПИСАНИЕ БЛАГОПОЛУЧНО ОБНОВЛЕНО!")
            tdb.DelNewGame(738070596, fitem)

def EndofSetSche(end: list, level: int):
    i = 0
    while i < len(end):
        tdb.Adjustment("schedule setting", level, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, end[i])
        if admin.IntCheck(end[i]):
            assert(text == testEndSchedule())
            assert(kbd == nav.MenuOptions)
            tdb.DElwaitingusers(738070596)
            print("УРА! ВСЕ ХОРОШО! МЫ ДОБАВИЛИ В УВЕДОМЛЕНИЯ ПОЛЬЗОВАТЕЛЯ!")
        else:
            assert(text == "Похоже, вы ввели не количество мест, или же вы ввели число, которое больше, чем максимальное значение двузначного числа. Введите, пожалуйста, нужное вам количество мест.")
            assert(kbd == None)
        i += 1


def FindCrashesViewWhoReg():
    admin.namer = TestingNamer
    database.ConnectTo("..\\bot(for_all)\\test_database.db")
    tdb.DelAllInSch(738070596)
    first = ["dhjkfhjkdfhjkdfhjk", 1111111111, "volleyballll", "enything else", "football"]
    second = ['asjhdahjksdhjkas', '11111111', 1111111, "14-07-2024", "06,02,2024", "20.12.2024", '04 02 2025', "76,27,2055" "56.57.2035", "33 55 2333", "15-07,2024", "24.07 2024", "20-02-2024"]
    third = ["12:00", "22 02", "14.45" "12,15", "24:01", "00.00", "12", "12 6", "14 00"]
    fourth = ["ahjksdhjkasdhjk", 12313131, "-66"]
    FirstStepViewWhoReg(first)
    SecondStepViewWhoReg(second)
    ThirdStepViewWhoReg(third)
    FourthStepViewWhoReg(fourth)



def FirstStepViewWhoReg(first: list):
    for fitem in first:
        tdb.Adjustment("view registered users", 0, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fitem)
        if fitem in ("volleyball", "football"):
            days_db = database.GamesWithUsers(fitem)
            if database.Nobody() == True:
                assert(text == "Вообще никто не забронировал места на игры, так что нигде никого нет!\n\n\nВозвращаю Вас в главное меню.")
                assert(kbd == nav.MenuOptions)
            elif days_db != []:
                assert(text == "Выберите дату:")
                assert(kbd == nav.kbdata(TestCreateDateList(days_db)))
            else:
                assert(text == "Никого нет\nВыберите вид спорта:")
                assert(kbd == nav.MenuSports)
        else:
            assert(text == "Я жду от Вас нажатия на кнопку!\n\nВыберите вид спорта.")
            assert(kbd == nav.MenuSports)

def SecondStepViewWhoReg(second: list):
    for sitem in second:
        tdb.Adjustment("view registered users", 1, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, sitem)
        bruh, date = admin.DateCheck(sitem)
        sport = tdb.SelSportView(738070596)
        if bruh is True:
            if database.CheckDate(date, sport) != 0:
                (times, seats) = database.TimeOfGamesWithUsers(738070596, date)
                if times != []:
                    assert(text == "Выберите время проведения игры:")
                    assert(kbd == nav.kbtime(TestCreateTimeList(times), seats))
                else:
                    assert(text == "Почему-то тут никого нет.\n\nВозвращаю Вас в главное меню.")
                    assert(kbd == nav.MenuOptions)
            else:
                assert(text == "Вы прислали мне дату, но, к сожалению, мне нужна только дата, которую я вам предлагаю на кнопках")
                assert(kbd == nav.kbdata(TestCreateDateList(database.GamesWithUsers(sport))))
        else:
            assert(text == "Я жду от вас нажатия на кнопку!\n\nВыберите дату.")
            assert(kbd == nav.kbdata(TestCreateDateList(database.GamesWithUsers(sport))))

def ThirdStepViewWhoReg(third: list):
    for thitem in third:
        tdb.Adjustment("view registered users", 2, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, thitem)
        date = tdb.SelDateView(738070596)
        bruh, time = admin.TimeCheck(thitem, date)
        (times, seats) = database.TimeOfGamesWithUsers(738070596, date)
        sport = tdb.SelSportView(738070596)
        if halt is True:
            if database.CheckTime(date, sport, time) != 0:
                (name_users, id_users) = database.UsersOfGamesWithUsers(738070596, time)
                assert(text == f"На эту игру зарегистрировалось {len(name_users)}.\nНажмите на имена ниже, чтобы узнать подробную информацию:")
                assert(kbd == nav.kbnames(name_users, id_users))
            else:
                assert(text == "Вы прислали мне время, но, к сожалению, я жду от вас время, которое я вам предлагаю на кнопках\n\nВыберите время.")
                
                assert(kbd == nav.kbtime(TestCreateTimeList(times), seats))
        else:
            assert(text == "Я жду от вас нажатия на кнопку!\n\nВыберите время.")
            assert(kbd == nav.kbtime(TestCreateTimeList(times), seats))

def FourthStepViewWhoReg(fourth: list):
    for fitem in fourth:
        tdb.Adjustment("view registered users", 3, 738070596)
        (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, fitem)
        time = tdb.SeltimeView(738070596)
        if database.CheckUser(fitem) != 0:
            (name, last_name, username, from_where, language, phone_number, us_seats, payment) = database.AllInfuser(738070596, int(fitem))
            if username != "Информация отсутствует":
                nick = (f"t.me/{username}")
                name = TestingNamer(name, nick)
            assert(text == f"Вот информация по этому пользователю:\nИмя: {name}\nФамилия(если есть): {last_name}\nНикнейм(если есть): {username}\nПредпочтительный язык: {language}\nОткуда пользователь: {from_where}\nНомер телефона(если был указан): {phone_number}\nЗабронировано мест вместе с ним(ней): {us_seats}\nСпособ оплаты: {payment}\n\n\n\nP.S. Если что, если пользователь регистрировался через бота, то можно кликнуть по его имени и перейти в диалог с ним")
            assert(kbd == nav.BackorMenu)
        else:
            (name_users, id_users) = database.UsersOfGamesWithUsers(738070596, time)
            assert(text == f"Я жду от Вас нажатия на кнопку!\n\nНа эту игру зарегистрировалось {len(name_users)}.\nНажмите на имена ниже, чтобы узнать подробную информацию:")
            assert(kbd == nav.kbnames(name_users, id_users))
        print("ВСЕ ХОРОШО! МЫ ПОСМОТРЕЛИ КТО КУДА ЗАПИСАЛСЯ!")

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
    assert(text == "Добро пожаловать в нашего бота! Этот бот может пригодиться вам, если вы приобрели его первую часть и вам требуется административная часть. Если это ваш случай, то нажмите на кнопку снизу.")
    assert(kbd == nav.ComStartReg)
    #Начало регистриции
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "Зарегистрироваться")
    assert(text == "Введите пароль.")
    #Окончательная регистрация
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "111")
    assert(text == """Вот пара рекомендаций о том, как пользоваться этим ботом:

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
сфоткайте или еще что то сделаете и отправтье сведения об ошибке разработчику.""")
    assert(kbd == nav.Next)
    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, "next")
    assert(text == "Вот опции, которые вам доступны:")
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
                    (text, kbd, prmode, halt, spreadsheet, fixed) = admin.DispatchPhrase(738070596, id_users[us])
                    assert(text == "Мои поздравления! Вы зарегестрировали этого пользователя на игру.\nВозвращаю Вас в главное меню")
                    assert(kbd == nav.MenuOptions)
                    tdb.Updatelvl(738070596, 5)
                    database.DelRegAdUs(738070596, id_users[us])
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
        assert(text == op_answers_text[0])
        assert(kbd == op_answers_kb[0])
    elif op == 3:
        assert(text == op_answers_text[1])
        assert(kbd == op_answers_kb[1])
    elif op == 4:
        assert(text == op_answers_text[2])
        assert(kbd == op_answers_kb[2])
