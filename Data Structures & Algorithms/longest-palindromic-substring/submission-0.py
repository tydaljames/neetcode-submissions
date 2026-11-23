class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def isPalindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True


        def expand(left, right):
            nonlocal length
            nonlocal longest
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            local = (right - left) - 1
            # print(s[left + 1], s[right - 1], local)
            print(left + 1, right - 1, local)


            if local > length:
                print("longer", local, length, left, right)
                length = local
                longest = [left + 1, right - 1]

        
        length = 1
        longest = [0, 0]

        for i in range(1, n):
            expand(i - 1, i + 1)

        for i in range(0, n):
            expand(i, i + 1)

        print(longest)

        return s[longest[0] : longest[1] + 1]
        