class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def bfs():
            q = deque()
            q.append((beginWord, 1))

            while q:
                node = q.popleft()
                word = node[0]
                dist = node[1]

                if word == endWord:
                    return dist
                if word in seen:
                    continue

                seen.add(word)

                for neighbor in adjList[word]:
                    q.append((neighbor, dist + 1))

            return 0

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

        
        seen = set()
        return bfs()






                