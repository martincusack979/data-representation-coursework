import requests
import urllib.parse


from config import config as cfg

targetUrl = "https://en.wikipedia.org"
apiKey = cfg["rtQ6A9S9j89Avc6e7gPCxbTPuFyXBifC26iPkmuFFddZjA7ERbhkq3pwwbOI4CkJ"]


config = {
"htmltopdfkey":"rtQ6A9S9j89Avc6e7gPCxbTPuFyXBifC26iPkmuFFddZjA7ERbhkq3pwwbOI4CkJ"
}


apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)