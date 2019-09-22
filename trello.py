import requests
import keys

url = "https://api.trello.com/1/cards"


querystring = {"name":"TestingAPI","desc":"Idk Does this work","pos":"top","idList":"5d828f95517f922a4c16833d","keepFromSource":"all","key":keys.apiKey,"token":keys.tokenKey}

response = requests.request("POST", url, params=querystring)

print(response.text)
