# 문제 링크: https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
cards = list(map(int, input().split()))


cards.sort(reverse=True)

def get_max_total():
    max_total = 0
    for i in range(N - 2):
        if cards[i] >= M:
            continue

        for j in range(i + 1, N - 1):
            if cards[i] + cards[j] >= M:
                continue

            for k in range(j + 1, N):
                total = cards[i] + cards[j] + cards[k]
                if total < M:
                    max_total = max(total, max_total)
                    break
                elif total == M:
                    return M

    return max_total


print(get_max_total())