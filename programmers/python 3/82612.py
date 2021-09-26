# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    return max(sum(price * (i + 1) for i in range(count)) - money, 0)