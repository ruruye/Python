import requests
from bs4 import BeautifulSoup

url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry'
# url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kosdaq&status=industry'


response = requests.get(url)
# print("response", response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

row_stys = soup.select(".row_sty")
for idx, rs in enumerate(row_stys):
    s_code = rs.select("a")[0]['href'].split("/")[3]
    s_name = rs.select("a")[0].text.strip()
    price = rs.select(".st_price")[0].text.strip()
    print(idx,s_code, s_name, price)