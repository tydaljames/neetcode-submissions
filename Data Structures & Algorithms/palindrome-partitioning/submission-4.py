class Solution:
    def partition(self, s: str) -> List[List[str]]:
        print = lambda *args, **kwargs: None
        palindromes = []
        substrings = []
        n = len(s)

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i):
            if i >= n:
                palindromes.append(substrings.copy())
                return

            for j in range(i, n):
                if isPalindrome(i, j):
                    substrings.append(s[i : j + 1])
                    dfs(j + 1)
                    substrings.pop()
                    

        dfs(0)
        return palindromes
