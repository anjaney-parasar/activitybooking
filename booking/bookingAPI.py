import http.client
import json

conn = http.client.HTTPSConnection("vgtechdemo.com")

ratekey="r2h5n390td60c7ie08korli5nq"
searchId="103"
fname= ["John"]
lname=["Doe"]
chfname=[]
chlname=[]
duration="1 DAYS"
adultPrice=14457.14
cancellation=[{'amount': 14457.14, 'dateFrom': '2024-10-04T00:00:00.000Z'}]
adult=1
childPrice=14457.14
children=0
totalPrice=14457.14
email="johndoe@gmail.com"
actname="Exotic Bird Show at Dubai Dolphinarium"
actimg="https://media.activitiesbank.com/49076/ENG/XL/Exotic%20Bird%20Show%201.jpg"

def bookactivity(searchId,fname:list,lname:list,chfname:list,chlname:list,adultPrice, adult,childPrice,children,email,actname,actimg,duration,ratekey,cancellation:list):
    payload = f"""{{
        "searchId": "{searchId}",
        "title": [],
        "fName": "{fname}",
        "lName": "{lname}",
        "childtitle": [],
        "chfName": "{chfname}",
        "childlast": "{chlname}",
        "adultPrice": "{adultPrice}",
        "adultNo": "{adult}",
        "childPrice": "{childPrice}",
        "childNo": "{children}",
        "totalPrice": "{adultPrice}",
        "email": "{email}",
        "contactNumber": "983210",
        "address": "Test Address",
        "checkIn": "2024-03-05",
        "hotel": "Test Hotel",
        "ActivityName": "{actname}",
        "ActivityImage": "{actimg}",
        "duration": "{duration}",
        "rateKey": "{ratekey}",
        "currency":"NGN",
        "cancellationPolicy": "{cancellation}"
    }}"""

    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/activity/activityBooking", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data=json.loads(data.decode("utf-8"))
    return data


bookresult=bookactivity(searchId, fname,lname,chfname,chlname,adultPrice, adult,childPrice,children,email,actname,actimg,duration, ratekey,cancellation)
print(bookresult['data'][0]['bookingStatus'])