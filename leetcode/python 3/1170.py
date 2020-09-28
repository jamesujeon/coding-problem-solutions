# 문제 링크: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            s = collections.Counter(s)
            return s[min(s)]

        queries = [f(q) for q in queries]
        n, words = len(words), sorted(f(w) for w in words)
        return [n - bisect.bisect(words, q) for q in queries]