# 문제 링크: https://www.acmicpc.net/problem/10816

from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))


card_nums = list(sorted(set(cards)))
cards = Counter(cards)

def count(num):
    low, high = 0, len(card_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if card_nums[mid] < num:
            low = mid + 1
        elif card_nums[mid] > num:
            high = mid - 1
        else:
            return cards[num]

    return 0


print(' '.join(str(count(num)) for num in nums))