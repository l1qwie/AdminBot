import sqlite3

import logging



connection = None
cursor = None

def ConnectTo (filename: str):
    global connection, cursor
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

def ResetAll(id: int):
    global connection, cursor
    with connection:
        cursor.execute("DELETE FROM Admins WHERE user_id = ?", (id,))
        
def IntermediateAction(id: int, lvl: int):
        global connection, cursor
        with connection:
            cursor.execute("UPDATE admins SET level = :lvl WHERE user_id = :id", ({"lvl": lvl, "id": id}))

def Password(msg: str):
    global connection, cursor
    with connection:
        cursor.execute("SELECT password FROM admins_password WHERE password = :msg", ({"msg": msg}))
        return cursor.fetchone()

def AddNewAdmin(a):
    global connection, cursor
    with connection:
        query = "INSERT INTO admins (user_id, name, surname, username, language_code, level) VALUES (?, ?, ?, ?, ?, ?)"
        values = (a.id, a.name, a.surname, a.username, a.language_code, a.level)
        cursor.execute(query, values)

def DelIntermediateAdmin(id: int):
    with connection:
        cursor.execute("DELETE FROM IntermediateAdmins WHERE user_id = :id", ({"id": id}))

def DataAct(id: int):
    with connection:
        cursor.execute("SELECT data_action FROM Admins WHERE user_id = ?", (id,))
        x = cursor.fetchone()
        res = x[0]
        #res = self.cursor.fetchone()[0]
        if res != None:
            point = ' '
            res_list = res.split(point)
        else:
            res_list = []
        return res_list


def AddAdmin(id: int, lvl: int):
    with connection:
        cursor.execute("INSERT INTO admins (user_id, action, setup_reg, level) VALUES (?, 'registation', 'start', ?)", (id, lvl,))

def delete():
    with connection:
        cursor.execute("DELETE FROM admins")


def RecognizeExMesID(id: int, n: str, ln: str, un: str):
    with connection:
        cursor.execute("SELECT exmess FROM admins WHERE user_id = :id", ({"id": id}))
        res = cursor.fetchone()
        if res == None:
            return res
        else:
            cursor.execute("UPDATE admins SET name = :n, last_name = :ln, username = :un WHERE user_id = :id", ({"n": n, "ln": ln, "un": un, "id": id}))
            return res[0]
        
def AddNewMesID(id: int, mid: int):
    with connection:
        cursor.execute("UPDATE admins SET exmess = :mid WHERE user_id = :id", ({"mid": mid, "id": id}))



def LevelAdmin(id: int) -> int:
    with connection:
        cursor.execute("SELECT level FROM admins WHERE user_id = ?", (id,))
        level = cursor.fetchone()
        if level is None:
            res = -1
            cursor.execute("INSERT INTO admins (user_id, action, setup_reg, level) VALUES (?, 'registation', 'start', ?)", (id, res+1,))
        else:
            res = int(level[0])
            
        return res


def UpdateAdmin(id: int, lvl: int, dat_act: str, act: str):
    with connection:
        column = None
        if act == "view registered users":
            if lvl == 1:
                column = "sport_check_users"
            elif lvl == 2:
                column = "date_check_users"
            elif lvl == 3:
                column = "time_check_users"
        elif act == "create new user":
            if lvl == 1:
                column = "fromwhere_new_user"
            elif lvl == 2:
                column = "name_new_user"
            elif lvl == 3:
                column = "lastname_new_user"
            elif lvl == 4:
                column = "language_new_user"
            elif lvl == 5:
                column = "phonenum_new_user"
        elif act == "registation":
            if lvl == 3:
                cursor.execute("UPDATE admins SET setup_reg = 'completed' WHERE user_id = ?", (id,))
        if column != None:
            if dat_act != "FALSE":
                cursor.execute(f"UPDATE admins SET level = :lvl, {column} = :dat_act WHERE user_id = :id", ({"lvl": lvl, "dat_act": dat_act, "id": id}))
        
