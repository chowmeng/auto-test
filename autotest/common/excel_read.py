import xlrd


class readExcel(object):
    def __init__(self, path,intername):
        self.path = path
        self.intername=intername
    @property
    def getSheet(self):
        xl = xlrd.open_workbook(self.path)
        #sheet = xl.sheet_by_index(0)
        sheet = xl.sheet_by_name(self.intername)
        return sheet

    @property
    def getRows(self):
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        col = self.getSheet.ncols
        return col

    @property
    def getCase(self):
        TestCase = []
        for i in range(1, self.getRows):
            TestCase.append(self.getSheet.cell_value(i, 0))
        return TestCase

    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 1))
        return TestName

    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 2))
        return TestData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 3))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 4))
        return TestMethod

    @property
    def getHeader(self):
        TestHeader = []
        for i in range(1, self.getRows):
            TestHeader.append(self.getSheet.cell_value(i, 5))
        return TestHeader

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.getSheet.cell_value(i, 6))
        return TestCode