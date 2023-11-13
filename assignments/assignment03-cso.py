import requests
import json

# find "exchequer account (historical series)" from CSO
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll():   
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("exchequer.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)


    




