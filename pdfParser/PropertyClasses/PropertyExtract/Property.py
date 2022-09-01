import traceback

import pymysql


class Property:

    @property
    def assetID(self):
        return self._assetID
    @assetID.setter
    def assetID(self, assetID):
        self.assetID = assetID

    @property
    def propertyListID(self):
        return self._propertyListID

    @propertyListID.setter
    def propertyListID(self, propertyListID):
        self._propertyListID = propertyListID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def propertyDetail(self):
        return self._propertyDetail

    @propertyDetail.setter
    def propertyDetail(self, propertyDetail):
        self._propertyDetail = propertyDetail

    @property
    def presentPrice(self):
        return self._presentPrice

    @presentPrice.setter
    def presentPrice(self, presentPrice):
        self._presentPrice = presentPrice


    # ---------------------------------------
    def selectOne(self, cursor, detail, politicianID, propertyListID, price):
        try:
            sql = "SELECT assetID FROM Property "+ \
                  "WHERE politicianID = %s AND propertyListID = %s AND propertyDetail = %s AND presentPrice = %s"
            cursor.execute(sql,(politicianID, propertyListID, detail, price))

            return cursor.fetchone()
        except Exception as e:
            traceback.print_exc()
            return None

    def insert(self, cursor):
        try:
            sql = "INSERT INTO Property VALUE (%s,%s,%s,%s,%s)"
            cursor.execute(sql,(None,self.propertyListID, self.politicianID, self.presentPrice, self.propertyDetail))
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            if(code == 1062):
                print("property 중복" + self.propertyDetail)
                sql = "SELECT count(assetID) from Property"
                cursor.execute(sql)
                selectcount = cursor.fetchone()
                sql = "ALTER TABLE Property AUTO_INCREMENT = %s"
                cursor.execute(sql,(selectcount[0]))
                print("auto increment set : " + str(selectcount[0]))
            else:
                traceback.print_exc()
            return False
    def updatePrice(self, cursor,price, id):
        try:
            sql = "UPDATE Property SET presentPrice = %s WHERE assetID = %s"
            cursor.execute(sql,(price, id))
            return True
        except Exception as e:
            traceback.print_exc()
            return False