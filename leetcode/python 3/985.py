# 문제 링크: https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        a_sum = sum(a for a in A if a % 2 == 0)
        answer = []
        for val, index in queries:
            if A[index] % 2 == val % 2:
                if A[index] % 2 == 0:
                    # Case: Even + Even == Even
                    # Add the even value from the query.
                    a_sum += val
                else:
                    # Case: Odd + Odd == Even
                    # Add the sum of them.
                    a_sum += A[index] + val
            elif A[index] % 2 == 0:
                # Case: Even + Odd == Odd
                # Subtract the previous even value.
                a_sum -= A[index]
            answer.append(a_sum)
            A[index] += val
        return answer