import requests  # handles API requests, requires package install.
import json  # Handles Json formatting in this code.

#keyword = input("Give city name: ")
#tempreq = f"https://api.openweathermap.org/data/2.5/weather?q={keyword},&callback=test&appid=22fc03c762c981f61627b4bcc36273aa"
tempreq = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid=22fc03c762c981f61627b4bcc36273aa"
answer = requests.get(tempreq).json()
#print(json.dumps(answer, indent=2))

# Lon Lat haku
try:
    answer = requests.get(tempreq)
    if answer.status_code==200:
        json_answer = answer.json()
        print(json_answer)
        for row in json_answer:
            print("lol")
            #latitude = row["lat"]
            #longitude = row["lon"]
except requests.exceptions.RequestException as e:
    print ("Invalid request.")