import bs4
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def parsePrice():
    r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    price=soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

for x in range(0,3):
    print('The current price: '+ str(parsePrice()))