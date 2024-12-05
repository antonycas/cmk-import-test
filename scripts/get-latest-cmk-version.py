#!/usr/bin/env python3

import sys
import requests
import json

try:
    version = sys.argv[1]
except IndexError as e:
    print("No Version Provided")
    sys.exit(2)

def get_latest_version(version):
    url = "https://download.checkmk.com/stable_downloads.json"
    res = requests.get(url)
    data = json.loads(res.text)

    try:
        latest_version = data['checkmk'][version]['version']    
    except Exception as ex:
        print(f"No JSON Data Returned For Version: {version}")
        sys.exit(2)

    return latest_version

if 'p' in version:
    print(version)
else:
    print(get_latest_version(version))
