# 문제 링크: https://www.acmicpc.net/problem/17903

m, _ = map(int, input().split())
for _ in range(m): input()

print(f"{'un' if m < 8 else ''}satisfactory")
