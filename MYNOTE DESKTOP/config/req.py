import requests

url = 'http://192.168.10.173:6001'

#demonstrate how to use the 'params' parameter:
x = requests.get(url)
print(x.text)