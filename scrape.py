from bs4 import BeautifulSoup
from bs4.element import Tag
from bs4.element import NavigableString
import requests
import json

url = 'http://allrecipes.com/search/results/?wt=chocolate%20chip%20cookie&sort=re&page={}'
recipe_key = '/recipe'

recipe_set = set()

page_num = 1
while True:
    page_url = url.format(page_num)
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html5lib')
    search_results = soup.find('div', {'id' : 'searchResultsApp'})
    if search_results:
        articles = search_results.findAll('article')
        if not articles:
            break
        for article in articles:
            link = article.find('a')
            if link is not None:
                recipe_url = link['href']
                if recipe_url.startswith(recipe_key):
                    recipe_set.add(recipe_url)
    else:
        with open('test.json', 'w') as f:
            f.write(json.dumps(list(recipe_set), sort_keys=True, indent=4, separators=(',', ': ')))
        print('bad thing')
    print(page_num)
    page_num += 1

with open('test.json', 'w') as f:
    f.write(json.dumps(list(recipe_set), sort_keys=True, indent=4, separators=(',', ': ')))
