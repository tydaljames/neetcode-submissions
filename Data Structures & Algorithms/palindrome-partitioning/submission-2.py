class Solution:
    def partition(self, s: str) -> List[List[str]]:
        print = lambda *args, **kwargs: None
        palindromes = []
        n = len(s)

        def isPalindrome(subset):
            i, j = 0, len(subset) - 1
            while i < j:
                if subset[i] != subset[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(substring, substrings, i):
            print(substrings, substring, i, palindromes)

            if isPalindrome(substring):
                substrings.append("".join(substring))

                if i == n:
                    palindromes.append(substrings.copy())
                    substrings.pop()
                    return

                char = s[i]

                # Complete and start new substring
                temp = substring
                substring = [char]
                dfs(substring, substrings, i + 1)
                substrings.pop()
                substring = temp


            
            if i == n:
                return

            char = s[i]

            # Continue current substring
            substring.append(char)
            dfs(substring, substrings, i + 1)


            


            

        dfs([s[0]], [], 1)
        return palindromes
