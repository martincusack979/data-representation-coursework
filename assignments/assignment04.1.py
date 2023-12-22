import requests
import json
from github import Github
from config import config as cfg

filename = "repos-assignment4.json"

# create new repository for purposes of assignment named "assignment 4"

url = 'https://api.github.com/repos/martincusack979/assignment4'

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)


# get the download url of the file in "assignment 4" repository called replace.txt    
fileinfo = repo.get contents("replace.txt")
urlOfFile= fileInfo.download_url

# make hhtp request to the file
response = requests.get(urlOfFile)
contentOfFile = response.text

# Update the contents of the file on git up by using the function 

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)



