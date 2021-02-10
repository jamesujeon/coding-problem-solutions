# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    return [sorted(array[cmd[0] - 1:cmd[1]])[cmd[2] - 1] for cmd in commands]