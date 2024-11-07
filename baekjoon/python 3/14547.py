# 문제 링크: https://www.acmicpc.net/problem/14547

while (s := input()) != '#':
    s = s.split()[1]
    s = ' and '.join(f"{i} {i} glued" for i in range(10) if str(i) * 2 in s)
    if s:
        print(s)
