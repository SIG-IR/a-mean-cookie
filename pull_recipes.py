# Pulls all recipe websites from 'recipe_twenty_pages.json' and writes
# their HTML to text files in the 'websites' folder.
# Takes ~7 minutes for 381 recipes.

import requests
import json
import time
from datetime import datetime

NUM_REQUESTS = 20	# Number of requests to make before each sleep.
TIME_TO_SLEEP = 5 	# Number of seconds to sleep between requests.
count = 0

# Used for determining execution time.
startTime = datetime.now()

# Reads in JSON from file.
with open('recipes_twenty_pages.json') as json_file:
	websites = json.load(json_file)
	
	# Loops over each url.
	for url in websites:
		# Checks if it should sleep.
		if count % NUM_REQUESTS == 0:
			time.sleep(TIME_TO_SLEEP)
		
		# Formats and sets the file name (Ex: 'websites/recipe083.txt')
		countFormat = '{num:003d}'.format(num = count)
		filename = 'websites/recipe' + countFormat + '.txt'
		
		# Gets the html for the url.
		response = requests.get(url);
		html = response.text
		
		# Writes the html to a file.
		with open(filename, 'w') as outfile:
			outfile.write(html)
		
		count += 1

# Prints recipe count and execution time.
execTime = datetime.now() - startTime
print('Wrote ' + str(count) + ' recipes in ' + str(execTime))