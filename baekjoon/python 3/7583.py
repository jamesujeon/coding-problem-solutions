# 문제 링크: https://www.acmicpc.net/problem/7583

while (s := input()) != '#':
    print(' '.join(w[0] + w[-2:0:-1] + w[-1] if len(w) > 3 else w for w in s.split()))
