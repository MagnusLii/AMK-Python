import requests  # handles API requests, requires package install.

key = "22fc03c762c981f61627b4bcc36273aa"
location = input("Gib city name: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"
answer = requests.get(request).json()

try:
    answer = requests.get(request)
    if answer.status_code == 200:
        json_answer = answer.json()
        print(f'''Temperature C: {json_answer["main"]["temp"]},'''
              f''' description: {json_answer["weather"][0]["description"]}''')
    elif not answer:
        print("Search returned no results.")

except requests.exceptions.RequestException as e:
    print("Hehe... broken")
