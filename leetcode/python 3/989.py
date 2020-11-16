# 문제 링크: https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i, carry = len(A) - 1, 0
        while i >= 0 or K > 0:
            carry += (A[i] if i >= 0 else 0) + (K % 10 if K > 0 else 0)
            if i >= 0:
                A[i] = carry % 10
            else:
                A.insert(0, carry % 10)
            carry //= 10

            if i >= 0:
                i -= 1
            if K > 0:
                K //= 10

        if carry:
            A.insert(0, carry)

        return A