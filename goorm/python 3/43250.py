# 문제 링크: https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in sorted(a + b):
    print(i, end=' ')