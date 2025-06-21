#LCM(a1, a2, ..., an) = LCM(a1, LCM(a2, LCM(a3, ..., an)))
'''get_lcm_recursive(arr, 2)
→ lcm(get_lcm_recursive(arr, 1), 30)
→ lcm(lcm(get_lcm_recursive(arr, 0), 18), 30)
→ lcm(lcm(12, 18), 30)
→ lcm(36, 30) = 180
'''
'''
get_lcm_recursive(arr, 2)
│
├── lcm(
│     └── get_lcm_recursive(arr, 1)
│         │
│         ├── lcm(
│         │     └── get_lcm_recursive(arr, 0)
│         │         └── return 12
│         │
│         └── arr[1] = 18
│     )
│     → lcm(12, 18) = 36
│
└── arr[2] = 30
→ lcm(36, 30) = 180'''


def gcd(a, b):
    # 유클리드 호제법
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def get_lcm_recursive(arr, index):
    if index == 0:
        return arr[0]
    return lcm(get_lcm_recursive(arr, index - 1), arr[index])

# 예시 사용
arr = [12, 18, 30]
result = get_lcm_recursive(arr, len(arr) - 1)
print("LCM:", result)
