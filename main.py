import requests
import random
from bs4 import BeautifulSoup as bs
import traceback
import pandas as pd

def get_free_proxies():
  url = 'https://free-proxy-list.net/'
  soup = bs(requests.get(url).content, 'html.parser')

  proxies = []
  div_table = soup.find_all('div', class_= 'fpl-list')

  

  ths = []
  tds = []
  for div in div_table:
    ths = div.find_all('th')
  
  ths_text = []
  
  for th in ths:
    ths_text.append(th.text)

  datas = []

  for div in div_table:
    rows = div.find_all('tr')
    row_data = []
    for row in rows[1:]:
      data = row.find_all('td')
      row_data = [each_row.text for each_row in data]
      datas.append(row_data)
  
  proxies = [str(each_ip[0]) + ":" + str(each_ip[1]) for each_ip in datas]
  
  # print(datas[0:5])
  # df = pd.DataFrame(datas)
  # df.columns = ths_text
  # print(df.head())
  
  return proxies
  

url = 'http://httpbin.org/ip'

proxies = get_free_proxies()

for i in range(len(proxies)):
  print('Request Number:', str(i+1))
  proxy = proxies[i]

  try:
    response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=3)
    print(response.json())
  except requests.exceptions.ConnectTimeout:
    print("Time out")
  except:
    print('Other error')