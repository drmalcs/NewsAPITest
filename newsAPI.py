# A simple Python3 Script to get my feet wet with a free REST API
# It returns the most recent news headlines on a topic of choice
# on mac: pip install newsapi-python     but only if you want to avoid using raw GET
#                pip install requests
#

import requests
from newsapi import NewsApiClient


newsAPIKey = "341f0bbe436a47b28364f2d9c2ac10bb"
hotTopic = "volcano"
hotTopic = input("Fetch most recent headlines: input subject:  ")
numHeadlinesToPrint = 5
numHeadlinesToPrint = int( input("Input number of headlines to show:  ") )
getString = "https://newsapi.org/v2/everything?q="+hotTopic+"&from=2021-10-11&sortBy=popularity&apiKey="+newsAPIKey
response = requests.get(getString)
if (response.status_code != 200):
    print("Something went wrong with our HTTP GET request. Status Code is: ")
    print(response.status_code)
else:
    responseJSON = response.json()
    articlesArray=responseJSON["articles"]
#    print( articlesArray[0])
    publishedAt = responseJSON["articles"][0]["publishedAt"]
    print("\n")
    print(  "Number of articles found on the hot topic of \"" +hotTopic+"\" is: "+str(responseJSON["totalResults"]) )
    print("Printing " +str(numHeadlinesToPrint) +" headlines\n")
    for article in range(numHeadlinesToPrint):
        print("Article " +str(article) +" published at: " +articlesArray[article]["publishedAt"] )
        print( "  Title: " +articlesArray[article]["title"] +"\n" )
