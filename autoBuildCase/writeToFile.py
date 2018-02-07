from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
import csv


# 把数据(字典)写入 excel
def writeToExcel(data):
    wb = Workbook()
    dest_filename = '../case/case.xlsx'
    # grab the active worksheet
    ws1 = wb.active
    ws1.title = "range names"
    # for key, value in data.items():
    #     for row in range(1,10):
    #         ws1.append(key)
    for row in range(1,len(data)+1):
        for key, value in data.items():
            ws1.append(key, value)
    wb.save(filename = dest_filename)
# 把数据写入 txt
# def writeToTxt(data):
# def writeToCSV(data):
#     writer = csv.writer(open('./case/dict.csv', 'wb'))
#     for key, value in data.items():
#         writer.writerow([key, value])

def writeToCSV(data):
    with open('./case/dict.csv', 'w') as f:
        l = []
        for k, v in data.items(): 
            l.append('%s: %s' % (str(k), str(v))) # Build a nice list of strings
            f.write(', '.join(l))
