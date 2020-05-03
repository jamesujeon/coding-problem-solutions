# 문제 링크: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        return list(map(lambda x: sortedNums.index(x), nums))