def RetainAdmin(id: int, name: str, surname: str,
                username: str,
                act: str,
                sport_check_users: str,
                date_check_users: int,
                time_check_users: int,
                user_id_check_users: int,
                fromwhere_new_user: str,
                name_new_user: str,
                lastname_new_user: str,
                language_new_user: str,
                phonenum_new_user: str,
                act_schedule: str,
                game_id_schedule: int,
                sport_schedule: str,
                date_schedule: int,
                time_schedule: int,
                seats_schedule: int,
                sport_reg_ad_us: str,
                date_reg_ad_us: int,
                time_reg_ad_us: int,
                seats_reg_ad_us: int,
                payment_reg_ad_us: str,
                user_id_change_user: str,
                action_change_user: str,
                gid_notification: int,
                uid_notification: int,
                condition_notification: str,
                level: int,
                uid: int):
    with connection:
        cursor.execute("""UPDATE Admins SET user_id = ?, name = ?, last_name = ?, username = ?, action = ?, sport_check_users = ?, date_check_users = ?, time_check_users = ?, user_id_check_users = ?,
                            fromwhere_new_user = ?, name_new_user = ?, lastname_new_user = ?, language_new_user = ?, phonenum_new_user = ?, 
                            act_schedule = ?, game_id_schedule = ?, sport_schedule = ?, date_schedule = ?, time_schedule = ?, seats_schedule = ?, sport_reg_ad_us = ?, date_reg_ad_us = ?, time_reg_ad_us = ?, seats_reg_ad_us = ?, payment_reg_ad_us = ?, 
                            user_id_change_user = ?, action_change_user = ?, gid_notification = ?, uid_notification = ?, condition_notification = ?, level = ? WHERE user_id = ?""", 
                            (id, name, surname, username, act, sport_check_users, date_check_users, time_check_users, user_id_check_users,
                                fromwhere_new_user, name_new_user, lastname_new_user, language_new_user, phonenum_new_user, act_schedule, game_id_schedule, sport_schedule,
                                date_schedule, time_schedule, seats_schedule, sport_reg_ad_us, date_reg_ad_us, time_reg_ad_us, seats_reg_ad_us, payment_reg_ad_us, user_id_change_user, action_change_user, 
                                gid_notification, uid_notification, condition_notification, level, uid))

def SelAction(id: int) -> str:
    with connection:
        cursor.execute("SELECT action FROM admins WHERE user_id = ?", (id,))
        return cursor.fetchone()[0]

def Action(id: int, act: str):
    with connection:
        cursor.execute("UPDATE Admins SET action = :act WHERE user_id = :id", ({"act": act, "id": id}))

def AllInfAdmin(id: int, n: str, ln: str, un: str):
    with connection:
        cursor.execute("UPDATE admins SET name = :n, last_name = :ln, username = :un WHERE user_id = :id", ({"n": n, "ln": ln, "un": un, "id": id}))

def GamesWithUsers(g: str):
    with connection:
        cursor.execute("""SELECT DISTINCT date
                            FROM Schedule
                            JOIN WatingForGamesUsers ON Schedule.game_id = WatingForGamesUsers.game_id
                            WHERE Schedule.sport = :g""", ({"g": g}),)
        res = [row[0] for row in cursor.fetchall()]
        return res
    
def Nobody() -> bool:
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers")
        count = int(cursor.fetchone()[0])
        if count == 0:
            bl = True
        else:
            bl = False
        return bl


def NewActionInformation(id: int, inf: str, lvl: int, act: str):
    with connection:
        if act == "create new user":
            table = "users_from_admins"
            fcolumn = "from_where"
        elif act == "view registered users":
            table = "prog_who_reg"
            fcolumn = "game"
        cursor.execute(f"INSERT INTO {table} (admin_id, {fcolumn}, level) VALUES (:id, :inf, :lvl)", ({"id": id, "inf": inf, "lvl": lvl}))

def UpdateActionInformation(id: int, inf: str, exlvl: int, nextlvl: int, act: str):
    with connection:
        cursor.execute("SELECT data_action FROM admins WHERE level = :exlvl and user_id = :id and action = :act", ({"exlvl": exlvl, "id": id, "act": act}))
        past_value = cursor.fetchone()[0]
        if past_value != None:
            inf = past_value + ',' + inf
        cursor.execute(f"UPDATE admins SET data_action = :inf, level = :nextlvl WHERE user_id = :id and level = :exlvl and action = :act", ({"inf": inf, "id": id, "exlvl": exlvl, "nextlvl": nextlvl, "act": act}))

