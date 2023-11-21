import requests
import urllib.parse
import json

filename = "repos-private.json"

url = 'https://api.github.com/martincusack979/aprivateone'

apiKey = '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'

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
