class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1 for _ in range(n)]

        def climb(i):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]
            
            memo[i] = min(climb(i + 1), climb(i + 2)) + cost[i]
            return memo[i]

        return min(climb(0), memo[1])
