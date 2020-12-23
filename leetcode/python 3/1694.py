# 문제 링크: https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        numbers = []
        number = number.replace(' ', '').replace('-', '')
        while True:
            # greater than or equal to 4 digits
            if len(number) > 3:
                # i == 2 or i == 3
                i = min(len(number) - 2, 3)
                numbers.append(number[:i])
                number = number[i:]
            # 2 or 3 digits
            elif len(number) > 1:
                numbers.append(number)
                break
        return '-'.join(numbers)