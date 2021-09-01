# 문제 링크: https://level.goorm.io/exam/49053/%EC%95%B5%EB%AC%B4%EC%83%88-%EA%BC%AC%EA%BC%AC/quiz/1

N = int(input())
sentences = [input() for _ in range(N)]


for s in sentences:
    s = ''.join(ch for ch in s if ch.lower() in 'aeiou')
    print(s if s else '???')