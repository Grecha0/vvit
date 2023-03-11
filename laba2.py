import requests
s_city = "Moscow,RU"
appid = "0f998ad3d8871b6d924aa6058a0cff4f"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
      params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'],'м/с', "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")