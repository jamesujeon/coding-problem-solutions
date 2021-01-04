# 문제 링크: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(K):
            if A[i] >= 0:
                break
            A[i] = -A[i]
            K -= 1

        if K % 2 == 1:
            A.sort()
            A[0] = -A[0]

        return sum(A)