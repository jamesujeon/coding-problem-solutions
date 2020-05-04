# 문제 링크: https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_cities = list(map(lambda x: x[0], paths))
        for _, dest_city in paths:
            if dest_city not in src_cities:
                return dest_city
        return None
