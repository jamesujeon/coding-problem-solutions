# 문제 링크: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(1 for word in sentence.split() if re.match("^([a-z]+(-?[a-z]+)?)?[!.,]?$", word))