def TimeOfGamesWithUsers(id: int, date: int) -> list:
    with connection:
        cursor.execute("SELECT sport_check_users FROM Admins WHERE user_id = :id", ({"id": id}))
        sport = cursor.fetchone()[0]
        cursor.execute("SELECT Schedule.time FROM Schedule WHERE Schedule.sport = :sp AND Schedule.date = :dt", ({"sp": sport, "dt": date}))
        times = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT Schedule.seats FROM Schedule WHERE Schedule.sport = :sp AND Schedule.date = :dt", ({"sp": sport, "dt": date}))
        seats = [row[0] for row in cursor.fetchall()]
        return times, seats
        
def UsersOfGamesWithUsers(id: int, time: str):
    with connection:
        cursor.execute("SELECT sport_check_users, date_check_users FROM Admins WHERE user_id = ?", (id,))
        res_list = cursor.fetchall()
        game_list = list(res_list[0])
        cursor.execute("SELECT game_id FROM Schedule WHERE sport = :sp and date = :dt and time = :tm", ({"sp": game_list[0], "dt": game_list[1], "tm": time}))
        gid = cursor.fetchone()[0]
        cursor.execute("""SELECT WatingForGamesUsers.user_id
                            FROM WatingForGamesUsers
                            JOIN Schedule ON Schedule.game_id = WatingForGamesUsers.game_id
                            WHERE Schedule.game_id = :game_id""", ({"game_id": gid}))
        users = [row[0] for row in cursor.fetchall()]
        names = []
        i = 0
        while i < len(users):
            cursor.execute("SELECT name FROM Users WHERE user_id = :uuid and name IS NOT NULL", ({"uuid": users[i]}))
            name = cursor.fetchone()
            if name != None:
                name = name[0]
                names.append(name)
            cursor.execute("SELECT last_name FROM Users WHERE user_id = :uuid and last_name IS NOT NULL", ({"uuid": users[i]}))    
            lastname = cursor.fetchone()
            if lastname != None:
                lastname = lastname[0]
                exvalue = names[i]
                names[i] = exvalue + ' ' + lastname
            i += 1
        
        return names, users

def RecallAdmin(id: int):
    with connection:
        cursor.execute("SELECT level FROM Admins WHERE user_id = ?", (id,))
        level = cursor.fetchone()
        if level is None:
            res = -1
            cursor.execute("INSERT INTO Admins (user_id, action, setup_reg, level) VALUES (?, 'registation', 'start', ?)", (id, res+1,))
        else:
            res = int(level[0])
        cursor.execute("""SELECT user_id, name, last_name, username, action, sport_check_users, date_check_users, time_check_users, user_id_check_users,
                                fromwhere_new_user, name_new_user, lastname_new_user, language_new_user, phonenum_new_user, act_schedule, game_id_schedule, sport_schedule, date_schedule, time_schedule,
                                seats_schedule, sport_reg_ad_us, date_reg_ad_us, time_reg_ad_us, seats_reg_ad_us, payment_reg_ad_us, user_id_change_user, action_change_user, gid_notification, uid_notification, 
                                condition_notification, level FROM Admins WHERE user_id = :id""", ({"id": id}))
        (user_id, name, surname, username, action, sport_check_users, date_check_users, time_check_users, user_id_check_users,
        fromwhere_new_user, name_new_user, lastname_new_user, language_new_user, phonenum_new_user, act_schedule, game_id_schedule, sport_schedule, date_schedule, time_schedule,
        seats_schedule, sport_reg_ad_us, date_reg_ad_us, time_reg_ad_us, seats_reg_ad_us, payment_reg_ad_us, user_id_change_user, action_change_user, gid_notification, uid_notification, condition_notification, level) = cursor.fetchone()
        return (user_id, name, surname, username, action, sport_check_users, date_check_users, time_check_users, user_id_check_users,
        fromwhere_new_user, name_new_user, lastname_new_user, language_new_user, phonenum_new_user, act_schedule, game_id_schedule, sport_schedule, date_schedule, time_schedule, seats_schedule,
        sport_reg_ad_us, date_reg_ad_us, time_reg_ad_us, seats_reg_ad_us, payment_reg_ad_us, user_id_change_user, action_change_user, gid_notification, uid_notification, condition_notification, level)
        
        self.cursor.execute("SELECT action FROM admins WHERE user_id = ?", (id,))
        act = self.cursor.fetchone()[0]
        return res, act

