# 문제 링크: https://www.acmicpc.net/problem/2822

l = [int(input()) for _ in range(8)]
s = sorted(l, reverse=True)[:5]

print(sum(s))
print(' '.join(str(i + 1) for i in range(8) if l[i] in s))