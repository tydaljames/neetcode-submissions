class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            memo[amount] = float('inf')
            for coin in coins:
                # if amount - coin >= 0:
                memo[amount] = min(dfs(amount - coin) + 1, memo[amount])

            return memo[amount]


        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1