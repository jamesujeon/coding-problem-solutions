# 문제 링크: https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    count += 1
        return count