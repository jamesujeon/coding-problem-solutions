# 문제 링크: https://www.acmicpc.net/problem/2511

scores = [0, 0]
winner = 'D'
for cards in zip(map(int, input().split()), map(int, input().split())):
    if cards[0] > cards[1]:
        scores[0] += 3
        winner = 'A'
    elif cards[0] < cards[1]:
        scores[1] += 3
        winner = 'B'
    else:
        scores[0] += 1
        scores[1] += 1

if scores[0] > scores[1]:
    winner = 'A'
elif scores[0] < scores[1]:
    winner = 'B'

print(scores[0], scores[1])
print(winner)
