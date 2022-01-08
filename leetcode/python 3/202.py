# 문제 링크: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        histories = {n}
        while n != 1:
            n = int(sum(int(d)**2 for d in str(n)))
            if n in histories:
                return False

            histories.add(n)

        return True