# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:

# Twitter twitter = new Twitter();

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);

# // User 1 follows user 2.
# twitter.follow(1, 2);

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);

# max heap
class Twitter(object):

    def __init__(self):
        self.posts = collections.defaultdict(list)
        self.follows = collections.defaultdict(list)
        self.followed = collections.defaultdict(list)
        self.feeds = collections.defaultdict(list)
        self.time = 0
        self.timeline = {}

    def postTweet(self, userId, tweetId):
        
        self.timeline[self.time] = tweetId
        
        self.posts[userId].append(self.time)
        heapq.heappush(self.feeds[userId], self.time)
        for i in self.followed[userId]:
            heapq.heappush(self.feeds[i], self.time)
        
        self.time += 1

    def getNewsFeed(self, userId):
        return [self.timeline[i] for i in heapq.nlargest(10, self.feeds[userId])]
        

    def follow(self, followerId, followeeId):
        
        if followerId == followeeId: return
        if followeeId in self.follows[followerId]: return
        
        self.follows[followerId].append(followeeId)
        self.followed[followeeId].append(followerId)
        for i in self.posts[followeeId]:
            heapq.heappush(self.feeds[followerId], i)
        

    def unfollow(self, followerId, followeeId):
        
        if followerId == followeeId: return
        if followeeId not in self.follows[followerId]: return
        
        self.follows[followerId].remove(followeeId)
        self.followed[followeeId].remove(followerId)
        for i in self.posts[followeeId]:
            self.feeds[followerId].remove(i)