# 문제 링크: https://www.acmicpc.net/problem/9636

for _ in range(int(input())):
    s = input()
    x, y, m = s.count('R') - s.count('L'), s.count('U') - s.count('D'), s.count('?')

    print(x - m, y - m, x + m, y + m)
