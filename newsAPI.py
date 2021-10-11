# A simple Python Script to do something
# on mac: pip install newsapi-python
import requests
from newsapi import NewsApiClient


newsAPIKey = "341f0bbe436a47b28364f2d9c2ac10bb"
hotTopic = "volcano"

getString = "https://newsapi.org/v2/everything?q="+hotTopic+"&from=2021-10-11&sortBy=popularity&apiKey="+newsAPIKey
response = requests.get(getString)
if (response.status_code != 200):
    print("Something went wrong with our HTTP GET request. Status Code is: ")
    print(response.status_code)
else:
    responseJSON = response.json()
    print("\n")
    print(  "Number of articles found on the hot topic of \"" +hotTopic+"\" is: "+str(responseJSON["totalResults"]) )
    print("\n")
    print(  "First result headline is:  ")
    print( responseJSON["articles"][0]["title"] )
    print("\n")




