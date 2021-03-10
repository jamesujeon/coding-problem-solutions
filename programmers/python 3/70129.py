# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    counts = [0, 0]
    while s != '1':
        zeros = s.count('0')
        s = bin(len(s) - zeros)[2:]
        counts[0] += 1
        counts[1] += zeros
    return counts