# 문제 링크: https://level.goorm.io/exam/43110/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B2%88%EA%B0%88%EC%95%84-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1

s = input()

result = ''
for i in range(len(s) // 2):
    result += s[i] + s[-(i + 1)]
if len(s) % 2:
    result += s[len(s) // 2]

print(result)