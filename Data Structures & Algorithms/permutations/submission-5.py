class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        n = len(nums)
        
        def dfs(perm, length):
            if length == n:
                perms.append(perm.copy())
                return

            for i in range(n):
                num = nums[i]
                if num == -1000:
                    continue

                perm.append(num)

                nums[i] = -1000
                dfs(perm, length + 1)
                perm.pop()
                nums[i] = num


        dfs([], 0)
        return perms
            