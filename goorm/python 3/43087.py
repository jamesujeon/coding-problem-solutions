# 문제 링크: https://level.goorm.io/exam/43087/%EC%84%B8%EB%A1%9C-%EC%9D%BD%EA%B8%B0/quiz/1

n = int(input())
letters = [list(input().split()) for _ in range(n)]

print(''.join(letters[i][-j] for j in range(1, n + 1) for i in range(n)))