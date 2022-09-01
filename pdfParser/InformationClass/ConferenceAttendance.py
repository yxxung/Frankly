import traceback

import pdfplumber
import os

import pymysql

table_settings = {
    "vertical_strategy" : "lines_strict",
    "horizontal_strategy" : "lines_strict",
    "keep_blank_chars": True,
    "text_tolerance": 1,
    "text_x_tolerance": 1
}
class Attendance:

    @property
    def attendanceID(self):
        return self._attendanceID

    @attendanceID.setter
    def attendanceID(self, attendanceID):
        self._attendanceID = attendanceID

    @property
    def conferenceID(self):
        return self._conferenceID

    @conferenceID.setter
    def conferenceID(self, conferenceID):
        self._conferenceID = conferenceID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        self._attendance = attendance

    @property
    def petitionLeave(self):
        return self._petitionLeave

    @petitionLeave.setter
    def petitionLeave(self, petitionLeave):
        self._petitionLeave = petitionLeave

    @property
    def businessTrip(self):
        return self._businessTrip

    @businessTrip.setter
    def businessTrip(self, businessTrip):
        self._businessTrip = businessTrip

    # @property
    # def conferenceDate(self):
    #     return self._conferenceDate
    #
    # @conferenceDate.setter
    # def conferenceDate(self, conferenceDate):
    #     self._conferenceDate = conferenceDate.replace("년","-").replace("월","-").replace("일","").replace("\n","")
    #
    # @property
    # def conferenceSession(self):
    #     return self._conferenceSession
    #
    # @conferenceSession.setter
    # def conferenceSession(self, conferenceSession):
    #     self._conferenceSession = conferenceSession


    # --------------------------------------

    def insert(self, cursor):
        try:
            sql = "INSERT INTO ConferenceAttendance VALUE (%s,%s, %s, %s,%s,%s)"
            cursor.execute(sql,(None,self.conferenceID, self.politicianID, self.attendance,\
                                self.petitionLeave, self.businessTrip))
            # self.conferenceDate,\
            #                                 self.conferenceSession
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            if(code == 1062):
                sql = "SELECT count(attendanceID) from ConferenceAttendance"
                cursor.execute(sql)
                selectcount = cursor.fetchone()
                sql = "ALTER TABLE ConferenceAttendance AUTO_INCREMENT = %s"
                cursor.execute(sql,(selectcount[0]))
                print("auto increment set : " + str(selectcount[0]))
                raise Exception('attendance 중복')
            else:
                traceback.print_exc()
            return False
        except Exception as e:
            traceback.print_exc()


    def attendanceCheck(self, token, index):
        # token 순서 예시  강기윤|국민의힘|결석|출석|2|1|1|0|0|0
        if(token[index+2] == "출석"):
            self.attendance = True
            self.petitionLeave = False
            self.businessTrip = False
        elif(token[index+2] == "출장"):
            self.attendance = False
            self.petitionLeave = False
            self.businessTrip = True
        elif(token[index+2] == "청가"):
            self.attendance = False
            self.petitionLeave = True
            self.businessTrip = False
        else:
            self.attendance = False
            self.petitionLeave = False
            self.businessTrip = False