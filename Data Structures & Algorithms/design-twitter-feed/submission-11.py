class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.postCount, tweetId, userId))
        self.postCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.posts[userId].copy()
        numPosts = {userId : 0}

        for followed in self.follows[userId]:
            print("f", followed)
            if self.posts[followed]:
                numPosts[followed] = len(self.posts[followed]) - 1
                heap.append(self.posts[followed][numPosts[followed]])

        heapq.heapify_max(heap)
        count = 10
        top10 = []

        while heap and count > 0:
            tweet = heapq.heappop_max(heap)
            top10.append(tweet[1])
            followed = tweet[2]
            numPosts[followed] -= 1
            if numPosts[followed] >= 0:
                heapq.heappush_max(heap, self.posts[followed][numPosts[followed]])
            
            count -= 1

        return top10


        # return [tweet[1] for tweet in heapq.nlargest(10, heap)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
