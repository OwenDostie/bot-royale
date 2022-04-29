import json
import requests

with open('api-key.txt') as f:
    key = f.read()

# url = '''https://api.clashroyale.com/v1/cards'''
# response = requests.get(url)
# t = response.json()
# print(t)