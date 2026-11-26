class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def dfs(node, prev):
            if node == endWord:
                return 1
            if node in seen:
                return float('inf')

            seen.add(node)

            minLadder = float('inf')
            for neighbor in reversed(adjList[node]):
                if neighbor == prev:
                    continue
                minLadder = min(dfs(neighbor, node) + 1, minLadder)
                adjList[node].remove(neighbor)
            
            seen.remove(node)
            return minLadder


        n = len(wordList) + 1
        m = len(wordList[0])
        adjList = defaultdict(list)
        wordList.append(beginWord)

        for i in range(n):
            for j in range(i + 1, n):
                word1 = wordList[i]
                word2 = wordList[j]

                oneOff = 0

                for k in range(m):
                    char1 = word1[k]
                    char2 = word2[k]

                    if char1 == char2:
                        continue

                    oneOff += 1
                    if oneOff > 1:
                        break
                
                if oneOff != 1:
                    continue
                
                adjList[word1].append(word2)
                adjList[word2].append(word1)


        
        print(adjList)
        seen = set()
        minLadder = dfs(beginWord, "")
        return minLadder if minLadder < float('inf') else 0






                