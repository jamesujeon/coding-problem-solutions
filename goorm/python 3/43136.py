# 문제 링크: https://level.goorm.io/exam/43136/%EC%82%BC%EA%B0%81%ED%98%95-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

n = int(input())

count = 0
for a in range(1, n):
    for b in range(a, n):
        c = n - a - b
        if c < b:
            break
        if c < a + b:
            count += 1

print(count)