def AllInfuser(id: int, usid: int):
    with connection:
        cursor.execute("SELECT sport_check_users, date_check_users, time_check_users FROM Admins WHERE user_id = ?", (id,))
        res_list = cursor.fetchall()
        game_list = list(res_list[0])
        cursor.execute("SELECT game_id FROM Schedule WHERE sport = :sp and date = :dt and time = :tm", ({"sp": game_list[0], "dt": game_list[1], "tm": game_list[2]}))
        gid = cursor.fetchone()[0]
        cursor.execute("SELECT name, last_name, username, from_where, language, phone_number FROM Users WHERE user_id = :id", ({"id": usid}))
        name, last_name, username, from_where, language, phone_number = cursor.fetchone()
        cursor.execute("SELECT seats, payment FROM WatingForGamesUsers WHERE user_id = :id and game_id = :game_id", ({"id": usid, "game_id": gid}))
        seats, payment = cursor.fetchone()

        if name == None:
            name = "Информация отсутствует"
        if last_name == None:
            last_name = "Информация отсутствует"
        if username == None:
            username = "Информация отсутствует"
        if from_where == None:
            from_where = "Информация отсутствует"
        if language == None:
            language = "Информация отсутствует"
        if phone_number == None:
            phone_number = "Информация отсутствует"
        return name, last_name, username, from_where, language, phone_number, seats, payment
    

def IdNewUser():
    with connection:
        cursor.execute("SELECT num FROM Negative")
        newid = cursor.fetchone()[0]-1
        cursor.execute("UPDATE Negative SET num = :newnum", ({"newnum": newid}))
        return newid

def CreateNewUser(id: int, phonenum: int):
    with connection:
        uid = IdNewUser()
        cursor.execute("SELECT fromwhere_new_user, name_new_user, lastname_new_user, language_new_user FROM Admins WHERE user_id = :id", ({"id": id}))
        (fromwhere, name, lastname, language) = cursor.fetchone()
        cursor.execute("""INSERT INTO Users (user_id, name, last_name, from_where, language, phone_number, user_admin) VALUES (:uid, :name, :lastname, :fromwhere, :language, :phonenum, 'TRUE')""", 
                            ({"uid": uid, "name": name, "lastname": lastname, "fromwhere": fromwhere, "language": language, "phonenum": phonenum}))

def NewScheduleGame(id: int, seats: int):
    with connection:
        cursor.execute("SELECT sport_schedule, date_schedule, time_schedule FROM Admins WHERE user_id = :id", ({"id": id}))
        (sp, dt, tm) = cursor.fetchone()
        cursor.execute("INSERT INTO Schedule (sport, date, time, seats, status) VALUES (:sp, :dt, :tm, :st, 'get ready')", ({"sp": sp, "dt": dt, "tm": tm, "st": seats}))

def AllFreeDates(sp: str) -> list:
    with connection:
        cursor.execute("SELECT date FROM Schedule WHERE sport = :sp AND seats IS NOT NULL AND status IS NOT 'DELETE'", ({"sp": sp}))
        dates = [row[0] for row in cursor.fetchall()]
        return dates
    
def HowMutchSeats(id: int) -> int:
    with connection:
        cursor.execute("""SELECT seats
                            FROM Schedule
                            JOIN Admins ON Admins.sport_reg_ad_us = Schedule.sport and Admins.date_reg_ad_us = Schedule.date and Admins.time_reg_ad_us = Schedule.time
                            WHERE Admins.user_id = :id AND Schedule.status IS NOT 'DELETE'""", ({"id": id}))
        seats = int(cursor.fetchone()[0])
        return seats
    
def TimesOfFreeDates(date: str, sport: str) -> list:
    with connection:
        cursor.execute("SELECT time FROM Schedule WHERE date = :date and sport = :sp and seats IS NOT NULL", ({"date": date, "sp": sport}))
        times = [row[0] for row in cursor.fetchall()]
        return times
    
def SeatsofTimesofDateofSport(date: str, sport: str) -> list:
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE date = :date and sport = :sp and seats IS NOT NULL",({"date": date, "sp": sport}))
        seats = [row[0] for row in cursor.fetchall()]
        return seats
    
