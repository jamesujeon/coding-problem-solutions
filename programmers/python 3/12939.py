# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    l = list(map(int, s.split()))
    return f'{min(l)} {max(l)}'