# import requests
from pprint import pprint
from searchdestination import searchdestination
from searchactivities import searchactivities
# url = "https://vgtechdemo.com/gopaddiberlin/gopaddiberlinbkend/web/activity/destinations"
from ages import ageconverter
print(ageconverter("4,12"))
# payload = "{\r\n    \"search\": \"York\"\r\n}"
# headers = {
#     "Token": "gopaddi@v1",
#     "Userid": "10"
# }

# def searchactivities(city,startDate,endDate,adults,children,ages)
# pprint(searchactivities(searchdestination("Delhi")[0],"2024-04-03","2024-04-05","2","1",[11]))
# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)