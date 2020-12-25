# 문제 링크: https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candy, ans = 0, [0] * num_people
        while candies > 0:
            for i in range(num_people):
                candy = min(candies, candy + 1)
                ans[i] += candy
                candies -= candy
                if candies == 0:
                    break
        return ans