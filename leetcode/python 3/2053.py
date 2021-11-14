# 문제 링크: https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distincts = [s for s in arr if counts[s] == 1]

        return distincts[k - 1] if k <= len(distincts) else ''