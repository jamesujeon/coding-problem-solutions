# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)

    count = 0
    while len(scoville) > 1 and scoville[0] < K:
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        count += 1

    return count if scoville[0] >= K else -1