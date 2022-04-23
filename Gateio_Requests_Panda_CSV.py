# coding: utf-8
import requests
import pandas as pd

#构建URL
host = "https://api.gateio.ws"
prefix = "/api/v4"
url = '/spot/tickers'

#构建请求头
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

# query_param = 'currency_pair=BTC_USDT'
query_param = ''

#获得gateio的币种的数据：名称，报价，涨跌幅等
r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
mylist = r.json()
# mydict = mylist[0]

# df=pd.DataFrame(mylist , columns=["currency_pair","last","lowest_ask","highest_bid","change_percentage","base_volume","quote_volume","high_24h","low_24h"])
#将数据转换为DataFrame
#mylist是一个列表，每个元素，内容是币种，类型是字典，可以理解成excel的一行
df=pd.DataFrame(mylist)

#保存到csv
df.to_csv("gateio.csv",index=False)