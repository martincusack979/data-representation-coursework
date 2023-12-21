import requests
import json
from github import Github
from config import config as cfg

filename = "repos-assignment4.json"

url = 'https://api.github.com/repos/martincusack979/assignment4'

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)