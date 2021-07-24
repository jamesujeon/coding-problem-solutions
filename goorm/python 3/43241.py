# 문제 링크: https://level.goorm.io/exam/43241/%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

a, op, b = input().split(' ')

a, b = int(a), int(b)
result = 0
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b

print('{:.2f}'.format(result) if op == '/' else result)