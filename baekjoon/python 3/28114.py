# 문제 링크: https://www.acmicpc.net/problem/28114

pys = [input().split() for _ in range(3)]

print(''.join(sorted(y[-2:] for _, y, _ in pys)))
print(''.join(s[0] for _, _, s in sorted(pys, key=lambda x: -int(x[0]))))
