# 문제 링크: https://www.acmicpc.net/problem/2028

for _ in range(int(input())):
    N = input()

    print("YES" if str(int(N)**2).endswith(N) else "NO")
