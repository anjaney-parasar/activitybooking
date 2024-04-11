from flask import Flask, request 
from pprint import pprint

app= Flask(__name__)

@app.route('/')
def hello():
  return "This servers returns details for a particular activity."

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
  total_people=int(adults)+int(children)
  activityName=parameters['activityName']
  duration=parameters['duration']
  activityimg=parameters['activityimg']
  acvtivitydescription=parameters['activitydescription']
  activityprice=parameters['activityprice']
  
  response={
          "fulfillmentResponse": {
              "messages": [
                  {
                    "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                    "channel": "",

                    #Union field message can be only one of the following:
                    "payload": {
                              "botcopy": [
                                {
                                  "card": {
                                    "action": {
                                      "buttons": [
                                        {
                                          "action": {
                                            "message": {
                                              "command": "Book Now",
                                              "type": "training"
                                            }
                                          },
                                          "title": "Book Now"
                                        }
                                      ]
                                    },
                                    "body": acvtivitydescription[:400],
                                    "image": {
                                      "alt": "Image of a cat",
                                      "url": activityimg
                                    },
                                    "subtitle": f'''💷Price: NGN {activityprice}
🗓️Duration: {duration}''',
                                    "title": activityName
                                  }
                                }
                              ]
                          }
                  }
              ]
          }
      }
  return response

if __name__ =="__main__":
  app.run(debug=True,port=8056)