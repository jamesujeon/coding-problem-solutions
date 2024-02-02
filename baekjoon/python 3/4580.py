# 문제 링크: https://www.acmicpc.net/problem/4580

while (s := input()) != '0':
    k, *p = map(int, s.split())

    p = [0] + p
    print(' '.join(sum([[str(i)] * (p[i] - p[i - 1]) for i in range(1, k + 1)], [])))
