# 문제 링크: https://www.acmicpc.net/problem/12174

for t in range(1, int(input()) + 1):
    b, s = int(input()), input().replace('I', '1').replace('O', '0')
    s = ''.join(chr(int(s[i * 8:(i + 1) * 8], 2)) for i in range(b))

    print(f"Case #{t}: {s}")
