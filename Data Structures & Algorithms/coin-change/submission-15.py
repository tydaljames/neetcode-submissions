class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda: float('inf'))

        def dfs(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            for coin in coins:
                memo[amount] = min(dfs(amount - coin) + 1, memo[amount])

            return memo[amount]


        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1