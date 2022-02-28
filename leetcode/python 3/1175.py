# 문제 링크: https://leetcode.com/problems/prime-arrangements/

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = self.get_prime_count(n)
        return (self.get_factorial(prime_count) * self.get_factorial(n - prime_count)) % (10**9 + 7)

    def get_prime_count(self, n: int) -> int:
        count = 0
        primes = [True] * (n + 1)
        for i in range(2, n + 1):
            if primes[i]:
                count += 1
                for j in range(i**2, n + 1, i):
                    primes[j] = False

        return count

    def get_factorial(self, n: int) -> int:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i

        return factorial
