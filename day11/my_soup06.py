import requests
from bs4 import BeautifulSoup

url = 'https://stock.mk.co.kr/price/home/KR7011150000'

response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
print("soup",soup)
    
my_trading_valume = soup.select("#trading_valume")
my_transaction_acmount = soup.select("#transaction_acmount")
my_table_stock = soup.select(".table-stock")
my_vs = my_table_stock[1].select(".volume")

print("거래량",my_trading_valume[0].text)
print("거래대금(백만)",my_transaction_acmount[0].text)
print("자본금(억)",my_vs[2].text.strip())
print("상장주식수(천주)",my_vs[3].text.strip())
print("가총액(백만)",my_vs[4].text.strip())
print("외국인보유비중",my_vs[5].text.strip().replace("%","").strip())
print("PER",my_vs[6].text.strip().split("/")[0].strip())
print("거EPS",my_vs[6].text.strip().split("/")[1].strip())
