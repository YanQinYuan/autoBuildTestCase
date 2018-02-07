#coding: utf-8
# 测试驱动开发，先编写测试文档
import openpyxl as xl
import random
import string
import re

from openpyxl import Workbook

# 得到用户输入
def getInput():
    user_input = input("请输入规则")
    return user_input

# varchar 随机生成器：根据数字（）生成含英文，字符，数字的组合
def varcharBuild(size=6, chars=string.ascii_uppercase + string.digits):
    data = ''.join(random.choice(chars) for _ in range(size))
    return data

# 拆解用户输入的信息，比如 varchar(8) 拆解成 varchar ，8,返回数组 ["8"]
def analyzeInput(user_input):
    # 获取varchar()里的数字
    res = str(user_input)
    size = re.findall('\((.*?)\)', res)
    return size[0]

# 根据生成器产生的数据生成一组测试数据；
# 临界值，等价类，sql注入，
def buildDataDic(size):
    maxNum = 0 # 临界值, 结果 0 (False)
    minNum = 0 # 临界值，结果 1 (True)
    comNum = 0 # 普通值
    maxmax = 0 # 最大值
    case_dic = {}
    maxNum = int(size) + 1
    maxNum = varcharBuild(maxNum)
    minNum = int(size) + 1
    minNum = varcharBuild(minNum)
    comNum = int(size)
    comNum = varcharBuild(comNum)
    maxmax = int(size) ** 2
    maxmax = varcharBuild(maxmax)
    case_dic.update({
        maxNum:0,
        minNum:1,
        comNum:1,
        "0":1,
        maxmax:0
    })
    return case_dic

# 把数据写入文档（txt or excel）
def writeDataToDoc(DocType, data):
    if DocType == "txt":
        pass
    if DocType == "excel":
        pass
    else:
        print("暂不支持该格式，请选择其它格式。")
