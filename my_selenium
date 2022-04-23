from selenium import webdriver
import time
import bs4


path="./chromedriver"
url="https://www.baidu.com"

browser=webdriver.Chrome(path)
browser.get(url)
webCode=browser.page_source
# print(webCode)
soup=bs4.BeautifulSoup(webCode,"html.parser")
print(soup.title)


# myInput=browser.find_element_by_id("kw")
# myInput.send_keys("Tony")
# time.sleep(2)
# myButton=browser.find_element_by_id("su")
# myButton.click()
time.sleep(2)
