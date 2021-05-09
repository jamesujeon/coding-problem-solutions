# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return x % sum(map(int, str(x))) == 0