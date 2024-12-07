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

versions_array = [ data["checkmk"][version]["version"] for version in versions ]
#for version in versions:
#    versions_array.append(data["checkmk"][version]["version"])
print(str(versions_array).replace("'",'"'))