def AllUsers() -> list:
    with connection:
        cursor.execute("SELECT name FROM Users WHERE setup_reg IS NOT 'DELETE'")
        names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT last_name FROM Users WHERE setup_reg IS NOT 'DELETE'")
        last_names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT user_id FROM Users WHERE setup_reg IS NOT 'DELETE'")
        users_id = [row[0] for row in cursor.fetchall()]
        namesurname = [(x, y) for x, y in zip(names, last_names)]

        return namesurname, users_id
    
def AdminUsers() -> list:
    with connection:
        cursor.execute("SELECT name FROM Users WHERE setup_reg IS NOT 'DELETE' and username IS NULL")
        names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT last_name FROM Users WHERE setup_reg IS NOT 'DELETE' and username IS NULL")
        last_names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT user_id FROM Users WHERE setup_reg IS NOT 'DELETE' and username IS NULL")
        users_id = [row[0] for row in cursor.fetchall()]
        namesurname = [(x, y) for x, y in zip(names, last_names)]

        return namesurname, users_id
    
def SelPersonWhoNeedsNotif(gid: int) -> list:
    with connection:
        cursor.execute("SELECT name FROM Users JOIN WaitingForNotification ON WaitingForNotification.user_id = Users.user_id WHERE WaitingForNotification.game_id = :gid", ({"gid": gid}))
        names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT last_name FROM Users JOIN WaitingForNotification ON WaitingForNotification.user_id = Users.user_id WHERE WaitingForNotification.game_id = :gid", ({"gid": gid}))
        last_names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT user_id FROM Users JOIN WaitingForNotification ON WaitingForNotification.user_id = Users.user_id WHERE WaitingForNotification.game_id = :gid", ({"gid": gid}))
        users_id = [row[0] for row in cursor.fetchall()]
        namesurname = [(x, y) for x, y in zip(names, last_names)]
        return namesurname, users_id


def DelRegAdUs(adid: int, uid: int):
    with connection:
        cursor.execute("""
            SELECT WatingForGamesUsers.game_id
            FROM WatingForGamesUsers
            JOIN Schedule ON Schedule.game_id = WatingForGamesUsers.game_id
            JOIN Admins ON Admins.sport_reg_ad_us = Schedule.sport AND Admins.date_reg_ad_us = Schedule.date AND Admins.time_reg_ad_us = Schedule.time
            WHERE Admins.user_id = :id
        """, {"id": adid})
        game_id = cursor.fetchone()[0]
        cursor.execute("""SELECT seats 
                            FROM WatingForGamesUsers
                            WHERE game_id = :game_id""", {"game_id": game_id})
        reserved_seats = cursor.fetchone()[0]
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = :game_id", ({"game_id": game_id}))
        remaining_seats = cursor.fetchone()[0]
        retern_seats = int(reserved_seats) + int(remaining_seats)
        cursor.execute("UPDATE Schedule SET seats = :retern_seats WHERE game_id = :game_id", ({"retern_seats": retern_seats, "game_id": game_id}))
        cursor.execute("DELETE FROM WatingForGamesUsers WHERE user_id = :uid and game_id = :game_id", ({"uid": uid, "game_id": game_id}))

def RegAdUs(sport: str, date: str, time: str, seats: str, payment: str, id: int, ad_id: int):
    with connection:
        cursor.execute("SELECT game_id FROM Schedule WHERE sport = :sp and date = :dt and time = :tm", ({"sp": sport, "dt": date, "tm": time}))
        g_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment) VALUES (:id, :g_id, :st, :pm)", ({"id": id, "g_id": g_id, "st": seats, "pm": payment}))
        cursor.execute("UPDATE Admins SET sport_reg_ad_us = NULL, date_reg_ad_us = NULL, time_reg_ad_us = NULL, seats_reg_ad_us = NULL, payment_reg_ad_us = NULL WHERE user_id = :ad_id", ({"ad_id": ad_id}))

def BalanceOfTheUniverse(seat: str, id: int):
    with connection:
        cursor.execute("""
            UPDATE Schedule
            SET seats = :st
            WHERE EXISTS (
                SELECT 1
                FROM Admins
                WHERE Admins.sport_reg_ad_us = Schedule.sport
                AND Admins.date_reg_ad_us = Schedule.date
                AND Admins.time_reg_ad_us = Schedule.time
                AND Admins.user_id = :id
            )
        """, {"st": seat, "id": id})


