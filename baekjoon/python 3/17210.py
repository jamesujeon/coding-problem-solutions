# 문제 링크: https://www.acmicpc.net/problem/17210

N, M = int(input()), int(input())

if N < 6:
    for m in ("01010" if M == 0 else "10101")[1:N]:
        print(m)
else:
    print("Love is open door")
