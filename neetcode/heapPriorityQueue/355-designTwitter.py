from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.user_followees = dict()
        self.last_timestamp = 0
        self.user_feed = dict()
        self.user_tweets = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((-self.last_timestamp, tweetId))

        self.last_timestamp += 1

        # add user to follow himselft
        if userId not in self.user_followees:
            self.user_followees[userId] = set()
        self.user_followees[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_followees:
            return []

        heap_available_tweets = []
        for followee in self.user_followees[userId]:
            if followee not in self.user_tweets:
                continue
            heap_available_tweets.extend(self.user_tweets[followee])

        heapq.heapify(heap_available_tweets)

        feed = []
        i = 0
        MAX_TWEETS = 10
        while i < MAX_TWEETS and heap_available_tweets:
            timestamp, id = heapq.heappop(heap_available_tweets)
            feed.append(id)
            i += 1
        return feed
        
    def getNewsFeedOld(self, userId: int) -> List[int]:
        if userId not in self.user_followees:
            return []
            
        feed = []
        added_tweets = set()
        i = 0
        MAX_TWEETS = 10
        while i < MAX_TWEETS:
            # look at the tweets from user followees and append the most recent one
            largest_timestamp = float("-inf")
            largest_timestamp_tweet_id = None

            for followee in self.user_followees[userId]:
                if followee not in self.user_tweets:
                    continue

                # get most recent inedit tweet
                followee_last_tweet_id, followee_last_tweet_timestamp = None, None

                j = len(self.user_tweets[followee]) - 1
                while j >= 0:
                    (id, timestamp) = self.user_tweets[followee][j]
                    if id not in added_tweets:
                        (followee_last_tweet_id, followee_last_tweet_timestamp) = (id, timestamp)
                        break
                    j -= 1

                # user does not have tweets or all of them have been added
                if not followee_last_tweet_id:
                    continue                    

                if followee_last_tweet_timestamp > largest_timestamp:
                    largest_timestamp_tweet_id = followee_last_tweet_id

            if not largest_timestamp_tweet_id:
                break
            feed.append(largest_timestamp_tweet_id)
            added_tweets.add(largest_timestamp_tweet_id)
            i += 1

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followees:
            self.user_followees[followerId] = set()
        self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_followees:
            if followeeId in self.user_followees[followerId]:
                self.user_followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 4) # User 1 posts a new tweet (id = 5).
twitter.postTweet(2, 5) # User 1 posts a new tweet (id = 5).
twitter.unfollow(1, 2) # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]

# twitter = Twitter()
# twitter.follow(1, 5) # User 1 posts a new tweet (id = 5).
# print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]

# twitter = Twitter()
# twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
# print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2)    # User 1 follows user 2.
# twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
# print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2)  # User 1 unfollows user 2.
# print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
