# coding: utf-8
from locale import currency
import requests
import pandas as pd

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/tickers'
# query_param = 'currency_pair=BTC_USDT'
query_param = ''
r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
mylist = r.json()
# mydict = mylist[0]

# df=pd.DataFrame(mylist , columns=["currency_pair","last","lowest_ask","highest_bid","change_percentage","base_volume","quote_volume","high_24h","low_24h"])
df=pd.DataFrame(mylist)
df.to_csv("gateio.csv",index=False)