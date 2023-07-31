# 문제 링크: https://www.acmicpc.net/problem/24302

def f1(x):
    if x <= 5:    return 400
    elif x <= 10: return 700
    elif x <= 20: return 1200
    elif x <= 30: return 1700
    else:         return x * 57

def f2(x):
    if x <= 2:    return 90 + x * 90
    elif x <= 5:  return 100 + x * 85
    elif x <= 20: return 125 + x * 80
    elif x <= 40: return 325 + x * 70
    else:         return 925 + x * 55

a, b = map(lambda x: int(x) // 1000, input().split())

print(f"{(min(f1(a), f2(a)) + min(f1(b), f2(b))) / 100:.2f}")
