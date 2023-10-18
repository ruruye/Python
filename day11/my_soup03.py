import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp_list_fake'

response = requests.get(url)
#print("response",response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')


tab = soup.select_one(".real")


trs = tab.select("tr")
for idx,tr in enumerate(trs):
    if idx ==0:
        continue
    tds = tr.select("td")
    print(tds[1].text,tds[3].text)