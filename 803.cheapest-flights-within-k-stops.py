#
# @lc app=leetcode id=803 lang='python3'
#
# [803] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # this is basically a greedy problem that is very similar to a
        # dynamic programming problem.  
        
        # data comes in as a list so we'll need to build a graph out of it
        # also, we'll need to keep track of the min price from the origin
        # to the node we're looking at visiting.  this allows us to optimize
        # the traversal to not bother adding more prices (edges) 
        # if we're already above existing minimum we've already seen.
        # initialize all min values as inf
        graph, min_totals = [[] for _ in range(n)], [float("inf")] * n
        for _from, to, price in flights:
            graph[_from].append((to, price))
        q = deque([(src, 0, 0)])
        while q:
            # we're using a BFS iteration by popping from left and pushing right
            _from, depth, total = q.popleft()
            for to, price in graph[_from]:
                # add the price to visit this neighbor to the
                # price to get to node
                summed = total + price
                # if we've already hit max depth or the price to visit
                # the neighbor is more than a path that has already visited
                # then stop this path here
                if depth > k or summed > min_totals[to]:
                    continue
                # otherwise if we still have room to explore, set the cost to
                # the (now guaranteed) min cost value
                min_totals[to] = summed
                # continue bfs by adding this to the right
                q.append((to, depth+1 , total + price))
        # if we never reached the destination node then it will
        # still have the initial value of inf
        return min_totals[dst] if min_totals[dst] != float("inf") else -1
# @lc code=end