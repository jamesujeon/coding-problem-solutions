# 문제 링크: https://leetcode.com/problems/most-common-word/

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]", ' ', paragraph.lower()).split()
        for word, _ in collections.Counter(paragraph).most_common():
            if word not in banned:
                return word