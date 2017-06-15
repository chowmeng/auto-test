# encoding: utf-8
from common.run_interface import testInterface
import unittest
import time
import ConfigParser
import os
import sys

class testLoginApi(unittest.TestCase):

    def testLoginApi(self):
        config = ConfigParser.ConfigParser()
        config = ConfigParser.ConfigParser()
        currentDir = os.path.dirname(__file__)
        filepath = currentDir + os.path.sep + "config.ini"
        config.readfp(open(filepath))
        source=config.get("INT", "path")
        Interface_name = config.get("INT", "Interface_name").split(',')
        dir_name= time.strftime(sys.path[0]+'/result/'+'%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
        os.mkdir(dir_name)
        for i in range(0, len(Interface_name)):
            file_name=dir_name+'/'+Interface_name[i]+'.txt'
            file=open(file_name, 'w')
            resultss = testInterface(source,Interface_name[i])
            result = resultss.testInterface
            file.write(result)
            file.close()
            print (result)

        file_name = dir_name + '/' + 'summary.txt'
        file = open(file_name, 'w')
        file.write('Start time:'+dir_name+'\n')
        end_time=time.strftime('~/result/'+'%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
        file.write('End time:'+end_time + '\n')
        file.write('Interface number:' + str(len(Interface_name))+ '\n')
        file.write('Success number:' + str(resultss.num_success) + '\n')
        file.write('Fail number:' + str(resultss.num_fail) + '\n')
        file.write('Total number:' + str(resultss.num_success+resultss.num_fail) + '\n')
        file.close()


if __name__ == '__main__':
    unittest.main()







