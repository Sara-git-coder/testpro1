import requests

# r = requests.get("http://baidu.com")
#
# r.encoding = "utf-8"
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print (r.text)

