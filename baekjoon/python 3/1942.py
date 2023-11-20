# 문제 링크: https://www.acmicpc.net/problem/1942

for _ in range(3):
    t1, t2 = input().split()
    h1, m1, s1 = map(int, t1.split(':'))
    h2, m2, s2 = map(int, t2.split(':'))

    count = 0
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    while True:
        h, m, s = t1 // 3600, t1 // 60 % 60, t1 % 60
        if int(f'{h}{m}{s}') % 3 == 0:
            count += 1
        if t1 == t2:
            break
        t1 = (t1 + 1) % 86400

    print(count)
