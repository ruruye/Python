import requests
from bs4 import BeautifulSoup
from dask.dataframe.tests.test_rolling import idx

url = 'http://127.0.0.1:8000/emp_list'

response = requests.get(url)
#print("response",response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.select("tr"))

trs = soup.select("tr")
for idx,tr in enumerate(trs):
    if idx ==0:
        continue
    tds = tr.select("td")
    print(tds[1].text,tds[3].text)