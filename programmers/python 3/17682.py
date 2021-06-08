# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dart_result):
    dart_result = dart_result.replace('10', '$')
    scores = []
    for ch in dart_result:
        if ch in '0123456789$':
            scores.append(10 if ch == '$' else int(ch))
        elif ch in 'DT':
            scores[-1] **= 2 if ch == 'D' else 3
        elif ch == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif ch == '#':
            scores[-1] *= -1

    return sum(scores)