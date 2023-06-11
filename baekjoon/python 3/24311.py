# 문제 링크: https://www.acmicpc.net/problem/24311

t1, t2 = map(int, input().split())
t3 = int(input())
t4, t5 = map(int, input().split())
br = int(input())
t6 = int(input())

t = t1 * 60 + t2 - (t3 + t4 * 60 + t5 + (br + 1) * t6 + 10)
print(f"{t // 60:02d} {t % 60:02d}")
