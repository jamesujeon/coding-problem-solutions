# 문제 링크: https://www.acmicpc.net/problem/5087

while (s := input()) != '#':
    scores = [0, 0]
    for c in s.split()[:-1]:
        scores[0 if c in 'A3579' else 1] += 1

    if scores[0] > scores[1]:
        print('Cheryl')
    elif scores[0] < scores[1]:
        print('Tania')
    else:
        print('Draw')
