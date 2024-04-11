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
  activity_list, searchId=searchactivities(destination,startDate,endDate,adults,children,ages)
  activity_list=activity_list[:7]
  print(activity_list)
  if not activity_list:
    noactivity={
            "fulfillmentResponse": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Oops! We couldn't find any activities for {destination} between {startDate} and  {endDate}."] 
                        }
                    },
                    {
                      "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                      "channel": "",

                      #Union field message can be only one of the following:
                      "payload": {
                              "botcopy": [
                                {
                                  "suggestions": [
                                    {
                                      "action": {
                                        "message": {
                                          "command": "I want to change search details",
                                          "type": "training"
                                        }
                                      },
                                      "title": "Would you like to change search details?"
                                    }
                                  ]
                                }
                              ]
                            }

                    }
                ]
            }
        }
    return noactivity
  else:  
    response={
            "fulfillmentResponse": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Click on any options below to know more!"] 
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
                                                  "command": "Get more details",
                                                  "parameters": {
                                                        "searchId":searchId,
                                                        "activityCode": i["activityCode"],
                                                        "duration": i['duration'],
                                                        "activityName":i['activityName'],
                                                        "activityimg":i['featureImage'],
                                                        "activitydescription":i['description'],
                                                        'activityprice':i['adultPrice']
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
  app.run(debug=True,port=9056)