# 문제 링크: https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def convert(n: int) -> str:
            if n % 3 == 0 and n % 5 == 0:
                return 'FizzBuzz'
            if n % 3 == 0:
                return 'Fizz'
            if n % 5 == 0:
                return 'Buzz'
            return str(n)

        return map(convert, range(1, n + 1))