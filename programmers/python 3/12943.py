# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    for count in range(500):
        if num == 1:
            return count
        num = num * 3 + 1 if num % 2 else num // 2
    return -1