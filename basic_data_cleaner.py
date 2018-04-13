# basic data cleaning
# 1. replaces duplicates with count of duplicates.
# 2. if the item doesnt have an amount, delete it. Some examples of bad data are given:
#   'Cake:',
#   'Reynolds® Parchment Paper',
#   'coarse sea salt',
#   'salt'
# 3.

import csv
import json
import re
from pprint import pprint

# input file operations
file_input = "raw_recipe_ingredients.json"
file_output = "firstclean_recipe_ingredients.jsonf"
outputCSV = "output_dict.csv"
data = json.load(open(file_input))
# pprint(data)

# RegEX cleaner for data
data_cleaned = list()
for element in data:
    # print(element)
    if (re.match(r"(\d)/(\d)", element)):
        frac = re.match(r"(\d)/(\d)", element).groups()
        out = (int(frac[0]) / int(frac[1]))
        data_clean = (re.sub(r"\d/\d ", str(''), element), out)
        data_cleaned.append(data_clean)
    elif (re.match(r"\d (\d)/(\d)", element)):
        frac = re.match(r"(\d) (\d)/(\d)", element).groups()
        out = (int(frac[1]) / int(frac[2])) * int(frac[0])
        data_clean = (re.sub(r"\d (\d)/(\d) ", str(''), element), out)
        data_cleaned.append(data_clean)

# pprint(data_cleaned)

#Counter
data_cleaned_tuple = {}

for data, values in data_cleaned:
    if data not in data_cleaned_tuple:
        #print(data)
        data_cleaned_tuple[str(data)] = []
        data_cleaned_tuple[str(data)].append(float(values))
        data_cleaned_tuple[str(data)].append(1.0)
    else:
        data_cleaned_tuple[str(data)][0] += float(values)
        data_cleaned_tuple[str(data)][1] += 1.0
# pprint(data_cleaned_tuple)


#Mean Operation (heh)
data_cleaned_mean = dict()
for data, list in data_cleaned_tuple.items():
    data_cleaned_mean[str(data)] = float(list[0] / list[1])
# pprint(data_cleaned_mean)

#Output Operations
output_cleaned_dict = {}
for keys in data_cleaned_mean:
    if data_cleaned_mean[keys] <= 0.5:
        continue
    else:
        output_cleaned_dict.update({keys: round(data_cleaned_mean[keys], 2)})
pprint(output_cleaned_dict)
with open(outputCSV, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in output_cleaned_dict.items():
        writer.writerow([key, value])

# data_counted = list(Counter(data).items())
# pprint(data_counted)
# data_cleaned = list()
# for data in data_counted:
#     if (re.match(r"(\d)/(\d)", data[0])):
#         frac = re.match(r"(\d)/(\d)", data[0]).groups()
#         out = (int(frac[0]) / int(frac[1])) * int(data[1])
#         data_clean = (re.sub(r"\d/\d ", str(''), data[0]), out)
#         data_cleaned.append(data_clean)
#         # print(data_clean)
#     elif (re.match(r"\d (\d)/(\d)", data[0])):
#         frac = re.match(r"\d (\d)/(\d)", data[0]).groups()
#         out = (int(frac[0]) / int(frac[1])) * int(data[1])
#
#         data_clean = (re.sub(r"\d (\d)/(\d) ", str(''), data[0]), out)
#         data_cleaned.append(data_clean)
#
# data_cleaned_tuple = {}
#
# for data, values in data_cleaned:
#     if data not in data_cleaned_tuple:
#         data_cleaned_tuple[str(data)] = []
#         data_cleaned_tuple[str(data)].append(float(values))
#         data_cleaned_tuple[str(data)].append(1.0)
#
#     else:
#         data_cleaned_tuple[str(data)][0] += float(values)
#         data_cleaned_tuple[str(data)][1] += 1.0
# # pprint(data_cleaned_tuple)
# data_cleaned_mean = dict()
# for data, list in data_cleaned_tuple.items():
#     data_cleaned_mean[str(data)] = round(float(list[0] / list[1]))
#
# # pprint(data_cleaned_2)
# # for data, values in data_cleaned:
# #     if (data_cleaned.count())
# # for data in data_cleaned_2:
# #     num, space, word = (str(data[0])).partition(' ')
# #     print(num + ' ' + word + '-' + str(data[1]) + '\n')
# #     num2 = num * data[1]
# #     print('edit:' + num2 + ' ' + word + '\n')
#
#
#
# output_cleaned_dict = {}
# for keys in data_cleaned_mean:
#     if data_cleaned_mean[keys] <= 1.0:
#         continue
#     else:
#         output_cleaned_dict.update({keys: data_cleaned_mean[keys]})
#
# with open('dict.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in output_cleaned_dict.items():
#         writer.writerow([key, value])
