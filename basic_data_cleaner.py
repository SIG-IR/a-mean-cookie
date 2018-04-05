# basic data cleaning
# 1. replaces duplicates with count of duplicates.
# 2. if the item doesnt have an amount, delete it. Some examples of bad data are given:
#   'Cake:',
#   'Reynolds® Parchment Paper',
#   'coarse sea salt',
#   'salt'

import csv
import json
import re
from collections import Counter

file_input = "raw_recipe_ingredients.json"
file_output = "firstclean_recipe_ingredients.json"
# input file operations
data = json.load(open(file_input))

data_counted = list(data)  # Need to change this to something that is open source or something
data_cleaned = list()
# print(sorted(data))
for data in data_counted:
    # if certain string doesn't have a count, delete that entry
    if (re.match(r"(\d)/(\d)", data)):
        # print(data)
        frac = re.match(r"(\d)/(\d)", data).groups()
        out = int(frac[0]) / int(frac[1])

        data = re.sub(r"\d/\d", str(out), data)
        data_cleaned.append(data)
        # print(data)
    elif (re.match(r"\d (\d)/(\d)", data)):
        # print(data)
        frac = re.match(r"\d (\d)/(\d)", data).groups()
        out = int(frac[0]) / int(frac[1])

        data = re.sub(r"\d (\d)/(\d)", str(out), data)
        data_cleaned.append(data)

    else:
        data_cleaned.append(data)

# print("\n".join(sorted(data_cleaned)))

data_cleaned = list(Counter(data_cleaned))  # Need to change this to something that is open source or something
for data in data_cleaned:
    if not re.match(r"[0-9]", data[0]):
        # print(data)
        if data in data_cleaned: data_cleaned.remove(data)

output_dict = {}
for data in data_cleaned:
    word, space, match = str(data).partition(' ')
    print(word + "***" + match)
    output_dict[match] = float(word)
# print("\n".join(sorted(data_cleaned)))
print(output_dict)
# print("\n".join(data_counted))
# print("\n".join(sorted(data_counted)))

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in output_dict.items():
        writer.writerow([key, value])


with open(file_output, 'w') as outfile:
    json.dump(sorted(data_cleaned), outfile)

# duplicate cleaner and assign to

#
# #output file operations
# output = open(txt_file_output, 'w')
# for item in ingredient_list:
#   output.write("%s\n" % ingredient_list)
#
# output.close()
