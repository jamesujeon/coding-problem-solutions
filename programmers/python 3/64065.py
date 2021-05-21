# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = sorted([set(sub.split(',')) for sub in s[2:-2].split('},{')], key=len)
    for i in reversed(range(len(s) - 1)):
        s[i + 1] -= s[i]
    return [int(list(sub)[0]) for sub in s]