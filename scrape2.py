from bs4 import BeautifulSoup
from bs4.element import Tag
from bs4.element import NavigableString
import requests
import json

page_url = 'http://allrecipes.com/recipe/261171/double-peanut-butter-milk-chocolate-chip-cookies/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202'

response = requests.get(page_url)
soup = BeautifulSoup(response.text, 'html5lib')

articles = soup.findAll('ul', {'id' : 'lst_ingredients_*'})
for article in articles:
    print(article)