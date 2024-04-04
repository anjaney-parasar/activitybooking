import http.client
import json
from pprint import pprint

conn = http.client.HTTPSConnection("vgtechdemo.com")

def searchactivities(city,startDate,endDate,adults,children,ages):
  payload = f"""{{
    "location": "{city}",
    "date": "{startDate} - {endDate}",
    "adultNo": "{adults}",
    "childNo": "{children}",
    "childAges": {ages}
  }}"""

  headers = {
      'Token': "gopaddi@v1",
      'Userid': "10"
      }

  conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/activity/activityList", payload, headers)

  res = conn.getresponse()
  data = res.read()
  data=json.loads(data.decode("utf-8"))
  activity_list=data['data'][0]['activityList']

  return activity_list