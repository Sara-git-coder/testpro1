import yaml

#load 把yaml格式转成python对象 列表
print (yaml.load ("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
 """,Loader=yaml.FullLoader))





# stream = file('document.yaml', 'w')
# print (yaml.dump ([1, 2, 3], stream))
#    # Output the document to the screen.
# #The yaml.dump function accepts a Python object and produces a YAML document.
# #dump 把一个python对象，如字典转成yaml文件
# print (yaml.dump ({'name': 'Silenthand Olleander', 'race': 'Human',
#                    'traits': ['ONE_HAND', 'ONE_EYE']}))