#
# @lc app=leetcode id=355 lang='python3'
#
# [355] Design Twitter
#

# @lc code=start

# T = 38
from heapq import *
from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.last_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # we can only ever display 10 tweets in the newsfeed
        # so the max we ever need to store for a user is 10
        # for the cases where they don't follow anyone and have 10 tweets
        if len(self.tweets[userId]) < 10:
            self.tweets[userId].appendleft((self.last_id, tweetId))
        else:
            self.tweets[userId].pop()
            self.tweets[userId].appendleft((self.last_id, tweetId))
        self.last_id += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        news = [t for t in self.tweets[userId]]
        heapify(news)
        for followeeId in self.following[userId]:
            for tweet in self.tweets[followeeId]:
                if len(news) < 10:
                    heappush(news, tweet)
                else:
                    heappushpop(news, tweet)
        return [n[1] for n in sorted(news, reverse=True)]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end