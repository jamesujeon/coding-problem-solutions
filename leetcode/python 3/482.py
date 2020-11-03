# 문제 링크: https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        reminder = len(S) % K

        parts = [S[:reminder]] if reminder else []
        for i in range(reminder, len(S), K):
            parts.append(S[i:i + K])

        return '-'.join(parts)