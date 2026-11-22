class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        n = len(nums)

        def dfs(combo, sum, i):
            if i >= n or sum > target:
                return

            if sum == target:
                combos.append(combo.copy())
                return
            
            dfs(combo, sum, i + 1)
            
            
            combo.append(nums[i])
            
            dfs(combo, sum + nums[i], i)
            combo.pop()

        dfs([], 0, 0)
        return combos

