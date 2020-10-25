# Instagram

## Requirements
1. User could upload pictures and videos to post them.
2. Users should be able to follow each other and see their posts.
3. Liking and commenting functionalities.
4. News feed generating functionalities.

## Constraints
* Service should always be highly available.
* Consistency is not the top concern here -- users could wait a couple of seconds to see the latest posts.
* We expect more reads than writes.
* The system should be highly reliable -- we should not lose any photo of the users.

## Capacity Estimates
Assumptions:
* 1M active users
* One user posts 2 pictures per day on average.
* One picture has an average size of 500 KB
* Read to write is 100:1

Storage:
1M * 2 * 500 KB = 1 TB/day

Bandwidth:
1 TB / 86400 = 10 GB/s

## High Level Design
Clients => LB => Server => Metadata DB / Cloud Storage

## Database Design
NoSQL is preferred over MySQL due to the following reasons:
* Sharding is necessary due to the large number of photos.
* We want to have replications for better reliability.

> **User table**\
> user_id (PK)\
> user_name\
> created_at

> **Photo table**\
> photo_id (PK)\
> photo_path\
> user_id\
> created_at

> **Follow table**\
> follow_id (PK)\
> user_id\
> follower_ids (list)\
> created_at

For the User and Photo table, we could use key-value NoSQL storage like Redis.\
For the Follow and User to Photo mapping table, since we need to store lists, we could use wide column NoSQL storage like HBase.

## Key Component Design
Since write requests tend to be much more heavy than read requests and we expect more read requests than write requests, we may face the situation that
the write requests take over majority of the traffic, significantly reducing the availability of the read requests.

One solution to this is to separate the photo upload service and photo read service. We could also add caching to the photo read service to further reduce latency.

## Sharding
Solution 1 - Partition based on user id\
While this seems to be the most straightforward solution, there could be a couple of factors that lead to a non-uniform partition: 1) There could have a couple of 'hot users'
having a lot of followers. 2) Some users could have significantly more photos than others

Solution 2 - Partition based on photo id\
We could have a KGS service running in the backend to generate keys for photos.

## News Feed Delivery
1. **Pull Model**\
The users will send requests to the server to pull updates at a constant interval or via manual refreshing. However, possible problems could be a) Most pull requests will be empty
which means additional traffic to the server b) An update won't be shown until the client issues a pull.

2. **Push Model**\
A server could push updates to the clients as soon as they are ready. This could be done by having the clients open a long pulling request with the server. A possible problem is 
if a user follows many other accounts, the server has to push quite often.

3. **Hybrid Model**\
We could adopt a hybrid model to solve both problems. For users who have a large number of followers, we could use a push model while for the rest of users, we use a pull model.

## Caching
For the photo storage, we could utilize Content Delivery Network (CDNs) to put the caching closer to users.

For metadata, we could utilize Memcache to avoid frequent request to application server and metadata database for hot user data.
