#coding: utf-8
# 测试驱动开发，先编写测试文档
import openpyxl as xl
import random
import string
import re

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
    size = re.findall('\((.*?)\)', res))
    return size

# 根据生成器产生的数据生成一组测试数据
def buildDataList(size):
    pass
    return

# 把数据写入文档（txt or excel）
def writeDataToDoc(DocType, data):
    if DocType == "txt":
        pass
    if DocType == "excel":
        pass
    else:
        print("暂不支持该格式，请选择其它格式。")

# if __name__ == '__main__':
#     user_input = getInput()
#     analyzeInput(user_input)
