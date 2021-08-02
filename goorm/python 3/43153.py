# 문제 링크: https://level.goorm.io/exam/43153/%EB%B3%B5%EC%86%8C%EC%88%98%EC%9D%98-%EA%B3%B1%EC%85%88/quiz/1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = A[0] * B[0] - A[1] * B[1]
b = A[0] * B[1] + A[1] * B[0]
result = str(a) + (f" {'+' if b > 0 else '-'} {abs(b)}i" if b else '')

print(result)