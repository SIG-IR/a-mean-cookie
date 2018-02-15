#Reads a JSON file and prints out all the text elements embedded within class chk_class having tag chk_tag

from bs4 import BeautifulSoup
import urllib
import json
from pprint import pprint

chk_tag = 'span'
chk_class = 'recipe-ingred_txt added'
ingredient_set = set()
json_file = "recipes_twenty_pages.json"

allCookies = json.loads(open(json_file).read())

for i in range(10):  #len(allCookies):
    print(allCookies[i])
    page_url = urllib.request.urlopen(allCookies[i])
    cookie_obj = BeautifulSoup(page_url, "lxml")
    cookie = cookie_obj.find_all(chk_tag, attrs={'class':chk_class})
    for cookie_ingredient in cookie:
       ingredient_set.add(cookie_ingredient.string)

pprint(sorted(ingredient_set))