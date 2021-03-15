# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    result = ''
    while n > 0:
        result += str(n % 3)
        n //= 3

    return int(result, 3)