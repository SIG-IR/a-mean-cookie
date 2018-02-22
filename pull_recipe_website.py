import requests
import json

response = requests.get("http://allrecipes.com/recipe/17165/big-soft-ginger-cookies/")
t = response.text
with open('cookie.txt', 'w') as outfile:
    outfile.write(t)

#print (type(classes))
#bs.find_all("a")
#div = bs.find("div")
#div.find('div')
#bs.find('div', {'class' : 'col-xs-6'})
