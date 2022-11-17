"""
일정 API 클래스
데이터 오입력 되어있는것 확인
https://open.assembly.go.kr/portal/data/service/selectServicePage.do

"""

import traceback


class openAPI:


    @property
    def ApiID(self):
        return self._ApiID

    @ApiID.setter
    def ApiID(self, ApiID):
        self._ApiID = ApiID

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def secretKey(self):
        return self._secretKey

    @secretKey.setter
    def secretKey(self, secretKey):
        self._secretKey = secretKey


    # -----------------------------------

    def search(self, cursor, APIName):
        try:
            sql = "SELECT * FROM API "+ \
                  "WHERE APIName = %s"
            cursor.execute(sql,(APIName))

            return cursor.fetchone()
        except Exception as e:
            traceback.print_exc()
            return None

    def setAPIInfo(self, cursor, APIName):
        result = self.search(cursor, APIName)
        # print("stub")
        if(result != None):
            self._URL = result[1]
            self._secretKey = result[2]
