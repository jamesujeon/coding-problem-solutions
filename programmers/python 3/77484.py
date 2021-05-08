# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    min_wins = len(set(win_nums).intersection(set(lottos)))
    max_wins = lottos.count(0) + min_wins
    return [min(7 - max_wins, 6), min(7 - min_wins, 6)]