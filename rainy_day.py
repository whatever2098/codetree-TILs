'''n개의 날씨 데이터가 주어짐 date, day, wheather
   "Rain"으로 표시된 비 오는 날 중에서
   가장 가까운(빠른) 날짜를 출력해야 함.'''

'''먼저 Rain인 날만 필터링 
   그 후, 그 필터링된 리스트에서 가장 빠른 날짜로 정렬(또는 min으로 선택)'''

'''날짜 정렬은 Rain 날 들에 대해서만 수행'''

n = int(input())
#date, day, wheather

wheather_datas = []

for _ in range(n):
    date, day, wheather = tuple(input().split())
    wheather_datas.append((date, day, wheather))

'''가장 가까운 Rainy 날 찾기
Rainy 날만 따로 모음'''
rainy_days = [d for d in wheather_datas if d[2] == "Rain"]

#날짜 기준으로 가장 빠른 날 찾기
nearest = min(rainy_days, key=lambda d: d[0])
print(nearest[0], nearest[1], nearest[2]) 