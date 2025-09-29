import sys
input = sys.stdin.readline

string_arr = ['L', 'E', 'B', 'R', 'O', 'S']

ch = input().strip()
if ch in string_arr:
    idx = string_arr.index(ch)
    print(idx)
else:
    print("None")