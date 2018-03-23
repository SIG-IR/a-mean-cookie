# Takes an input json and scrapes the html for ingredients.
# outputs the list as a json.
import glob
from datetime import datetime
from bs4 import BeautifulSoup
import json

path = 'C:/Users/athar/PycharmProjects/a-mean-cookie-re/websites/*.html'  # note C:
files = glob.glob(path)
ingredient_list = list()
chk_tag = 'span'
chk_class = 'recipe-ingred_txt added'
txt_file_output = "raw_recipe_ingredients.json"

startTime = datetime.now()
for name in files:
    cookie_obj = BeautifulSoup(open(name), "html.parser")
    cookie = cookie_obj.find_all(chk_tag, attrs={'class': chk_class})
    # print(cookie)
    for cookie_ingredient in cookie:
        ingredient_list.append(cookie_ingredient.string)

with open(txt_file_output, 'w') as outfile:
    json.dump(sorted(ingredient_list), outfile)

endTime = datetime.now() - startTime
print('process finished in:' + str(endTime))
