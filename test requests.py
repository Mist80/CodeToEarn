import requests

try:
    myResponse=requests.get("http://ifeng.com")
except:
    print("my error")
else:
    print(myResponse.text)