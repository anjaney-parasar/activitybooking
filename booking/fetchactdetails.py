import http.client
import json
from pprint import pprint
conn = http.client.HTTPSConnection("vgtechdemo.com")


def fetchactdetails(searchId, actcode):
    payload =f"""{{
        "searchId":"{searchId}",
        "activityCode":"{actcode}"}}"""

    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/activity/activityDetails", payload, headers)

    res = conn.getresponse()
    data = res.read()
    res=json.loads(data.decode("utf-8"))
    # pprint(res)
    result={}
    try:
        actPriceArr=res['data'][0]['activityPriceArray'][0]
        result['searchId']=searchId
        result['adultprice']=actPriceArr['adultPrice']
        result['cancellationPolicy']=actPriceArr['cancellationPolicy']
        result['childPrice']=actPriceArr['childPrice']
        result['rateKey']=actPriceArr['rateKey']
        result['totalPrice']=actPriceArr['totalPrice']
        result['duration']=actPriceArr['duration']
        result['actName']=res['data'][0]['ActivityName']
        result['actImage']=res['data'][0]['featuredImage']
        return result
    except IndexError:
        return "Activity details not found."

