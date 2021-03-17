# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    return ' '.join(map(lambda x: x.capitalize(), s.split(' ')))