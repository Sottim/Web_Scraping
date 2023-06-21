import requests
from bs4 import BeautifulSoup 

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

beautifulSoup = BeautifulSoup(r.content, 'html.parser')
print(beautifulSoup.prettify())

