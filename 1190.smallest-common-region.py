
#
# @lc app=leetcode id=1190 lang='python3'
#
# [1190] Smallest Common Region
#

# @lc code=start
        
class Solution:
    def findSmallestRegion(self, regions: list[list[str]], region1: str, region2: str) -> str:
        graph = {}
        for region in regions:
            parent, children = region[0], region[1:]
            for child in children:
                graph[child] = parent
                
        lineage = set([region1])
        while (parent := graph.get(region1)):
            lineage.add(parent)
            region1 = parent
    
        if region2 in lineage:
            return region2
        
        while (parent := graph.get(region2)):
            if parent in lineage:
                return parent
            region2 = parent
        
# @lc code=end