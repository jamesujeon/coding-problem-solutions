# 문제 링크: https://www.acmicpc.net/problem/18198

record = input()

scores = {'A': 0, 'B': 0}
for i in range(0, len(record), 2):
    scores[record[i]] += int(record[i + 1])

print('AB'[scores['A'] < scores['B']])
