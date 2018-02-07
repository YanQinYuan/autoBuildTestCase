# AutoBuildTestCase

### Introduce
This a project helps you build test case automatically.

### TDD
### Function

1. if you input like 'varchar(8)', it will automatically build testcase like '12345678','qwe123qweqw'
and declare it True or False.


### Quick Start.


## CHINESE:

1. 根据用户输入生成随机字符串
2. 根据生成的字符串组合成测试用例
3. 保存测试用例到文件里

例子：你输入 【varchar(8)】,程序自动生成 一个 excel 文件，内容涵盖所有覆盖这个规则的用例，如
【12345678，True】【qwertytyu，False】【0，Ture】【aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa，False】

ChangeLog:
面向对象改写：以 varchar, datetime, int 等数据类型为对象
