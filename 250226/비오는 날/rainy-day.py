n = int(input())
dates = []
days = []
weathers = []

class Weather_Data:
    def __init__(self, date, day, weather):
        self.date_ = date
        self.day_ = day
        self.weather_ = weather

weather_datas = []
for i in range (n):
    date, day, weather = tuple(input().split())
    if weather == "Rain":
        dates.append(date)
        weather_datas.append(Weather_Data(date, day, weather))

for i in range (len(weather_datas)):
    if weather_datas[i].date_ == sorted(dates)[0]:
        print(weather_datas[i].date_, weather_datas[i].day_, weather_datas[i].weather_)
