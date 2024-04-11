import requests
import json

url = "https://vgtechdemo.com/gopaddiberlin/gopaddiberlinbkend/web/activity/destinations"

def searchdestination(city):
  payload = f'''{{\"search\": "{city}"}}'''
  headers = {
      "Token": "gopaddi@v1",
      "Userid": "10"
  }
  response = requests.request("POST", url, data=payload, headers=headers)
  data=json.loads(response.text)
  # {"success":true,"message":"","data":[{"destinations":[{"title":"New York Area - Ny,United States","countryId":"629","cityId":"629"},
  #                                         {"title":"York,United Kingdom","countryId":"731","cityId":"731"}]}]}
  title=data['data'][0]['destinations']
  title_list=[]
  for i in title:
    title_list.append(i['title'])
  return title_list