def DelUs(id: int):
    with connection:
        cursor.execute("UPDATE Users SET setup_reg = 'DELETE' WHERE user_id = ?", (id,))
        cursor.execute("UPDATE WatingForGamesUsers SET setup_reg = 'DELETE' WHERE user_id = ?", (id,))
        cursor.execute("UPDATE WaitingForNotification SET setup = 'DELETE WHERE user_id = ?'", (id,))

def CreateTable():
    with connection:
        cursor.execute("SELECT game_id, sport, date, time, seats FROM Schedule WHERE status IS NOT 'DELETE'")
        data = cursor.fetchall()
        return data
    
def UpdateInfAboutUs(fw: str, name: str, lastname: str, lang: str, phonenum: str, id: int):
    with connection:
        if fw is not None:
            cursor.execute("UPDATE Users SET from_where = :fw WHERE user_id = :id", ({"fw": fw, "id": id}))
        elif name is not None:
            cursor.execute("UPDATE Users SET name = :name WHERE user_id = :id", ({"name": name, "id": id}))
        elif lastname is not None:
            cursor.execute("UPDATE Users SET last_name = :lastname WHERE user_id = :id", ({"lastname": lastname, "id": id}))
        elif lang is not None:
            cursor.execute("UPDATE Users SET language = :lang WHERE user_id = :id", ({"lang": lang, "id": id}))
        elif phonenum is not None:
            cursor.execute("UPDATE Users SET phone_number = :phonenum WHERE user_id = :id", ({"phonenum": phonenum, "id": id}))

def CheckDate(date: int, sport: str):
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE sport = :sport and date = :date", ({"sport": sport, "date": date}))
        return cursor.fetchone()[0]
    
def CheckTime(dt: str, sp: str, tm: int):
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE sport = :sp and date = :dt and time = :tm", ({"sp": sp, "dt": dt, "tm": tm}))
        res = cursor.fetchone()[0]
        return res
    
def CheckUser(id: int):
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE user_id = :id", ({"id": id}))
        return cursor.fetchone()[0]

def FindDates():
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status IS NOT 'DELETE'")
        return cursor.fetchone()[0]
    
def SelAllUid():
    with connection:
        cursor.execute("SELECT user_id FROM Users WHERE setup_reg IS NOT 'DELETE'")
        all_uid = [row[0] for row in cursor.fetchall()]
        return all_uid
    
def SelAdmUs():
    with connection:
        cursor.execute("SELECT user_id FROM Users WHERE setup_reg IS NOT 'DELETE' and username IS NULL")
        all_uid = [row[0] for row in cursor.fetchall()]
        return all_uid

def SelUsWhoNeedNotif(gid: int):
    with connection:
        cursor.execute("SELECT user_id FROM WaitingForNotification WHERE game_id = ?", (gid,))
        uidnotif = [row[0] for row in cursor.fetchall()]
        return uidnotif
    
def CountUsWhoNeedNotif(gid: int):
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WaitingForNotification WHERE game_id = ?", (gid,))
        return cursor.fetchone()[0]
    
def ChangedDates():
    with connection:
        cursor.execute("""SELECT Schedule.date
                  FROM Schedule  
                  JOIN WaitingForNotification ON Schedule.game_id = WaitingForNotification.game_id""")
        days = [row[0] for row in cursor.fetchall()]
        truedays = []
        if days is not []:
            while db < len(days):
                year = days[db]//10000
                month = (days[db]-(year*10000))//100
                day = (days[db]-(year*10000)-(month*100))//1
                date_str = f"{day}-{month}-{year}"
                truedays.append(date_str)
                db += 1
        cursor.execute("""SELECT WaitingForNotification.status 
                       FROM WaitingForNotification
                       JOIN Schedule ON WaitingForNotification.game_id = Schedule.game_id""")
        statuses = [row[0] for row in cursor.fetchall()]
        return truedays, statuses

def SelGid():
    with connection:
        cursor.execute("SELECT game_id FROM Schedule WHERE status IS NOT 'DELETE'")
        gid = [row[0] for row in cursor.fetchall()]
        return gid

