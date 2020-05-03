# 문제 링크: https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        dlist = []
        for i in range(0, len(nums), 2):
            dlist += [nums[i + 1]] * nums[i]
        return dlist
