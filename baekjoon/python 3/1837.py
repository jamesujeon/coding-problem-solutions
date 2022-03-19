# 문제 링크: https://www.acmicpc.net/problem/1837

P, K = map(int, input().split())

def validate() -> str:
    if K > 2 and P % 2 == 0:
        return 'BAD 2'

    for i in range(3, K, 2):
        if P % i == 0:
            return f'BAD {i}'

    return 'GOOD'

print(validate())
