import urllib.parse
query = 'Hello World@Python'
parsed = urllib.parse.quote(query)
print(parsed)