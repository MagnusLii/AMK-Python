import requests  # handles API requests, requires package install.
import json  # Handles Json formatting in this code.

keyword = input("Give a keyword for the query: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword
answer = requests.get(request).json()
#print(json.dumps(answer, indent=2))


try:
    answer = requests.get(request)
    if answer.status_code==200:
        json_answer = answer.json()
        print(json.dumps(json_answer, indent=2))
        for row in json_answer:
            print(row["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Invalid request.")
