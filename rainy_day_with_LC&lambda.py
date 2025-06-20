n = int(input())

wheather_datas = []

#tuple로 data 저장
for _ in range(n):
  date, day, wheather = input().split()
  wheather_datas.append((date, day, wheather))
  #tuple은  숫자로 인덱싱한다.  ex)data[0] == 날짜, data[1] == 요일, data[2] == 날씨

#Rainy한 날만 모아서 날짜 순으로 정렬
rainy_days = [data for data in wheather_datas if data[2] == "Rain"]

if rainy_days:
  rainy_days.sort(key = lambda d: d[0])
  nearest = rainy_days[0]
  print(nearest[0], nearest[1], nearest[2])
else:
  print("Rainy day not found")


nearest = min(rainy_days, key = lambda d: d[0])