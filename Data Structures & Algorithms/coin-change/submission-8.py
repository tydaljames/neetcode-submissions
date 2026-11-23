class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = [float('inf') for _ in range(amount + 1)]
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            # if memo[amount] != float('inf'):
            if amount in memo:
                return memo[amount]

            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
                    # memo[amount] = min(dfs(amount - coin) + 1, memo[amount])

            # return memo[amount]
            memo[amount] = res
            return res


        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1