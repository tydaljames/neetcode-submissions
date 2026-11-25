class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [-1 for _ in range(n)]
        minWord = float('inf')
        maxWord = 0

        for word in wordDict:
            minWord = min(len(word), minWord)
            maxWord = max(len(word), maxWord)

        def word(left):
            # print(left, memo)
            if left >= n:
                # return s[left:right + 1] in wordDict
                return True

            if memo[left] != -1:
                return memo[left]
            
            for right in range(left + minWord, n + 1):
                # print(left, right)
                substring = s[left:right]
                # print(substring)

                if (right - left) > maxWord:
                    # print("Too big")
                    break
                    # memo[left] = False
                    # return memo[left]

            # memo[left] = word(left, right + 1)

                

                if substring in wordDict:
                    memo[left] = word(right) or memo[left]
                    # print(memo)

                    if memo[left] == True:
                        return memo[left]

            # print("Finished loop")
            memo[left] = False
            # print(left, memo)
            return memo[left]


        return word(0)
        