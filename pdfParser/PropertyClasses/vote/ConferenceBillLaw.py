
class ConferenceBillLaw:

    @property
    def billID(self):
        return self._billID

    @billID.setter
    def billID(self, billID):
        self._billID = billID

    @property
    def billNumber(self):
        return self._billNumber

    @billNumber.setter
    def billNumber(self, billNumber):
        self._billNumber = billNumber

    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, generation):
        self._generation = generation

    @property
    def billTitle(self):
        return self._billTitle

    @billTitle.setter
    def billTitle(self, billTitle):
        self._billTitle = billTitle

    @property
    def proposer(self):
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        self._proposer = proposer

    @property
    def billResult(self):
        return self._billResult

    @billResult.setter
    def billResult(self, billResult):
        self._billResult = billResult

    @property
    def effectiveDate(self):
        return self._effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, effectiveDate):
        self._effectiveDate = effectiveDate

    @property
    def proposalDate(self):
        return self._proposalDate

    @proposalDate.setter
    def proposalDate(self, proposalDate):
        self._proposalDate = proposalDate

    @property
    def competentCommittee(self):
        return self._competentCommittee

    @competentCommittee.setter
    def competentCommittee(self, competentCommittee):
        self._competentCommittee = competentCommittee

    @property
    def billLawAPIID(self):
        return self._billLawAPIID

    @billLawAPIID.setter
    def billLawAPIID(self, billLawAPIID):
        self._billLawAPIID = billLawAPIID

# -------------------------------------------------------------------


    def selectAll(self, cursor):
        sql = "SELECT * FROM ConferenceBillLaw"
        cursor.execute(sql)
        selectBillLawLists = cursor.fetchall()
        ConferenceBillLawList = []

        for billLaw in selectBillLawLists:
            cb = ConferenceBillLaw()
            cb.billID = billLaw[0]
            cb.generation = billLaw[1]
            cb.billTitle = billLaw[2]
            cb.proposer = billLaw[3]
            cb.billResult = billLaw[4]
            cb.effectiveDate = billLaw[5]
            cb.proposalDate = billLaw[6]
            cb.competentCommitee = billLaw[7]
            cb.billNumber = billLaw[8]
            cb.billLawAPIID = billLaw[9]
            ConferenceBillLawList.append(cb)

        return ConferenceBillLawList

    def update(self, cursor,apiID, billNumber):
        sql = "UPDATE ConferenceBillLaw SET billLawAPIID = %s WHERE billNumber = %s"
        cursor.execute(sql,(apiID, billNumber))