# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    for i, citation in enumerate(sorted(citations, reverse=True)):
        if i >= citation:
            return i
    return len(citations)