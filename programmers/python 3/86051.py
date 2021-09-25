# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return sum(set(range(10)) - set(numbers))