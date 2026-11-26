class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.postCount, tweetId))
        self.postCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.posts[userId].copy()

        for followed in self.follows[userId]:
            for post in self.posts[followed]:
                heap.append(post)

        # heapq.heapify_max(heap)
        return [tweet[1] for tweet in sorted(heap, reverse=True)[:10]]


        # return [tweet[1] for tweet in heapq.nlargest(10, heap)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
