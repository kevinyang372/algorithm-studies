# TinyURL

## Requirements
1. User should get a shortened version of the original URL.
2. Other users will get redirected to the original URL when entering the shortened URL.
3. The URL will expire after a certain time.
4. Users should be able to pick a custom URL.

## Capacity Estimation
Assumptions:
* 1M URLs are created everyday
* Read to Write ratio is approximately 100:1
* Each URL takes around 500 bytes in storage

Storage:\
1M * 500 bytes = 500 MB/day

Bandwidth:\
1M * 100 * 500 bytes / 86400 seconds = 500 KB/s

## Key Constraints:
* Reads traffic are much more heavy than writes.
* Availability is important (we should always expect the redirection to work).
* Redirection should have minimum latency.
* Shortened Url should not be predictable.

## System API Design
Create URL:
```
create_url(api_key, original_url) -> returns unique shortened url
```

Delete URL:
```
delete_url(api_key, url)
```

## High Level Design
Clients => LB => Servers => LB => DB

## Database Design
NoSQL is preferred over MySQL due to the following reasons:
* There is very little relationship in between tables (so we don't need to worry about ACID as there's no foreign keys)
* We expect minimum latency when accessing the urls
* Partition is necessary given the large number of urls

> **User table**\
> user_id (PK)\
> api_key\
> created_at\

> **URL table**\
> url_id (PK)\
> shortened_url\
> original_url\
> user_id\
> created_at\
> expired_at\

## Key Generation
The method we are going to use to generate **unique** and **fixed length** encoded url

### Hashing Method
We could use hashing algorithms like MD5 or SHA256 to generate unique hashes for each input
and use encoding algorithms like Base64 and Base32 to transform the hash value into the alphabet sets we wanted

```
For example, with input value "my_url.com"
"my_url.com" == SHA256 ==> "b8d367217e876ace3458938b754bafc74177dd1605f77be8a46c0058a9ece36a"
"b8d367217e876ace3458938b754bafc74177dd1605f77be8a46c0058a9ece36a" == Base64 ==> "YjhkMzY3MjE3ZTg3NmFjZTM0NTg5MzhiNzU0YmFmYzc0MTc3ZGQxNjA1Zjc3YmU4YTQ2YzAwNThhOWVjZTM2YQ=="
```
* As a note here, N in Base_N represents the number of characters used to represent the encoded string. For example, Base64 will have 64 unique characters and Base32 will have 32.

**Problem:** \
How are we going to limit the encoded url to a certain length? We could select the first or last n characters but this will likely cause a high overlap rate of results.

### Key Generation Service (KGS)
The alternative way is to have a Key Generation Service running in the backend to continue generating new keys.
In order to keep track of all the keys generated, we could have a used table and an available key table. Whenever a user selected a key, we remove it from the available key table and add it to used key.
We could also cache some keys in each app server to ensure the best response rate of each key.

## Caching
**How many urls should we cache?**\
Following the 80-20 rule, we would expect 20% of the urls generating 80% of the traffic. Therefore, we could cache 20% of the urls.

**Cache eviction policy?**\
LRU Cache.

## Data Purging
We should also have a clean-up service running in the backend to constantly pick-up expired links and remove them from the database.
