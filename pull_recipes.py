# Pulls all recipe websites from 'recipe_twenty_pages.json' and writes
# their HTML files in the 'websites' folder.

# Make sure there is a folder named 'websites' in the main directory.
# Takes 7-10 minutes for 381 recipes.

import json
import os
import random
import time
from datetime import datetime

import requests

NUM_REQUESTS = 20  # Number of requests to make per block.
TIME_TO_SLEEP_LIST = [2, 4, 8, 16, 32]  # Number of seconds to sleep between request blocks.
requestCount = 0

# Used for determining execution time.
startTime = datetime.now()

# Creates a 'websites' folder if it doesn't already exist.
if not os.path.exists('websites'):
    os.makedirs('websites')

# Reads in JSON from file.
with open('recipes_twenty_pages.json') as json_file:
    websites = json.load(json_file)

    # Loops over each url.
    for url in websites:
        # Checks if it should sleep.
        if (requestCount > 0) and (requestCount % NUM_REQUESTS == 0):
            i = random.randint(0, 4)
            TIME_TO_SLEEP = TIME_TO_SLEEP_LIST[i]
            time.sleep(TIME_TO_SLEEP)

        # Gets the html of the website.
        response = requests.get(url)
        html = response.text

        # Formats and sets the file name (Ex: 'websites/recipe083.txt')
        countFormat = '{num:003d}'.format(num=requestCount)
        filename = 'websites/recipe' + countFormat + '.html'

        # Writes the html to a file.
        with open(filename, 'w') as outfile:
            outfile.write(html)

        requestCount += 1

# Prints recipe count and execution time.
execTime = datetime.now() - startTime
print('Wrote ' + str(requestCount) + ' recipes in ' + str(execTime))
