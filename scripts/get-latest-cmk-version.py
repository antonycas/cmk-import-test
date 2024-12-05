#!/usr/bin/env python3

import sys

string = sys.argv[1]

if 'p' in string:
    print(string)
else:
    print(f"p not in {string}")
