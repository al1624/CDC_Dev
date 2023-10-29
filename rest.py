import requests

url = "http://localhost:8083/connectors"


try:
    r = requests.get(url)
    data = r.text
    print(data)
except Exception as e:
    print(e)