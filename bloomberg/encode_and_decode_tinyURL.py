# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# naive hashing
class Codec:
    
    def __init__(self):
        self.hash_key = {}
        self.key_hash = {}

    def encode(self, longUrl):
        l = abs(hash(longUrl)) % 10000
        self.key_hash[longUrl] = l
        self.hash_key[l] = longUrl       
        return l    

    def decode(self, shortUrl):
        return self.hash_key[shortUrl]

# tinyURL like
import string
import random

class Codec:
    
    def __init__(self):
        self.base = 'http://tinyurl.com/'
        self.length = 6
        self.key_hash = {}

    def encode(self, longUrl):
        generate_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(self.length))
        while generate_url in self.key_hash:
            generate_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(self.length))
        self.key_hash[generate_url] = longUrl
        return self.base + generate_url

    def decode(self, shortUrl):
        generate_url = shortUrl.split('/')[-1]
        return self.key_hash[generate_url]