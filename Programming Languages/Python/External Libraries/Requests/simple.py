import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"

for _ in range(10):
    response = requests.get(url)
    print("The response status is: "+str(response.status_code))
    print(response.json())