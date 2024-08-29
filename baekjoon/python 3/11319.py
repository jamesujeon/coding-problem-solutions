# 문제 링크: https://www.acmicpc.net/problem/11319

for _ in range(int(input())):
    s = input().replace(' ', '').lower()
    c = sum(i in 'aeiou' for i in s)
    print(len(s) - c, c)
