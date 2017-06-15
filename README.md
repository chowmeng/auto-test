# auto-test
这是一个用python写的自动化接口测试框架。
config.ini文件中Interface_name=login,addartical用来记录需要测试的接口。测试用例保存在testCase\source.xlsx中，sheet页名称为测试的接口名称，如果需要对某些测试用例进行执行，需要将sheet页名称添加到ini文件Interface_name=后，并用‘，‘隔开。
目前只能执行post和get的接口测试，结果存储在result文件夹中。
