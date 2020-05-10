# 문제 링크: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        result = [-1]
        for i in range(len(arr) - 1):
            result.append(max(arr[i], result[i]))
        return result[::-1]
