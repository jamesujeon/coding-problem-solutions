# 문제 링크: https://www.acmicpc.net/problem/2083

import sys

for input in sys.stdin:
    name, age, weight = input.split()
    if name == '#':
        break

    print(f"{name} {'Senior' if int(age) > 17 or int(weight) >= 80 else 'Junior'}")
