# 문제 링크: https://www.acmicpc.net/problem/19963

def i():
    return map(int, input().split())

n, _, _ = i()
n = set(range(1, n + 1)) - set(i()) - set(i())

print(len(n))
print(' '.join(map(str, n)))
