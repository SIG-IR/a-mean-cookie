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

data_counted = list(Counter(data).items())  # Need to change this to something that is open source or something
# pprint(data_counted)

data_cleaned = list()
for data in data_counted:
    # if certain string doesn't have a count, delete that entry
    if (re.match(r"(\d)/(\d)", data[0])):
        frac = re.match(r"(\d)/(\d)", data[0]).groups()
        out = (int(frac[0]) / int(frac[1])) * int(data[1])
        data_clean = (re.sub(r"\d/\d ", str(''), data[0]), out)
        data_cleaned.append(data_clean)
        # print(data_clean)
    elif (re.match(r"\d (\d)/(\d)", data[0])):
        frac = re.match(r"\d (\d)/(\d)", data[0]).groups()
        out = (int(frac[0]) / int(frac[1])) * int(data[1])

        data_clean = (re.sub(r"\d (\d)/(\d) ", str(''), data[0]), out)
        data_cleaned.append(data_clean)

data_cleaned_tuple = {}

for data, values in data_cleaned:
    if data not in data_cleaned_tuple:
        data_cleaned_tuple[str(data)] = []
        data_cleaned_tuple[str(data)].append(float(values))
        data_cleaned_tuple[str(data)].append(1.0)

    else:
        data_cleaned_tuple[str(data)][0] += float(values)
        data_cleaned_tuple[str(data)][1] += 1.0

data_cleaned_mean = dict()
for data, list in data_cleaned_tuple.items():
    data_cleaned_mean[str(data)] = round(float(list[0] / list[1]))

# pprint(data_cleaned_2)
# for data, values in data_cleaned:
#     if (data_cleaned.count())
# for data in data_cleaned_2:
#     num, space, word = (str(data[0])).partition(' ')
#     print(num + ' ' + word + '-' + str(data[1]) + '\n')
#     num2 = num * data[1]
#     print('edit:' + num2 + ' ' + word + '\n')


# output_dict_count = Counter(data_cleaned_2).items()
# #pprint(output_dict_count)
# output_mean_dict = {k: v / 1  for k, v in output_dict.items()}
output_cleaned_dict = {}
# #pprint(sorted(output_dict.items(), key=operator.itemgetter(0)))
for keys in data_cleaned_mean:
    if data_cleaned_mean[keys] <= 1.0:
        continue
    else:
        output_cleaned_dict.update({keys: data_cleaned_mean[keys]})
#
#
#
# #pprint(output_cleaned_dict)
#
#
with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in output_cleaned_dict.items():
        writer.writerow([key, value])

#
#
# # duplicate cleaner and assign to
#
# #
# # #output file operations
# # output = open(txt_file_output, 'w')
# # for item in ingredient_list:
# #   output.write("%s\n" % ingredient_list)
# #
# # output.close()
