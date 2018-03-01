import requests
import json

#Gets a request from the URL.
request = requests.get("http://allrecipes.com/recipe/17165/big-soft-ginger-cookies/")
#Gets the HTML from the request.
html = response.text
#Writes the HTML to a text file in the 'websites' folder.
with open('websites/cookie.txt', 'w') as outfile:
    outfile.write(html)
