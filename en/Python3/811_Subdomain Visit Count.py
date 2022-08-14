# @algorithm @lc id=829 lang=python3 
# @title subdomain-visit-count

from collections import defaultdict
from en.Python3.mod.preImport import *
# @test(["9001 discuss.leetcode.com"])=["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# @test(["900 google.mail.com","50 yahoo.com","1 intel.mail.com","5 wiki.org"])=["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        flat = defaultdict(int)
        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            split = domain.split(".")[::-1]
            path = split[0]
            flat[path] += count
            for part in split[1:]:
                path = f"{part}.{path}"
                flat[path] += count
        return [f"{count} {domain}" for domain, count in flat.items()]
                