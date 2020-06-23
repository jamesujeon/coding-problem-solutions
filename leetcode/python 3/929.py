# 문제 링크: https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            splits = email.split('@')
            result.add(splits[0].split('+')[0].replace('.', '') + '@' + splits[1])
        return len(result)