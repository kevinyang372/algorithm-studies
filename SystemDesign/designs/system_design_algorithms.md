# System Design Algorithms

## Bloom Filter
**Why Bloom Filter**\
Quickly check whether an item is present in a set. There could have false positives but no false negatives.

**Algorithm Overview**
1. Initialize m bits (all 0)
2. Create k hash functions with each all them mapping an input to one of the m bits
3. When inserting a new item, pass the variable through k hash functions and set the output bits to 1
4. When checking the existence of an item, pass the variable through k hash functions and check if the output bits are all 1

**Example**\
Web crawler uses Bloom Filter to check whether the url has already been explored by another crawler.

## Frugal Streaming
**Why Frugal Streaming**\
Use a small set of memories (one or two) to estimate stats of data stream

**Algorithm Overview**
*Frugal-1U*
```
m = 0
for s in stream:
    if s > m:
        m += 1
    else:
        m -= 1
```

## Geohash
**Why Geohash**\
Location-based search -- find or match nearby items / people.

**Algorithm Overview**
1. The hash consists of 12 characters. Each represents a grid of different sizes on Earth.
2. The first character of the hash identifies one of 32 cells in the grid, roughly 5000km x 5000km on the planet.
3. The second character identifies one of the 32 squares in the first cell, so the resolution of the two characters combined is now 1250km x 1250km.
4. This continues until the twelfth character, which can identify an area as small as just a couple of square inches on Earth.

**Example**\
Google Maps / Uber / Tinder...

## API Rate Limiting
**Why API Rate Limiting**\
API Rate Limiting protects the endpoints from exploding request traffic and malicious DDoS attacks

**Algorithm Overview**
1. Leaky Bucket / Token Bucket: Apply a fixed-size queue (FIFO) for requests. Problem: Recent requests could starved out by older requests.
2. Fixed Window: Limit the request rate in a specific timeframe (one minute for example)

## Quadtree
**Why Quadtree**
Proximity ordering in O(logN) time -- the algorithm allows for quick fetching of nearest N neigbhors.

**Algorithm Overview**
1. Recursively divide a geospace into four subspaces and register the points into the corresponding subspaces.
2. Stop when the number of points one subspaces hold is under a pre-set threshold.

**Examples**
Uber's nearest driver

## B Tree / B+ Tree
**Why B Tree**\
Fast access to records stored in database without a linear scan on all data points.

**Algorithm Overview**
1. Build a tree bottom up.
2. When a node exceeds the number of elements it can store, split the node and push one element to its parent node / create a parent node.
