#!/usr/bin/env python3
import sys
import requests
import json

url = "https://download.checkmk.com/stable_downloads.json"
res = requests.get(url)
data = res.json()

if __name__ == "__main__":
    try:
        versions_arg = sys.argv[1]
        versions = versions_arg.replace(" ","").split(",")
    except IndexError as e:
        print("No Version Provided")
        sys.exit(2)

    latest_versions_array = []
    for version in versions:
        try:
            if 'p' in version:
                latest_versions_array.append(version)
            else: 
                latest_versions_array.append(data["checkmk"][version]["version"])
        except KeyError as e:
            print(f"No Version found for {version}")
            sys.exit(2)

    print(str(latest_versions_array).replace("'",'"'))
