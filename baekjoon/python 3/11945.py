# 문제 링크: https://www.acmicpc.net/problem/11945

N, _ = map(int, input().split())
shapes = [input() for _ in range(N)]

for shape in shapes:
    print(shape[::-1])
