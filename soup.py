import bs4
import requests
import pandas as pd

myURL="https://www.baidu.com"
myPage=requests.get(myURL)
myPageSoup=bs4.BeautifulSoup(myPage.text, "html.parser")

# for link in myPageSoup.find_all('a'):
#     print(link.get('href'))

for link in myPageSoup.find_all(True):
    print(link.name)