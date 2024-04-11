from flask import Flask, request 
from pprint import pprint

app= Flask(__name__)

@app.route('/')
def hello():
  return "This servers returns activity search results"


item_list=["orange", "mango", "apple", "grapes","banana"]
@app.route('/',methods=['POST'])
def webhook():
  response={
          "fulfillmentResponse": {
              "messages": [
                  {
                      "text": {
                          "text": [
                              f"I am looping over a list to get these carousels!"] 
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
                                              "link": {
                                                "target": "_blank",
                                                "url": "https://botcopy.com"
                                              }
                                            },
                                            "body": "Description One",
                                            "image": {
                                              "alt": "Image of a cat",
                                              "url": "https://homepages.cae.wisc.edu/~ece533/images/cat.png"
                                            },
                                            "subtitle": "Subtitle One",
                                            "title": i
                                          } for i in item_list
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
  app.run(debug=True,port=8090)