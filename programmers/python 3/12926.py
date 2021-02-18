# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ch = chr((ord(ch) - base + n) % 26 + base)
        answer += ch
    return answer