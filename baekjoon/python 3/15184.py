# 문제 링크: https://www.acmicpc.net/problem/15184

f = input().upper().count

for i in map(chr, range(65, 91)):
    print(f"{i} | {'*' * f(i)}")
