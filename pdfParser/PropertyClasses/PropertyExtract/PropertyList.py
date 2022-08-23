import traceback


class PropertyList:

    @property
    def propertyListID(self):
        return self._propertyListID

    @propertyListID.setter
    def propertyListID(self, propertyListID):
        self._propertyListID = propertyListID

    @property
    def propertyListName(self):
        return self._propertyListName

    @propertyListName.setter
    def propertyListName(self, propertyListName):
        self._propertyListName = propertyListName

    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, relation):
        self._relation = relation

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self,section):
        self._section = section

    # ----------------------------------------------

    def selectOne(self, cursor,section, kind, relation):
        try:
            sql = "SELECT propertyListID FROM PropertyList "+\
                "WHERE section = %s AND kind = %s AND relation = %s"
            cursor.execute(sql,(section, kind, relation))

            return cursor.fetchone()
        except Exception as e:
            traceback.print_exc()
            return None
    def insert(self, cursor):
        try:
            sql = "INSERT INTO PropertyList VALUE (%s,%s, %s, %s)"
            cursor.execute(sql,(None,self.section, self.kind, self.relation))
            return True
        except Exception as e:
            traceback.print_exc()
            return False

        # ----------------------------------------------

        # iterator 동작시 json 내용과 현재 오브젝트의 값 비교
    def __eq__(self, other):
        # type이 dict인 경우..
        if(str(type(other)) == "<class 'dict'>"):
            return self.section == other["종류"] and self.kind == other["상세종류"] and self.relation == other["관계"]
        elif (str(type(other)) == "<class 'PropertyList'>"):
            return self.section == other.section and self.kind == other.kind and self.relation == other.relation
        else:
            return False

    def __hash__(self, other):
        return hash((self.section, self.kind, self.relation))




