# 문제 링크: https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for i in range(1, n + 1):
            key = sum(int(c) for c in str(i))
            groups[key] = groups.get(key, 0) + 1

        largest_size = max(groups.values())
        return sum(size == largest_size for size in groups.values())