# 문제 링크: https://level.goorm.io/exam/43113/substring/quiz/1

s = input()
i, count = map(int, input().split())


print(s[i - 1:i + count - 1])
