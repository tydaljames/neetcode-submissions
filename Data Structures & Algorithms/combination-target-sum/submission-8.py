class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        n = len(nums)
        nums.sort()

        def dfs(combo, sum, i):
            if sum == target:
                combos.append(combo.copy())
                return

            for j in range(i, n):
                if sum + nums[j] > target:
                    return
                
                combo.append(nums[j])
                dfs(combo, sum + nums[j], j)
                combo.pop()

        dfs([], 0, 0)
        return combos

