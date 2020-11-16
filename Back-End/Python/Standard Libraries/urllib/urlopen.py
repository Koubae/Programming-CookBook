from urllib.request import urlopen
import json


url = "https://jsonplaceholder.typicode.com/todos"
read_response = urlopen(url)
print(read_response)
with urlopen(url) as f:
    for i in f:
        print(i)