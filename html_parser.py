# Reads a txt file and writes out all the text elements embedded within class chk_class having tag chk_tag
from bs4 import BeautifulSoup

# from pprint import pprint

chk_tag = 'span'
chk_class = 'recipe-ingred_txt added'
ingredient_list = list()
txt_file_input = "cookie.txt"
txt_file_output = "data.txt"

with open(txt_file_input, 'r') as input_stream:
    data = input_stream.read().replace('\n', '')

# pprint(data)
cookie_obj = BeautifulSoup(data, "lxml")
cookie = cookie_obj.find_all(chk_tag, attrs={'class': chk_class})
for cookie_ingredient in cookie:
    ingredient_list.append(cookie_ingredient.string)
# pprint(sorted(ingredient_list))

output = open(txt_file_output, 'w')
for item in ingredient_list:
    output.write("%s\n" % ingredient_list)

output.close()
