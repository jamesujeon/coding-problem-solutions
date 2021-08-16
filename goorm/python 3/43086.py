# 문제 링크: https://level.goorm.io/exam/43086/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EB%B9%88%EB%8F%84-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

s = input().replace(' ', '').lower()


counts = [0] * 26
for alpha in s:
    counts[ord(alpha) - 97] += 1


for i, count in enumerate(counts):
    print(f'{chr(i + 97)} : {count}')
