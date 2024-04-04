from flask import Flask, request 
from searchactivities import searchactivities
from pprint import pprint
from ages import ageconverter

app= Flask(__name__)

@app.route('/')
def hello():
  return "This servers returns activity search results"

@app.route('/',methods=['POST'])
def webhook():
  req=request.get_json(force=True)
  pprint(req)
  sessionInfo=req['sessionInfo']
  parameters=sessionInfo['parameters']
  destination=parameters['activity_destination'] if parameters['activity_destination'] else parameters['activity_destination2']
  adults=parameters['adults']
  startDate=parameters['start-date']
  endDate=parameters['end-date']
  children=parameters['children']
  ages=parameters['ages']
  ages=ageconverter(ages)
  if (children!=0) and (ages==''):
    for i in range(int(children)):
      ages.append('7')
  total_people=int(adults)+int(children)
  # def searchactivities(city,startDate,endDate,adults,children,ages)
  # pprint(searchactivities(searchdestination("Delhi")[0],"2024-04-03","2024-04-05","2","1",[11]))
  activity_list=searchactivities(destination,startDate,endDate,adults,children,ages)
  activity_list=activity_list[:7]
  response={
          "fulfillmentResponse": {
              "messages": [
                  {
                      "text": {
                          "text": [
                              f"Click on any options below to book now!"] 
                      }
                  },
                  {
                    "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                    "channel": "",

                    #Union field message can be only one of the following:
                    "payload": {
                        
                          "botcopy": [
                                      {
                                        "carousel": [
                                          {
                                            "action": {
                                              "message": {
                                                "type": "training",
                                                "command": "Book now",
                                                "parameters": {
                                                      "activityCode": i["activityCode"],
                                                      "duration": i['duration'],
                                                      "activityName":i['activityName']
                                                    }
                                              }
                                            },
                                            "body": f"{i['description'][:150]}....",
                                            "image": {
                                              "alt": "Image of activity",
                                              "url": i['featureImage']
                                            },
                                            "subtitle": f"NGN {i['adultPrice']}",
                                            "title": i['activityName']
                                          } for i in activity_list
                                        ]
                                      }
                                    ]

                        
            }
                  }
              ]
          }
      }
  return response

if __name__ =="__main__":
  app.run(debug=True,port=8080)