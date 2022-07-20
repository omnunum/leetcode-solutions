# @algorithm @lc id=2026 lang=python3 
# @title merge-triplets-to-form-target-triplet


from en.Python3.mod.preImport import *
# @test([[2,5,3],[1,8,4],[1,7,5]],[2,7,5])=true
# @test([[3,4,5],[4,5,6]],[3,2,5])=false
# @test([[2,5,3],[2,3,4],[1,2,5],[5,2,3]],[5,5,5])=true
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = target
        li, ri = 0, 0
        n = len(triplets)
        while ri < n:
            l, r = triplets[li], triplets[ri]
            # disqualify right side if any values go above target
            if [True for i in range(3) if r[i] > t[i]]:
                ri += 1
                continue
            # disqualify left side if any values go above target
            # right side needed to come first since we dont want
            # li to ever be greater then ri
            if [True for i in range(3) if l[i] > t[i]]:
                li += 1
                continue
            # test for success criteria
            merged = [max(l[i], r[i]) for i in range(3)]
            if merged == t:
                return True
            # if merging would have more matches over the left window
            # then we call that a partial success and move both windows
            l_match_count = sum([1 for i in range(3) if l[i] == t[i]])
            merged_match_count = sum([1 for i in range(3) if merged[i] == t[i]])
            if merged_match_count > l_match_count:
                triplets[ri] = merged
                li, ri = ri, ri+1
            # if it wouldn't be an improvement, abandon the merge and 
            # just move the right window forward to try the next combo
            else:
                ri += 1
        return False
