import traceback

import pymysql


class PropertyChange:

    @property
    def changeID(self):
        return self._changeID

    @changeID.setter
    def changeID(self, changeID):
        self._changeID = changeID

    @property
    def politicianID(self):
        return self._politicianID

    @politicianID.setter
    def politicianID(self, politicianID):
        self._politicianID = politicianID

    @property
    def propertyID(self):
        return self._propertyID

    @propertyID.setter
    def propertyID(self, propertyID):
        self._propertyID = propertyID

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason
    # ----------------------------------------

    def insert(self, cursor):
        try:
            sql = "INSERT INTO PropertyChange VALUE (%s,%s, %s, %s,%s,%s)"
            cursor.execute(sql,(None,self.politicianID, self.propertyID, self.period, self.price, self.reason))
            return True
        except pymysql.err.IntegrityError as e:
            code, msg = e.args
            if(code == 1062):
                print("propertyChange 중복")
                # sql = "ALTER TABLE PropertyList AUTO_INCREMENT = "
                # cursor.execute(sql)
            else:
                traceback.print_exc()
            return False
        except Exception as e:
            traceback.print_exc()