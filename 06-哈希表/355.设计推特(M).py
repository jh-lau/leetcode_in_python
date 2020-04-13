"""
  @Author       : liujianhan
  @Date         : 2020/4/13 上午9:27
  @Project      : leetcode_in_python
  @FileName     : 355.设计推特(M).py
  @Description  : 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。
    你的设计需要支持以下的几个功能：
    postTweet(userId, tweetId): 创建一条新的推文
    getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
    follow(followerId, followeeId): 关注一个用户
    unfollow(followerId, followeeId): 取消关注一个用户
    示例:

    Twitter twitter = new Twitter();

    // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
    twitter.postTweet(1, 5);

    // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
    twitter.getNewsFeed(1);

    // 用户1关注了用户2.
    twitter.follow(1, 2);

    // 用户2发送了一个新推文 (推文id = 6).
    twitter.postTweet(2, 6);

    // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
    // 推文id6应当在推文id5之前，因为它是在5之后发送的.
    twitter.getNewsFeed(1);

    // 用户1取消关注了用户2.
    twitter.unfollow(1, 2);

    // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
    // 因为用户1已经不再关注用户2.
    twitter.getNewsFeed(1);
"""
import heapq
import itertools
from typing import List
from collections import defaultdict, deque


# 104ms, 19.4MB
class Twitter:
    def __init__(self):
        self.followee = defaultdict(set)
        self.tweet = defaultdict(deque)
        self.time = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.time += 1
        self.tweet[user_id].appendleft((self.time, tweet_id))

    def get_news_feed(self, user_id: int) -> List[int]:
        user_id not in self.followee[user_id] and self.followee[user_id].add(user_id)
        return [
            tweet for _, tweet in itertools.islice(heapq.merge(
                *map(self.tweet.__getitem__, self.followee[user_id]),
                reverse=True
            ), 0, 10)
        ]

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followee[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followee[follower_id].discard(followee_id)

