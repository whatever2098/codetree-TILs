import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(float, input().split()))
total = 0.0;

for i in range(n):
    total += arr[i]

avg = round(total / n, 1)

print(avg)

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
elif(avg < 3.0):
    print("Poor")

#print("Perfect" if avg >= 4.0 else "Good" if avg >= 3.0 else "Poor")
#avg round(total/n, 1) 1번째 까지 반올림

# print(f"{avg:.1f}")  # 소수 1자리까지 반올림하여 출력

