import requests
import csv

from xml.dom.minidom import parse, parseString

url: "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"


page = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
doc = parseString(page.content)
# check that it works



