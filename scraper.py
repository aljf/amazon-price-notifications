from bs4 import BeautifulSoup
import urllib.request
import re 
import locale


# TODO Grab the url from my site form 
product_url = 'https://www.amazon.com/Apple-MacBook-15-inch-512GB-Storage/dp/B07S58MHXF/ref=sr_1_3?crid=FNIHK7IY3CFT&keywords=macbook+pro+15+inch&qid=1576365616&s=electronics&sprefix=macbookpro%2Celectronics%2C205&sr=1-3'

source = urllib.request.urlopen(product_url).read()

soup = BeautifulSoup(source,'lxml')

decimal_point_char = locale.localeconv()['decimal_point']
raw_price = soup.find(id="priceblock_ourprice").get_text().replace('$', '')
price = re.sub(r'[^0-9'+decimal_point_char+r']+', '', raw_price)

print(price)

# TODO send price to mail.py and check if it is low enough