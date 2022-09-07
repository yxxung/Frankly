"""
일정 API 클래스
데이터 오입력 되어있는것 확인
https://open.assembly.go.kr/portal/data/service/selectServicePage.do

"""

import traceback


class ScheduleAPI:

    def __init__(self, sApiID):
        self._sApiID = sApiID


    @property
    def sApiID(self):
        return self._sApiID

    @sApiID.setter
    def sApiID(self, sApiID):
        self._sApiID = sApiID

    @property
    def scheduleURL(self):
        return self._scheduleURL

    @scheduleURL.setter
    def scheduleURL(self, scheduleURL):
        self._scheduleURL = scheduleURL

    @property
    def secretKey(self):
        return self._secretKey

    @secretKey.setter
    def secretKey(self, secretKey):
        self._secretKey = secretKey


    # -----------------------------------

    def search(self, cursor, id):
        try:
            sql = "SELECT * FROM ScheduleAPI "+ \
                  "WHERE sApiID = %s"
            cursor.execute(sql,(id))

            return cursor.fetchone()
        except Exception as e:
            traceback.print_exc()
            return None

    def setAPIInfo(self, cursor):
        result = self.search(cursor, self._sApiID)
        print("stub")
        if(result != None):
            self._scheduleURL = result[1]
            self._secretKey = result[2]
