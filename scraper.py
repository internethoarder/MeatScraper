import requests
from bs4 import BeautifulSoup


URL = 'https://www.christensenranch.com/product-category/boxed-beef/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#title = soup.find("div",{"class":'product-title__name'}).get_text()
#price = soup.findAll("span",{"class":'price'})
for el in soup.find_all('span', attrs={'class': 'woocommerce-Price-amount amount'}):
    print (el.get_text())

#print(price)
