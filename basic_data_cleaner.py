# basic data cleaning
# 1. replaces duplicates with count of duplicates.
# 2. if the item doesnt have an amount, delete it. Some examples of bad data are given:
#   'Cake:',
#   'Reynolds® Parchment Paper',
#   'coarse sea salt',
#   'salt'

from collections import Counter
import json
import re

file_input = "raw_recipe_ingredients.json"
file_output = "firstclean_recipe_ingredients.json"
# input file operations
data = json.load(open(file_input))
data_counted = list(Counter(data))  # Need to change this to something that is open source or something

for data in data_counted:
    if not re.match(r"[0-9]", data[0]):
        print(data)
        if data in data_counted: data_counted.remove(data)

with open(file_output, 'w') as outfile:
    json.dump(sorted(data_counted), outfile)

# duplicate cleaner and assign to

#
# #output file operations
# output = open(txt_file_output, 'w')
# for item in ingredient_list:
#   output.write("%s\n" % ingredient_list)
#
# output.close()
