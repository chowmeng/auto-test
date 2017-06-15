from common.excel_read import readExcel
from common.methofComm import testApi

class testInterface(object):
    num_fail=0
    num_success=0
    def __init__(self, paths,intername):
        self.paths = paths
        self.intername=intername
    @property
    def testInterface(self):
        excel = readExcel(self.paths,self.intername)
        results=''
        caseid = excel.getCase
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        header = excel.getHeader
        code = excel.getCode
        row = excel.getRows

        print method
        for i in range(0, row - 1):
            #print code[i]
            api = testApi(method[i], url[i], data[i],header[i])
            apicode = api.getCode

            apijson = api.getJson
            if apicode == code[i]:
                testInterface.num_success =testInterface.num_success + 1
                liris = [str(caseid[i]),name[i],'pass',str(int(code[i])),str(apicode),str(apijson),'\n']
                delimiter = '|'
                results_temp= delimiter.join(liris)
                results=results+results_temp



            else:
                testInterface.num_fail = testInterface.num_fail + 1
                liris = [str(caseid[i]), name[i], 'nopass', str(int(code[i])), str(apicode), str(apijson), '\n']
                delimiter = '|'
                results_temp= delimiter.join(liris)
                results = results + results_temp
        print testInterface.num_success
        print testInterface.num_fail

        return results




