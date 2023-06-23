# 문제 링크: https://www.acmicpc.net/problem/24803

G, S, C = map(int, input().split())
power = G * 3 + S * 2 + C

result = ""
if power > 7:
    result = "Province"
elif power > 4:
    result = "Duchy"
elif power > 1:
    result = "Estate"

if result:
    result += " or "

if power > 5:
    result += "Gold"
elif power > 2:
    result += "Silver"
else:
    result += "Copper"

print(result)
