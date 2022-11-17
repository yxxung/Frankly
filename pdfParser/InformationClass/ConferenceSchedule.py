import traceback

import pymysql


class ConferenceSchedule:
    @property
    def conferenceID(self):
        return self._conferenceID

    @conferenceID.setter
    def conferenceID(self, conferenceID):
        self._conferenceID = conferenceID

    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, generation):
        self._generation = generation

    @property
    def conferenceDate(self):
        return self._conferenceDate

    @conferenceDate.setter
    def conferenceDate(self, conferenceDate):
        self._conferenceDate = conferenceDate

    @property
    def conferenceTitle(self):
        return self._conferenceTitle

    @conferenceTitle.setter
    def conferenceTitle(self, conferenceTitle):
        self._conferenceTitle = conferenceTitle

    @property
    def conferenceSession(self):
        return self._conferenceSession

    @conferenceSession.setter
    def conferenceSession(self, conferneceSession):
        self._conferenceSession = conferneceSession


    # ----------------------

    def search(self, cursor, input, column):
        try:
            if(column == "conferenceDate"):
                sql = "SELECT * FROM ConferenceSchedule "+ \
                      "WHERE conferenceDate = %s"
                cursor.execute(sql,(input))
            elif(column == "conferenceTitle"):
                sql = "SELECT * FROM ConferenceSchedule "+ \
                      "WHERE conferenceTitle = %s"
                cursor.execute(sql,(input))

            return cursor.fetchone()
        except Exception as e:
            traceback.print_exc()
            return None

    def insert(self, cursor):
        try:
            sql = "INSERT INTO ConferenceSchedule VALUE (%s,%s, %s, %s, %s)"
            cursor.execute(sql,(None,self.generation, self.conferenceDate, self.conferenceTitle,self.conferenceSession))
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            print("schedule 중복")
            sql = "SELECT count(conferenceID) from ConferenceSchedule"
            cursor.execute(sql)
            selectcount = cursor.fetchone()
            sql = "ALTER TABLE ConferenceSchedule AUTO_INCREMENT = %s"
            cursor.execute(sql,(selectcount[0]))
            print("auto increment set : " + str(selectcount[0]))
            return False
        except Exception as e:
            traceback.print_exc()




