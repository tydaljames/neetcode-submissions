class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

        for i in range(n - 1):
            expand(i, i + 1)

        for i in range(1, n - 1):
            expand(i - 1, i + 1)

        return count