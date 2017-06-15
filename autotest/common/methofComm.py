import requests
import json
class testApi(object):
    def __init__(self, method, url, data,headers):
        self.method = method
        self.url = url
        self.data = data
        self.headers=headers

    @property
    def testApi(self):
        try:
            if self.method == 'post':
                r = requests.post(self.url, data=json.loads(self.data), headers=json.loads(self.headers))

            elif self.method == 'get':
                r = requests.get(self.url, params=eval(self.data))
            return r
        except:
            print('fail')

    @property
    def getCode(self):
        if self.testApi!= None:
            code = self.testApi.json()['errno']
            return code
        return None

    @property
    def getJson(self):
        if self.testApi != None:
            json_data = self.testApi.json()
            return json_data
        return None