def CountTGUsers(id: int):
    with connection:
        cursor.execute("""SELECT COUNT(*)
                        FROM Users
                        JOIN WatingForGamesUsers ON Users.user_id = WatingForGamesUsers.user_id
                        JOIN Schedule ON WatingForGamesUsers.game_id = Schedule.game_id
                        JOIN Admins ON Schedule.sport = Admins.sport_schedule AND Schedule.date = Admins.date_schedule AND Schedule.time = Admins.time_schedule
                        WHERE Admins.user_id = 738070596 and Users.username IS NOT NULL
                        """, ({"id": id}))
        tgusers = cursor.fetchone()[0]
        if tgusers == 0:
            cursor.execute("""SELECT *
                        FROM Users
                        JOIN WatingForGamesUsers ON Users.user_id = WatingForGamesUsers.user_id
                        JOIN Schedule ON WatingForGamesUsers.game_id = Schedule.game_id
                        JOIN Admins ON Schedule.sport = Admins.sport_schedule AND Schedule.date = Admins.date_schedule AND Schedule.time = Admins.time_schedule
                        WHERE Admins.user_id = 738070596 and Users.username IS NOT NULL
                        """)
            print(cursor.fetchone())
        cursor.execute("""SELECT COUNT(*)
                        FROM Users
                        JOIN WatingForGamesUsers ON Users.user_id = WatingForGamesUsers.user_id
                        JOIN Schedule ON WatingForGamesUsers.game_id = Schedule.game_id
                        JOIN Admins ON Schedule.sport = Admins.sport_schedule AND Schedule.date = Admins.date_schedule AND Schedule.time = Admins.time_schedule
                        WHERE Admins.user_id = 738070596 and Users.username IS NULL
                        """, ({"id": id}))
        adusers = cursor.fetchone()[0]
        print("я конечно дико извиняюсь", tgusers, adusers)
        return tgusers, adusers
    
def ChangeGame(id: int, seats: int):
    with connection:
        cursor.execute("SELECT game_id_schedule, sport_schedule, date_schedule, time_schedule FROM Admins WHERE user_id = ?", (id,))
        gid, sport, date, time = cursor.fetchone()
        cursor.execute("SELECT sport, date, time, seats FROM Schedule JOIN Admins ON Admins.game_id_schedule = Schedule.game_id WHERE Admins.user_id = ?", (id,))
        sp, dt, tm, st = cursor.fetchone()
        print([sport, date, time, int(seats)])
        print([sp, dt, tm, st])
        if (sport != sp) or (date != dt) or (time != tm) or (int(seats) != st):
            cursor.execute("UPDATE Schedule SET sport = :sport, date = :date, time = :time, seats = :seats, status = 'changed' WHERE game_id = :gid", ({"sport": sport, "date": date, "time": time, "seats": seats, "gid": gid}))

def UserWhoNeedNotif(id: int):
    with connection:
        cursor.execute("""SELECT Users.user_id
                        FROM Users
                        JOIN WatingForGamesUsers ON Users.user_id = WatingForGamesUsers.user_id
                        JOIN Schedule ON WatingForGamesUsers.game_id = Schedule.game_id
                        JOIN Admins ON Schedule.sport = Admins.sport_schedule AND Schedule.date = Admins.date_schedule AND Schedule.time = Admins.time_schedule
                        WHERE Admins.user_id = :id and Users.username IS NULL
                        """, ({"id": id}))
        users_ids = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT game_id_schedule FROM Admins WHERE user_id = ?", (id,))
        gid = cursor.fetchone()[0]
        i = 0
        print("YAYAYAYYAYAYYAYA", users_ids)
        while i < len(users_ids):
            print("ТУТ Я ТУТ")
            cursor.execute("INSERT INTO WaitingForNotification (game_id, admin_id, user_id, status) VALUES (:gid, :id, :uid, 'waiting')", ({"gid": gid, "id": id, "uid": users_ids[i]}))
            i += 1

def ShadowRemoveGame(gid: int):
    with connection:
        cursor.execute("UPDATE Schedule SET status = 'DELETE' WHERE game_id = :gid", ({"gid": gid}))

