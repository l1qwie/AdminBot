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
            self.cursor.execute("UPDATE admins SET action = :act, level = :lvl WHERE user_id = :id", ({"act": act, "lvl": lvl, "id": id}))
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
