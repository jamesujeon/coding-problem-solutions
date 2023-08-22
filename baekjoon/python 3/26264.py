# 문제 링크: https://www.acmicpc.net/problem/26264

N = int(input())
B = input().count("bigdata")
S = N - B

result = "bigdata?" if B >= S else "security!"
if B == S: result += " security!"

print(result)