def WhoNeedNotif(id: int):
    with connection:
        cursor.execute("SELECT name FROM Users JOIN WaitingForNotification ON Users.user_id = WaitingForNotification.user_id and WaitingForNotification.admin_id = :id WHERE WaitingForNotification.status IS NOT 'notified'", ({"id": id}))
        names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT last_name FROM Users JOIN WaitingForNotification ON Users.user_id = WaitingForNotification.user_id and WaitingForNotification.admin_id = :id WHERE WaitingForNotification.status IS NOT 'notified'", ({"id": id}))
        last_names = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT Users.user_id FROM Users JOIN WaitingForNotification ON Users.user_id = WaitingForNotification.user_id and WaitingForNotification.admin_id = :id WHERE WaitingForNotification.status IS NOT 'notified'", ({"id": id}))
        users_id = [row[0] for row in cursor.fetchall()]

        namesandlastnames = [(x, y) for x, y in zip(names, last_names)]
        return namesandlastnames, users_id

def IdNotifUsers(id):
    with connection:
        cursor.execute("""SELECT Users.user_id FROM Users
                       JOIN WaitingForNotification ON WaitingForNotification.user_id = Users.user_id AND
                                                      WaitingForNotification.admin_id = ?""", (id,))
        users_id = [row[0] for row in cursor.fetchall()]
        return users_id

def InfOfUser(uid: int):
    with connection:
        cursor.execute("SELECT name, last_name, language, phone_number FROM Users WHERE user_id = ?", (uid,))
        name, last_name, language, phone_number = cursor.fetchone()
        if name == None:
            name = "Информация отсутствует"
        if last_name == None:
            last_name = "Информация отсутствует"
        if language == None:
            language = "Информация отсутствует"
        if phone_number == None:
            phone_number = "Информация отсутствует"

        return name, last_name, language, phone_number

def InfAboutGameofUser(uid: int):
    with connection:
        cursor.execute("""SELECT Schedule.game_id, Schedule.sport, Schedule.date, Schedule.time, Schedule.status
                       FROM Schedule
                       JOIN WaitingForNotification ON WaitingForNotification.game_id = Schedule.game_id AND 
                       WaitingForNotification.user_id = ?""", (uid,))
        game_id, sport, date, time, status = cursor.fetchone()

        year = date//10000
        month = (date-(year*10000))//100
        day = (date-(year*10000)-(month*100))//1
        date_str = f"{day}-{month}-{year}"

        hour = time//100
        minute = (time-(hour*100))//1
        time_str = f"{hour}:{minute}"

        return game_id, sport, date_str, time_str, status
    
def SetupUs(id: int, condition: str):
    with connection:
        cursor.execute("SELECT uid_notification, gid_notification FROM Admins WHERE user_id = ?",(id,))
        uid, gid = cursor.fetchone()
        cursor.execute("UPDATE WatingForGamesUsers SET setup_reg = :condition WHERE user_id = :uid AND game_id = :gid", ({"condition": condition, "uid": uid, "gid": gid}))
        cursor.execute("UPDATE WaitingForNotification SET status = 'notified', setup = 'DELETE' WHERE user_id = :uid AND game_id = :gid AND admin_id = :id", ({"uid": uid, "gid": gid, "id": id}))

def SeatsBack(id: int):
    with connection:
        cursor.execute("SELECT uid_notification, gid_notification FROM Admins WHERE user_id = ?",(id,))
        uid, gid = cursor.fetchone()
        cursor.execute("SELECT seats FROM WatingForGamesUsers WHERE user_id = :uid AND game_id = :gid", ({"uid": uid, "gid": gid}))
        seats = cursor.fetchone()[0]
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = :gid", ({"gid": gid}))
        remainder = cursor.fetchone()[0]
        newseats = int(seats) + int(remainder)
        cursor.execute("UPDATE Schedule SET seats = :newseats WHERE game_id = :gid", ({"newseats": newseats, "gid": gid}))

def ChangeStatusUser(id):
    with connection:
        cursor.execute("SELECT uid_notification, gif_notification FROM Admins WHERE user_id = ?", (id,))
        uid, gid = cursor.fetchone()
        cursor.execute("UPDATE WaitingForNotification SET status = 'notified', setup = 'DELETE' WHERE user_id = :uid AND game_id = :gid AND admin_id = :id", ({"uid": uid, "gid": gid, "id": id}))