import requests
from bs4 import BeautifulSoup


URL = 'https://www.christensenranch.com/product-category/boxed-beef/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#title = soup.find("div",{"class":'product-title__name'}).get_text()
#price = soup.findAll("span",{"class":'price'})
#for el in soup.find_all('span', attrs={'class': 'woocommerce-Price-amount amount'}):
 #   print (el.get_text())
#for title in soup.find_all('h2', attrs={'class': 'woocommerce-loop-product__title'}):
 #   print (title.get_text())
#print(price)

results = soup.find("ul",{"class":'products columns-3'})

beef_elements = results.find_all("li", class_="product_tag-beef-boxes")

for beef_elements in beef_elements:
    price_element = beef_elements.find("span", class_="woocommerce-Price-amount amount")
    title_element = beef_elements.find("h2", class_="woocommerce-loop-product__title")
    print(title_element.text.strip())
    print(price_element.text.strip())




#beef_element = results.find_all("li", class_="none product type-product post-21079 status-publish first instock product_cat-best-sellers product_cat-boxed-beef product_cat-holiday product_tag-beef-boxes product_tag-holiday-gifts product_tag-brisket has-post-thumbnail shipping-taxable purchasable product-type-simple")

#for beef_element in beef_element:
  #  print(beef_element, end="\n"*2)
