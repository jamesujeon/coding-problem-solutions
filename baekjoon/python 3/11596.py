# 문제 링크: https://www.acmicpc.net/problem/11596

def f():
    return sorted(map(int, input().split()))

t1, t2 = f(), f()
print('YES' if t1 == t2 and t1[0]**2 + t1[1]**2 == t1[2]**2 else 'NO')
