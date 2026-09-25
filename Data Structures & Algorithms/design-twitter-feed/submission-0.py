import heapq as hq

class Twitter:
    """
    when see 10 most recent -> heap
    keep track of:
    * global time to track which tweet comes first
    * dictionary with key as userId and values as their tweetId
    * dictionary to map followers and following using userId
    
    """

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)  # k: userId, v: [userId]
        self.tweets = defaultdict(list)  # k: userId, v: [(time, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        # append (time, tweetId) per post
        self.tweets[userId].append((self.time, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        # u = users that actually count
        users = set(self.following[userId])
        users.add(userId) # each userId follow themselves

        # populate heap with each person newest tweet
        h = []
        for u in users:
            if u in self.tweets: # check if user ever posted a tweet
                i = len(self.tweets[u]) - 1 # index of latest tweet
                t, tid = self.tweets[u][i] # only unpack the last tweet
                # push negated time to get latest tweets
                hq.heappush(h, (-t, u, tid, i - 1)) # index of next older one
    
        # each pop always newest tweet left across everyone
        res = []
        while h and len(res) < 10:
            _, u, tid, i = hq.heappop(h)
            res.append(tid) 
            # if this user still has more tweets
            if i >= 0:
                t, next_tid = self.tweets[u][i] # i is next older one
                hq.heappush(h, (-t, u, next_tid, i - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # chech if followeeId exists, avoid crash
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)