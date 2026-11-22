class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        n = len(nums)

        def dfs(combo, sum, i):
            if i >= n or sum > target:
                return

            # print(sum)

            if sum == target:
                combos.append(combo.copy())
                return
            
            skip = dfs(combo, sum, i + 1)
            
            sum += nums[i]
            combo.append(nums[i])
            
            take = dfs(combo, sum, i)
            combo.pop()

        dfs([], 0, 0)
        return combos

