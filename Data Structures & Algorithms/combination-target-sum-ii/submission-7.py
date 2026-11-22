class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        n = len(candidates)
        candidates.sort()
        # print(candidates)

        def dfs(combo, sum, i):
            print(combo, sum)

            if sum == target:
                combos.append(combo.copy())
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if sum + candidates[j] > target:
                    return

                # take
                combo.append(candidates[j])
                dfs(combo, sum + candidates[j], j + 1)
                combo.pop()


        dfs([], 0, 0)
        return combos