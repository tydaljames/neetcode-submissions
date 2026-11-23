class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        coins.sort()
        dp[0] = 0

        for i in range(amount):
            for coin in coins:
                if coin + i > amount:
                    break
                dp[coin + i] = min(dp[coin + i], dp[i] + 1)

        return dp[amount] if dp[amount] < float('inf') else -1
                

