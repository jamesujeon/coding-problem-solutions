# 문제 링크: https://www.acmicpc.net/problem/25801

from collections import Counter

counts = Counter(input()).values()
if all(i % 2 == 0 for i in counts):
    print(0)
elif all(i % 2 == 1 for i in counts):
    print(1)
else:
    print("0/1")
