# 문제 링크: https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        result, carry = '', 0
        for d1, d2 in zip(num1, num2):
            carry, remainder = divmod(int(d1) + int(d2) + carry, 10)
            result += str(remainder)

        for d in num2[len(num1):]:
            carry, remainder = divmod(int(d) + carry, 10)
            result += str(remainder)

        if carry > 0:
            result += str(carry)

        return result[::-1]