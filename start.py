from autoBuildCase import buildCase as bc
from autoBuildCase import writeToFile as wf

user_input = bc.getInput()
size = bc.analyzeInput(user_input)
case_dic = bc.buildDataDic(size)
print(case_dic)
# wf.writeToCSV(case_dic)
