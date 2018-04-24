''' 
author: tta

date: 4.23.2018

note: this program requires a few arguments to be supplied
on the commandline as parameters for the API call

read the API docs here: http://docs.openstates.org/en/latest/api/
'''

import requests
import json
import sys

N = 3	# the current number of desired parameters

def search(api_key, keyword):
	url = "https://openstates.org/api/v1/bills"
	params = {
		'apikey':		api_key,
		'state':		'ny',
		'search_window':	'session',
		'type':			'bill',
		'q':			keyword,
		'fields':		'bill_id,title,action_dates,actions,subjects,sources'
		}
	r = requests.get(url, params=params)
	return r.json()


def pretty_json(obj):
	return json.dumps(obj, indent=4, sort_keys=True)

if __name__ == "__main__":
	if len(sys.argv) != N:
		sys.stderr.write('usage: %s <api_key> <keyword>\n' % sys.argv[0]) # this is
			# to output an error message with guidance to the correct script
			# call. sys.arvg[0] refers to the name of this script.
		sys.exit(1)

	api_key = sys.argv[1]
	keyword = sys.argv[2]

	data = search(api_key, keyword)	# return a json object	
	print(pretty_json(data))	# display the json file in a readable format
