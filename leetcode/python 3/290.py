# 문제 링크: https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def convert(words: List[str]) -> List[str]:
            i, d = 0, {}
            for word in words:
                if word not in d:
                    d[word] = i
                    i += 1
            return [d[word] for word in words]

        return convert(list(pattern)) == convert(s.split())