#Reads a txt file and prints out all the text elements embedded within class chk_class having tag chk_tag

from bs4 import BeautifulSoup
import urllib
import json
from pprint import pprint

chk_tag = 'span'
chk_class = 'recipe-ingred_txt added'
ingredient_set = list()
json_file = "recipes_twenty_pages.json"

with open('cookie.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

#pprint(data)
cookie_obj = BeautifulSoup(data, "lxml")
cookie = cookie_obj.find_all(chk_tag, attrs={'class': chk_class})
for cookie_ingredient in cookie:
    ingredient_set.append(cookie_ingredient.string)
pprint(sorted(ingredient_set))

'''
allCookies = json.loads(open(json_file).read())
#open the fle read the file and get the
for i in range(1):  #len(allCookies):
    print(allCookies[i])
    page_url = urllib.request.urlopen(allCookies[i])
    cookie_obj = BeautifulSoup(page_url, "lxml")
    cookie = cookie_obj.find_all(chk_tag, attrs={'class':chk_class})
    for cookie_ingredient in cookie:
       ingredient_set.append(cookie_ingredient.string)

pprint(sorted(ingredient_set))
'''