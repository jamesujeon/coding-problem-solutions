# 문제 링크: https://www.acmicpc.net/problem/2935

A, op, B = (input() for _ in range(3))

if A > B:
    A, B = B, A

result = ''
if op == '+':
    if A == B:
        result = '2' + '0' * (len(A) - 1)
    else:
        result = '1' + '0' * (len(B) - len(A) - 1) + A
else:
    result = '1' + '0' * (len(A + B) - 2)

print(result)
