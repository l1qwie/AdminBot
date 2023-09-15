import sqlite3



class TestDB:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    #RESETS
    def ResetUser(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM admins WHERE user_id = ?", (id,))

    def ResetOptions(self, id: int):
        with self.connection:
            self.cursor.execute("UPDATE admins SET action = 'divarication', level = 3 WHERE user_id = ?", (id,))


    def ResetAll(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM Admins WHERE user_id = ?", (id,))
            self.cursor.execute("DELETE FROM UsersFromAdmin WHERE admin_id = ?", (id,))


    #Data adjustment
    def Adjustment(self, act: str, lvl: int, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET action = :act, level = :lvl WHERE user_id = :id", ({"act": act, "lvl": lvl, "id": id}))


    def Adjustment2(self, act: str, lvl: int, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET action = :act, level = :lvl WHERE user_id = :id", ({"act": act, "lvl": lvl, "id": id}))
    #New User adjustment
    def AdjustmentForNewUs(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM users_from_admins WHERE admin_id = :id", ({"id": id}))
    #Check who reg
    def DelAllInAct(self, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET sport_check_users = NULL, date_check_users = NULL, time_check_users = NULL WHERE user_id = ?", (id,))
    
    def DelBeforeSport(self, id: int, lvl: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET date_check_users = NULL, time_check_users = NULL, level = :lvl WHERE user_id = :id", ({"id": id, "lvl": lvl}))

    def DelBeforeDate(self, id: int, lvl: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET time_check_users = NULL, level = :lvl WHERE user_id = :id", ({"id": id, "lvl": lvl}))

    def ChangeLvl(self, id: int, lvl: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET level = :lvl WHERE user_id = :id", ({"lvl": lvl, "id": id}))

    #Change User
    def DelAllchus(self, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET user_id_change_user = NULL WHERE user_id = ?", (id,))

    #Change Schedule
    def DelAllInSch(self, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET sport_schedule = NULL, date_schedule = NULL, time_schedule = NULL, seats_schedule = NULL WHERE user_id = ?", (id,))
    #Registired Admin User
    def DelAllRegAdUs(self, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET sport_reg_ad_us = NULL, date_reg_ad_us = NULL, time_reg_ad_us = NULL, seats_reg_ad_us = NULL, payment_reg_ad_us = NULL WHERE user_id = ?", (id,))

    def DelBeforeSportreg_ad(self, lvl: int, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET date_reg_ad_us = NULL, time_reg_ad_us = NULL, seats_reg_ad_us = NULL, payment_reg_ad_us = NULL, level = ? WHERE user_id = ?", (lvl, id,))
        
    def DelBeforeDatereg_ad(self, lvl: int, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET time_reg_ad_us = NULL, seats_reg_ad_us = NULL, payment_reg_ad_us = NULL, level = ? WHERE user_id = ?", (lvl, id,))

    def DelBeforePaymentreg_ad(self, lvl: int, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET payment_reg_ad_us = NULL, level = ? WHERE user_id = ?", (lvl, id,))

    def Updatelvl(self, id: int, lvl: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET level = ? WHERE user_id = ?", (lvl, id,))
    
    def CustomSport(self, sport: str, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET sport_schedule = :sport WHERE user_id = :id", ({"sport": sport, "id": id}))
            
    def CustomDate(self, date: str, id: id):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET date_schedule = :date WHERE user_id = :id", ({"date": date, "id": id}))

    def CustomTime(self, time: str, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET time_schedule = :time WHERE user_id = :id", ({"time": time, "id": id}))

    def CustomSportRegUs(self, sport: str, id: int):
        with self.connection:
            self.cursor.execute("UPDATE Admins SET sport_reg_ad_us = :sport WHERE user_id = :id", ({"sport": sport, "id": id}))

    def SelSport(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT sport_reg_ad_us FROM Admins WHERE user_id = :id", ({"id": id}))
            return self.cursor.fetchone()[0]
    
    def SelDate(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT date_reg_ad_us FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def SelTime(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT time_reg_ad_us FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def SelSportView(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT sport_check_users FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]

    def SelDateView(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT date_check_users FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
    
    def SelDateSch(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT date_schedule FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
    
    def SeltimeView(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT time_check_users FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def SelActSch(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT act_schedule FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
            
    def SelNitifGameId(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT gid_notification FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
    
    def SelUsId(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT uid_notification FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def DElwaitingusers(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM WaitingForNotification WHERE admin_id = ?", (id,))

    def SelStatus(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT condition_notification FROM Admins WHERE user_id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def DelNewGame(self, id: int, seats: str):
        with self.connection:
            self.cursor.execute("SELECT sport_schedule, date_schedule, time_schedule FROM Admins WHERE user_id = ?", (id,))
            sport, date, time = self.cursor.fetchone()
            self.cursor.execute("DELETE FROM Schedule WHERE sport = :sport AND date = :date AND time = :time AND seats = :seats", ({"sport": sport, "date": date, "time": time, "seats": seats}))

    def Podgonka(self, id: int):
        with self.connection:
            self.cursor.execute("SELECT game_id_schedule FROM Admins WHERE user_id = ?", (id,))
            gid = self.cursor.fetchone()[0]
            self.cursor.execute("UPDATE Schedule SET status = 'get ready' WHERE game_id = :gid", ({"gid": gid}))

    def DelNewRegUsToGame(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM WatingForGamesUsers WHERE user_id = ?", (id,))
        
    def CreateNotifUser(self):
        with self.connection:
            self.cursor.execute("INSERT INTO WaitingForNotification (game_id, admin_id, user_id, status) VALUES ('3', '738070596', '-66', 'waiting')")