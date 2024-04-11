import http.client
from names import namedivider
conn = http.client.HTTPSConnection("vgtechdemo.com")
name="Anjaney Parasar"
fname, lname= namedivider(name)

payload = f"""{{
            "searchId":"3",
                "title": [
        "Mr"
    ],
    "fName": [
        "Sreehari"
    ],
    "lName": [
        "Shiji"
    ],
    "childtitle": [],
    "chfName": [],
    "childlast": [],
    "adultPrice": "16513.72",
    "adultNo": "1",
    "childPrice": "9908.2",
    "childNo": "0",
    "totalPrice": "16513.72",
    "email": "sreehari.novag@gmail.com",
    "contactNumber": "9876543210",
    "address": "Test Address",
    "checkIn": "2024-04-05",
    "hotel": "Test Hotel",
    "ActivityName": "Exotic Bird Show at Dubai Dolphinarium",
    "ActivityImage": "https://media.activitiesbank.com/49076/ENG/XL/Exotic%20Bird%20Show%201.jpg",
    "duration": "1 DAYS",
    "rateKey": "k4t3of07ne3nbniuvldogoi5cf",
    "currency":"NGN",
    "cancellationPolicy": "[]"
}}"""

headers = {
    'Token': "gopaddi@v1",
    'Userid': "10"
    }

conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/activity/activityBooking", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))