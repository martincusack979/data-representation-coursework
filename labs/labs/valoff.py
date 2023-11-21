import requests
import json
url = "https://api.valoff.ie//api/Property/GetProperties?Fields=LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=LEISURE&Format=csv&Download=false"

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("valoff.json", "wt") as fp:
        print(json.dumps(getAll()), file = fp)