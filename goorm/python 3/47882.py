# 문제 링크: https://level.goorm.io/exam/47882/헷갈리는-작대기/quiz/1

S = input()


counts = {'1': 0, 'I': 0, 'l': 0, '|': 0}
for ch in S:
    if ch in counts:
        counts[ch] += 1


for ch in '1Il|':
    print(counts[ch])