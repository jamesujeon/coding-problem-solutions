# 문제 링크: https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counts = {}
        for cpdomain in cpdomains:
            count, components = cpdomain.split()
            count = int(count)
            components = components.split('.')

            subdomains = ['.'.join(components[i:]) for i in range(len(components))]
            for subdomain in subdomains:
                if subdomain not in subdomain_counts:
                    subdomain_counts[subdomain] = 0
                subdomain_counts[subdomain] += count
        return [f'{count} {subdomain}' for subdomain, count in subdomain_counts.items()]