import requests
import json
from config import config as cfg

filename = "repos-private.json"
apikey = "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"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# the more basic way of setting authorization
# headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)