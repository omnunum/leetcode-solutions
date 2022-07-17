#
# @lc app=leetcode id=207 lang='python3'
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre = defaultdict(list)
        for p in prerequisites:
            if p[0] == p[1]:
                return False
            pre[p[0]].append(p[1])
        q = deque(((c, set([c])) for c in pre.keys()))
        while q:
            c, already = q.popleft()
            while pre[c]:
                p = pre[c].pop()
                if p in already:
                    return False
                q.appendleft((p, already | set([p])))  
        return True
            
            
        
# @lc code=end