from flask import Flask, request 
from pprint import pprint

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
  total_people=int(adults)+int(children)

  response={
          "fulfillmentResponse": {
              "messages": [
                  {
                      "text": {
                          "text": [
                              f"Shall I search for activities in {destination} for {total_people} people between {startDate} and {endDate}? Please confirm."] 
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
                                      "type": "training",
                                      "command": ""
                                    }
                                  },
                                  "title": "Yes"
                                },
                                {
                                  "title": "No, I would like to edit details",
                                  "action": {
                                    "message": {
                                      "type": "training",
                                      "command": ""
                                    }
                                  }
                                }
                                
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