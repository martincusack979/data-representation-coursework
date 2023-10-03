import requests

page = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
print(page)
print("------------")
print(page.content)
