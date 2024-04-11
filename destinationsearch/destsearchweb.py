from flask import Flask, request
from destinationsearch.searchdestination import searchdestination

app=Flask(__name__)

@app.route('/')
def hello():
  return "Webhook for making activity destination search"


@app.route('/',methods=['POST'])
def webhook():
  req=request.get_json(force=True)
  sessionInfo=req['sessionInfo']
  activity_destination=sessionInfo['parameters']['activity_destination']
  session_name = req.get('sessionInfo').get('session')
  destination_list=searchdestination(activity_destination)

  if not destination_list:
    no_destination={
        "fulfillment_response":
            {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Sorry, we couldn't find any destinations in {activity_destination}, Please try another city."
                            ]
                        }
                    }
                ]
            },
        "session_info": {
            "session": session_name,
            "parameters": {
                "activity_destination": None
            }
        },
        "target_page": req.get('pageInfo').get("currentPage")  # Maintain current page
    }

    return no_destination
  
  elif len(destination_list)>1:
    manydestination={
        "fulfillment_response":
            {
            "messages": [
                {
                    "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                    "channel": "",

                    #Union field message can be only one of the following:
                    "text": {
                        "text": [
                            f'We found multiple destinations with the name {activity_destination} in it.'
                            ],
                                "allowPlaybackInterruption": False
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
                                "command": i,
                                "type": "training"
                              }
                            },
                            "title": i
                          }for i in destination_list
                        ]
                      }
                    ]
                  }
                }
            ],
            "mergeBehavior": "REPLACE"
            },
            
        "session_info": {
            "session": session_name,
            "parameters": {
                "activity_destination": None
            }
        },
        #            projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/a2735fbd-0179-49a4-99e8-30577c9ccf93/pages/c1fb8a04-c84b-42a6-9403-d3e68debacb2
     "target_page": "projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/38ab63df-27e4-4e6c-87f9-d46f1c14d337/pages/b31cf974-f204-421d-afce-19e902af18a7 "
    
    }

    return manydestination
  
  else:
    perfect={
      
        "session_info": {
            "session": session_name,
            "parameters": {
                "activity_destination": destination_list[0]
            }
        },
            "target_page": "projects/travel-chatbot-409605/locations/us-central1/agents/ad7caede-bce6-4562-ae2f-8dacfb73bddf/flows/38ab63df-27e4-4e6c-87f9-d46f1c14d337/pages/3d45df9e-f73d-4fd8-a10d-2fbed8495162"
    }

    return perfect

if __name__=="__main__":
  app.run(debug=True, port=3000)


 
  
