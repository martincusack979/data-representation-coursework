import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbookbyId(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    book = {
        'Author': "Jimmy",
        'Title' : "blahblahblah",
        'Price' : 777
    } 
     
    response = requests.post(url,json=book)
    return response.json()

def deletebook(id):
    geturl = url + "/" + str(id)
    response = requests.delete(geturl)
    return response.json()


if __name__ == "__main__":
    # print (createBook({}))
    # print (getallbooks())
    # print (getbookbyId(1))
    print (deletebook(335))






