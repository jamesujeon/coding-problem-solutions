# 문제 링크: https://www.acmicpc.net/problem/4646

while (s := input()) != '0':
    n, *m = map(int, s.split())

    s, e = 0, sum(m)
    for i in range(n - 1):
        s += m[i]
        e -= m[i]
        if s == e:
            print(f'Sam stops at position {i + 1} and Ella stops at position {i + 2}.')
            break
    else:
        print('No equal partitioning.')
