# 문제 링크: https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline


def get_order(N, M, priorities):
    queue = deque((i, priorities[i]) for i in range(N))
    priorities.sort()

    count = 0
    while queue:
        document = queue.popleft()
        if document[1] != priorities[-1]:
            queue.append(document)
            continue

        count += 1
        priorities.pop()
        if document[0] == M:
            break

    return count


for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    print(get_order(N, M, priorities))