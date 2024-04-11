from flask import Flask, request 
from  pprint import pprint
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
  adults=int(parameters['adults'])
  fullnames=[]
  for i in range(adults):
    fullnames.append(parameters[f"fullname_{i+1}"])
  children=int(parameters['children'])
  child_fullnames=[]
  for i in range(children):
    child_fullnames.append(parameters[f"child_fullname_{i+1}"])
  email=parameters['email']
  duration=parameters['duration']

  print("Search Id is:", searchId)
  print("activityCode ",activityCode)

  print("Number of adults",adults)
  print("Number of children", children)
  print("Email ", email)
  print("Duration ",duration)
  print("List of fullnames", fullnames)
  print("list of children",child_fullnames)
  print("\n")
  print(fetchactdetails(searchId,activityCode))




  return ""

if __name__=="__main__":
  app.run(debug=True, port=5600)
