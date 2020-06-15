# 문제 링크: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            prices[i] -= next((p for p in prices[i + 1:] if p <= prices[i]), 0)
        return prices