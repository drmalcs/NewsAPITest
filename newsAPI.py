# A simple Python Script to do something
# on mac: pip install newsapi-python
import requests
from newsapi import NewsApiClient
newsAPIKey = "341f0bbe436a47b28364f2d9c2ac10bb"
getString = "https://newsapi.org/v2/everything?q=volcano&from=2021-10-11&sortBy=popularity&apiKey="+newsAPIKey
response = requests.get(getString)
print(response.status_code)
responseJSON = response.json()
print(  responseJSON["totalResults"] )

##print("The Articles:\n\n " +response.articles)

