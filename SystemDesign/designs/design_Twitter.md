# Twitter

## Requirements
1. User can post tweets.
2. User can follow other users.
3. There should be a timeline generated everytime user refreshes.
4. Tweets should be able to contain images and videos.

## Constraints
* The service should be highly available.
* The latency should be minimized.
* Consistency could take a hit -- it will be fine if some users don't see a tweet for a second or two.
* Read-heavy system

## Capacity Estimation
Assumptions:
* 1M active users
* Each user posts 2 tweets every day
* The average size of a tweet is 500 KB
* Read to write ratio is 10:1

Storage: 1M * 2 * 500 KB = 1TB / day

Bandwidth: 1TB / 86400 = 11MB / sec

## System API
API for posting tweets:
```
post_tweet(api_key, tweet_content) -> url for the tweet
```

## High Level Design
![image](https://user-images.githubusercontent.com/30107576/97817347-a53afd00-1c50-11eb-9842-e3cd736b463d.png)

## Database Design
> **Tweet**\
> tweet_id (PK)\
> user_id\
> created_at\
> tweet_location\
> content_location\
> number_of_likes

> **User**\
> user_id (PK)\
> created_at\
> username\
> last_login

> **UserFollow**\
> user_id1 (PK)\
> user_id2 (PK)

> **Favorite**\
> tweet_id (PK)\
> user_id (PK)\
> creation_time\

## Data Sharding
**Sharding by user id**\
Store all the data of one user in a server. When querying, we could hash the user id and find the corresponding server for storing that user's information.
- Some hot users may get many queries everyday that could overload the system.
- The number of tweets each user has is probably not uniformly distributed.

**Sharding by tweet id**\
Assign a random server for each tweet. However, to query on specific attributes, we need to ask every server for the set of tweets it is storing, filter, 
and aggregate the results to return to the user
- Very costly as we need to query all databases to find a specific tweet.

**Sharding by creation time**
- The traffic won't be uniform -> while writing, all traffic will go to one server and while reading, most traffic will go to the server storing latest information.

**Sharding by combining tweet creation time and id**\
Create a unique key with the first part being the epoch seconds of the current time and the second part an auto-incrementing sequence to make each id unique.
To filter on the result, we still need to query all servers but the read will be significantly faster as we don't need to filter upon read time any more.

## Generating News Feeds
**Considerations**
* Some users may have a large following group and some hot users may have many users.
* The system should be able to generate any user feed in real time with low latency.
* The latest tweets should be reflected almost immediately in the feeds.

**API**\
```
get_user_feed(api_key, user_id, filters) -> list of tweets
```

**Workflow**
1. Retrieve a list of follows of a user sorted by their creation time.
2. Rank these posts based on relevance to the user.
3. Store the feed in a cache server.
4. Return the top N tweets in the feed.
5. When user refreshes, return the next N posts.

**Problem with Online Feed Generation**
1. Database queries are slow and costly for users that follows many people.
2. Live updates could lead to high push traffic to the clients.

**Offline Feed Generation**\
We could have dedicated servers that generates feed offline and store it in a stack structure. Every user updates will be pushed to the feed generation pipeline.
When a user refreshes, the server responds with the latest N feed items generated.
