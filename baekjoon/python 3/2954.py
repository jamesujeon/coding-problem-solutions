# 문제 링크: https://www.acmicpc.net/problem/2954

s = input()
for v in "aeiou":
    s = s.replace(f"{v}p{v}", v)

print(s)
