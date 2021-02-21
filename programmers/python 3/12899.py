# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer += '124'[n % 3]
        n //= 3
    return answer[::-1]