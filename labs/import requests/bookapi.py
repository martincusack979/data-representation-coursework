[{"Author":"Test124","Price":5,"Title":"Test","id":122},{"Author":"adf","Price":32,"Title":"Skills needed by a Data Scientist","id":163},{"Author":"andrew","Price":12,"Title":"javascript","id":179},{"Author":"andrew","Price":122,"Title":"javascript","id":180},{"Author":"Roy Keane","Price":155,"Title":"The Second Half","id":181},{"Author":"andrew","Price":10000000,"Title":"javascript","id":183},{"Author":"andrew","Price":10000000,"Title":"javascript","id":184},{"Author":"andrew","Price":10000000,"Title":"javascript","id":185},{"Author":"shane","Price":2,"Title":"test","id":193},{"Author":"mark","Price":22,"Title":"dog","id":195},{"Author":"JK Rowling","Price":999,"Title":"magic","id":197},{"Author":"Andrew","Price":12,"Title":"Javascript","id":198},{"Author":"Me","Price":3000,"Title":"My Book","id":280},{"Author":"Sean","Price":30,"Title":"Coding for Dummies","id":281},{"Author":"ooo","Price":20000,"Title":"HelloWorld!","id":285},{"Author":"Orla","Price":19000,"Title":"HelloWorld2!","id":286},{"Author":"OrlaC","Price":10,"Title":"LovePython!","id":290},{"Author":"asdfsd","Price":11111,"Title":"overviewasd","id":321},{"Author":"test test test","Price":2222,"Title":"testing title","id":324},{"Author":"test test test","Price":123412,"Title":"testing title","id":326}]
from bookapidao import getallbooks

books = getallbooks()
total = 0
count = 0
for book in books:
    total += book["Price"]
    count += 1

print("average of", count, "books is", total/count)    
