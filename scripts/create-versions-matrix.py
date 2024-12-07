#!/usr/bin/env python3
import sys
import requests
import json

url = "https://download.checkmk.com/stable_downloads.json"
res = requests.get(url)
data = json.loads(res.text)

try:
    versions_arg = sys.argv[1]
except IndexError as e:
    print("No Version Provided")
    sys.exit(2)

versions = versions_arg.split(",")

#matrix = {"include": [ {"version": data["checkmk"][version]["version"]} for version in versions ]}
matrix = {"include": [ {"version": data["checkmk"][version]["version"] } for version in versions ]} 
json_matrix = str(matrix).replace("'",'\\"')

test_matrix = json.dumps(matrix).replace('"','\\"')

print(test_matrix)
#print(matrix)
#print(json_matrix)