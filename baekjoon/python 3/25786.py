# 문제 링크: https://www.acmicpc.net/problem/25786

a, b = input(), input()

a, b = a.zfill(len(b)), b.zfill(len(a))
print(''.join('0' if (a <= '2' and b <= '2') or (a >= '7' and b >= '7') else '9' for a, b in zip(a, b)))
