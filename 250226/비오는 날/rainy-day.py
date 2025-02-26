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
    rainy_days = 0
    if weather == "Rain":
        rainy_days += 1
        dates.append(date)
        weather_datas.append(Weather_Data(date, day, weather))

for i in range (rainy_days):
    if weather_datas[i].date_ == sorted(dates)[0]:
        print(weather_datas[i].date_, weather_datas[i].day_, weather_datas[i].weather_)
