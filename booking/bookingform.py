from flask import Flask, request 
from pprint import pprint


app= Flask(__name__)

@app.route('/')
def hello():
  return "This servers returns activity booking form"

@app.route('/',methods=['POST'])
def webhook():
  req=request.get_json(force=True)
  pprint(req)
  sessionInfo=req['sessionInfo']
  parameters=sessionInfo['parameters']
  destination=parameters['activity_destination'] if parameters['activity_destination'] else parameters['activity_destination2']
  adults=int(parameters['adults'])
  startDate=parameters['start-date']
  endDate=parameters['end-date']
  children=int(parameters['children'])
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
                              "form": {
                                "force": True,
                                "subtitle": "",
                                "fields": [
                                  {
                                    "error": "This field is required.",
                                    "helperText": "",
                                    "expose": True,
                                    "required": True,
                                    "parameter": "fullname_1",
                                    "placeholder": "Person 1",
                                    "type": "text",
                                    "label": "Full Name"
                                  }                                  
                                ] ,
                                "action": {
                                  "message": {
                                    "type": "training",
                                    "command": "Submit"
                                  }
                                },
                                "title": "Activity Booking",
                                "style": "message"
                              }
                            }
                          ]
                    }



                  }
              ]
          }
      }
  fields=response["fulfillmentResponse"]["messages"][0]["payload"]["botcopy"][0]['form']["fields"]

  for i in range(1,adults):
    fields.append({
      "error": "This field is required.",
      "helperText": "",
      "expose": True,
      "required": True,
      "parameter": f"fullname_{i+1}",  # Create unique parameter name
      "placeholder": f"Person {i+1}",
      "type": "text",  # Change type to TEXT for full name
      "label": f"Full Name {i+1}"
    })
  
  if (children>0):
    for i in range(0,children):
      fields.append({
        "error":"This field is required.",
        "helperText":"",
        "expose":True,
        "required":True,
        "parameter":f"child_fullname_{i+1}",
        "placeholder": f"Child {i+1}",
        "type":"text",
        "label":f"Child Full Name {i+1}"
      })

  fields.extend([{
        "error":"This field is required.",
        "helperText":"",
        "expose":True,
        "required":True,
        "parameter":"email",
        "placeholder": "johndoe@gmail.com",
        "type":"email",
        "label":"Email"
      }])

  return response

if __name__ =="__main__":
  app.run(debug=True,port=8056)