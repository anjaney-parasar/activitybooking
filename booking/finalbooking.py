from flask import Flask, request 
from  pprint import pprint
from names  import namedivider
from bookingAPI import bookactivity
import  json
from fetchactdetails import fetchactdetails
app=Flask(__name__)

@app.route('/')
def function():
  return "This webhook returns booking"

@app.route('/',methods=['POST'])
def webhook():
  req=request.get_json(force=True)
  parameters=req['sessionInfo']['parameters']
  activityCode=parameters['activityCode']
  searchId=int(parameters['searchId'])
  adult=int(parameters['adults'])
  fullnames=[]
  for i in range(adult):
    # parameters[f"fullname_{i+1}"]=parameters[f"fullname_{i+1}"]+" "
    fullnames.append(parameters[f"fullname_{i+1}"])
  print(fullnames)
  children=int(parameters['children'])
  child_fullnames=[]
  for i in range(children):
    # parameters[f"child_fullname_{i+1}"]=parameters[f"child_fullname_{i+1}"]+" "
    child_fullnames.append(parameters[f"child_fullname_{i+1}"])
  print(child_fullnames)
  email=parameters['email']
  duration=parameters['duration']
  fnames=[]
  lnames=[]
  for i in fullnames:
    fname, lname= namedivider(i)
    fnames.append(fname)
    lnames.append(lname)
  chfname=[]
  chlname=[]
  for i in child_fullnames:
    fname, lname=namedivider(i)
    chfname.append(fname)
    chlname.append(lname)


  # print("Search Id is:", searchId)
  # print("activityCode ",activityCode)

  # print("Number of adults",adult)
  # print("Number of children", children)
  # print("Email ", email)
  # print("Duration ",duration)
  # print("List of fullnames", fullnames)
  # print("list of children",child_fullnames)
  # print("\n")
  actdetails=fetchactdetails(searchId,activityCode)
  if actdetails!="Activity details not found.":
    adultPrice=actdetails['adultprice']
    childPrice=actdetails['childPrice']
    actname=actdetails['actName']
    actimg=actdetails['actImage']
    ratekey=actdetails['rateKey']
    cancellation=actdetails['cancellationPolicy']
  else:
    nofetch={
                "fulfillment_response":
                    {
                        "messages": [
                            {
                                "text": {
                                    "text": [
                                        f"Sorry, we are unable to fetch activity details right now, Please try again next time."
                                    ]
                                }
                            }
                        ]
                    }
            }

    return nofetch
  # bookresult=bookactivity(searchId, fname,lname,chfname,chlname,adultPrice, adult,childPrice,children,email,actname,actimg,duration, ratekey,cancellation)
                          # (searchId,fname:list,lname:list,chfname:list,chlname:list,adultPrice, adult,childPrice,children,email,actname,actimg,duration,ratekey,cancellation:list):
  bookresult=bookactivity(searchId, fname,lname,chfname,chlname,adultPrice, adult,childPrice,children,email,actname,actimg,duration, ratekey,cancellation)
  bookingstatus=bookresult['data'][0]['bookingStatus']
  response={
        "fulfillment_response":
            {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Booking status is:{bookingstatus}"
                            ]
                        }
                    }
                ]
            }
    }

  return response

if __name__=="__main__":
  app.run(debug=True, port=5600)
