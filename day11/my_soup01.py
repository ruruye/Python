import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp_list'

response = requests.get(url)
#print("response",response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
trs = soup.find_all('tr')

for idx, tr in enumerate(trs):
    if idx ==0 :
        continue
    tds = tr.find_all('td')
    
    print(tds[1].text,tds[3].text)