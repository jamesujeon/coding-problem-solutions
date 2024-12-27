# 문제 링크: https://www.acmicpc.net/problem/15449

s = sorted(map(int, input().split()))
print(sum(s[i] + s[j] > s[k] for i in range(3) for j in range(i + 1, 4) for k in range(j + 1, 5)))
