import json;
import requests
jsondata=requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=840d79976e9497d0a7a6ba0b2a886be8");
print(json.loads(jsondata.text))
