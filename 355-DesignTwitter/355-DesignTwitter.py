# Last updated: 10/8/2025, 9:50:58 PM
class Twitter:

    def __init__(self):
        self.count=0
        self.followerset=defaultdict(set)
        self.tweet_list=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_list[userId].append((self.count,tweetId))
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]

        self.followerset[userId].add(userId)
        for followeeId in self.followerset[userId]:
            if followeeId in self.tweet_list and self.tweet_list[followeeId]:
                index=len(self.tweet_list[followeeId])-1
                count,tweet_id=self.tweet_list[followeeId][index]
                heapq.heappush(heap,[count,tweet_id,followeeId,index-1])
        while heap and len(res) < 10:
            count,tweet_id,followeeId,index=heapq.heappop(heap)
            res.append(tweet_id)
            if index>=0:
                count,tweet_id=self.tweet_list[followeeId][index]
                heapq.heappush(heap,[count,tweet_id,followeeId,index-1])
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerset[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerset[followerId]:
            self.followerset[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)