#!/usr/bin/python3
"""Script documentation for voting page

   This script votes for a specific ID number a total of 1024 times
"""
import requests

url = 'http://158.69.76.135/level0.php'
data = {'id': 300, 'holdthedoor': 'vote'}
votes_counted = 0

for i in range(1024):
    requests.post(url, data)
    votes_counted += 1

print("Votes: {}".format(votes_counted))
