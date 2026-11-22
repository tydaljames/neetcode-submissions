class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, n, rob1):
            if i >= n:
                return 0

            if memo[i][rob1] > -1:
                return memo[i][rob1]

            take = dfs(i + 2, n, rob1) + nums[i]
            skip = dfs(i + 1, n, rob1)

            print(take, skip, nums[i])

            memo[i][rob1] = max(take, skip)
            return memo[i][rob1]


        take1 = dfs(0, n - 1, True)
        skip1 = dfs(1, n, False)

        return nums[0] if n == 1 else max(take1, skip1)
