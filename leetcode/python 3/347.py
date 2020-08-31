# 문제 링크: https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [n for n, _ in nums[:k]]