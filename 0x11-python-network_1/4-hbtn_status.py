#!/usr/bin/python3
# Script that fetches a  given url
# Using urllib module
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    rawData = response.read()

    convertData = rawData.decode("UTF-8")
    print("Body response:")
    print("\t- type: {}".format(type(convertData)))
    print("\t- content: {}".format(convertData))
