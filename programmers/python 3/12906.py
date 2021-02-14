# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for n in arr:
        if not answer or n != answer[-1]:
            answer.append(n)
    return answer