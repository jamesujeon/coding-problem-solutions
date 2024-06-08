# 문제 링크: https://www.acmicpc.net/problem/9046

from collections import Counter

for _ in range(int(input())):
    c = Counter(input().replace(' ', '')).most_common()

    print(c[0][0] if len(c) == 1 or c[0][1] != c[1][1] else '?')
