# from searchresults.searchactivities import searchactivities
from fetchactdetails import fetchactdetails
# activity_list, searchId=searchactivities("Dubai,United Arab Emirates","2024/06/05","2024/06/07",2,0,[])
# print("yes the activity list is working" if activity_list else "act list not working")
# print("Search ID is", searchId)

# def fetchactdetails(searchId, actcode):
actdetails=fetchactdetails(112, "E-E10-A9SUNO0024")
print(actdetails)

