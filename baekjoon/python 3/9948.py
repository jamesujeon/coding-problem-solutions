# 문제 링크: https://www.acmicpc.net/problem/9948

import sys
input = sys.stdin.readline

n = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

while (s := input().strip()) != '0 #':
    d, m = s.split()
    d = (n.index(m[:3]) + 1) * 100 + int(d)

    if d == 229:
        print("Unlucky")
    elif d == 804:
        print("Happy birthday")
    else:
        print("Yes" if d < 804 else "No")
