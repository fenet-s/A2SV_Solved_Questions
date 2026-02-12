from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        domain_map = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                domain_map['.'.join(domains[i:])] += count
        return ['{} {}'.format(v, k) for k, v in domain_map.items()]