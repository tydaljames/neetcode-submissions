class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1 for _ in range(n + 1)]

        def climb(i):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]
            
            take1 = climb(i + 1)
            take2 = climb(i + 2)

            memo[i] = min(take1, take2) + cost[i]
            print(i, n, take1, take2, memo[i])

            return memo[i]

        return min(climb(0), climb(1))
