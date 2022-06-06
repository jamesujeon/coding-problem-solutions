# 문제 링크: https://www.acmicpc.net/problem/16199

sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

print(ey - sy - int(sm > em or (sm == em and sd > ed)))
print(ey - sy + 1)
print(ey - sy)
