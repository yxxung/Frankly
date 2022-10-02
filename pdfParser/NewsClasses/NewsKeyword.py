import traceback

import pymysql


class NewsKeyword:

    @property
    def newsKeywordID(self):
        return self._newsKeywordID

    @newsKeywordID.setter
    def newsKeywordID(self, newsKeywordID):
        self._newsKeywordID = newsKeywordID

    @property
    def newsKeyword(self):
        return self._newsKeyword

    @newsKeyword.setter
    def newsKeyword(self, newsKeyword):
        self._newsKeyword = newsKeyword

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    # @property
    # def category(self):
    #     return self._category
    #
    # @category.setter
    # def category(self, category):
    #     self._category = category

    @property
    def newsID(self):
        return self._newsID

    @newsID.setter
    def newsID(self, newsID):
        self._newsID = newsID

    # --------------------------

    def insert(self, cursor):
        try:
            sql = "INSERT INTO NewsKeyword VALUE (%s, %s, %s, %s)"
            cursor.execute(sql,(None,self.newsKeyword, self.politicianID, self.newsID))
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            print("키워드 중복")
            sql = "SELECT count(newsKeywordID) from NewsKeyword"
            cursor.execute(sql)
            selectcount = cursor.fetchone()
            sql = "ALTER TABLE NewsKeyword AUTO_INCREMENT = %s"
            cursor.execute(sql,(selectcount[0]))
            print("auto increment set : " + str(selectcount[0]))
            raise Exception('키워드 중복')
        except Exception as e:
            traceback.print_exc()