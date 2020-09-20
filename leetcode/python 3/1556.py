# 문제 링크: https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        nums = []
        while True:
            nums.append(str(n % 1000).zfill(3))
            n //= 1000
            if not n:
                break
        nums[-1] = str(int(nums[-1]))
        return '.'.join(reversed(nums))