"""
json 是一种非常流行的，轻量级的数据交换格式
json 对人友好，易于读写
json 对机器友好，易于解析和生成
json 是由列表和字典组成

使用场景：
生成：将对象生成为字符串，存入文件、数据库在网络传输
解析：解析来自文件，数据库，网络传输的字符串python对象
跨语言的数据交换：比如python和C c++/java/havascripts的数据交换
"""


import json
info = [{
            "name":'Tom',
            "gender":'male',
            "age":20

        },{
            "name": 'Sara',
            "gender": 'female',
            "age": 30
        },{
            "name": 'Jerry',
            "gender": 'male',
            "age": 12
        }
]
#dumps 将json转换成字符串
# data = json.dumps(info,sort_keys=False,indent=4)
# print (data)
# print(type(data))

#dump把数据类型转成字符串并存储在文件中
print("读取json文件")
json.dump(info,open("testdata/json_dump.json","w"))
print("读写结束")
