class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1 for _ in range(n)]

        rob1 = False

        def dfs(i, n, memo):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]

            take = dfs(i + 2, n, memo) + nums[i]
            skip = dfs(i + 1, n, memo)

            memo[i] = max(take, skip)
            print(i, n, memo)
            return memo[i]


        take1 = dfs(0, n - 1, memo.copy())
        skip1 = dfs(1, n, memo.copy())

        return max(take1, skip1)
