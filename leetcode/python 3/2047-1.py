# 문제 링크: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0

        for word in sentence.split():
            if any(ch.isdigit() for ch in word):
                continue

            hyphens = sum(ch == '-' for ch in word)
            if hyphens > 1 or (
                hyphens == 1 and (
                    word[0] == '-' or word[-1] == '-' or (
                        word[-1] in '!.,' and word[-2] == '-'
                    )
                )
            ): continue

            punctuations = sum(ch in '!.,' for ch in word)
            if punctuations > 1 or (
                punctuations == 1 and word[-1] not in '!.,'
            ): continue

            count += 1

        return count
