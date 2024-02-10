# 문제 링크: https://www.acmicpc.net/problem/4807

i = 1
while (N := int(input())) != 0:
    a = list(map(int, input().split()))

    count = 0
    while count < 1000 and len(set(a)) > 1:
        a = [abs(a[k] - a[(k + 1) % N]) for k in range(N)]
        count += 1

    if count < 1000:
        print(f'Case {i}: {count} iterations')
    else:
        print(f'Case {i}: not attained')
    i += 1
