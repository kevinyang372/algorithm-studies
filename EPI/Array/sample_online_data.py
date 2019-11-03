# Design a program that takes as input a size k, and reads packets, continuously maintaining a uniform random subset of size k of the read packets.
import random

class Sample:

    def __init__(self, k):
        self.subset = []
        self.seen = 0
        self.cap = k

    def read(self, packet):
        if len(self.subset) < self.cap:
            self.subset.append(packet)
            self.seen += 1
        elif random.randint(0, self.seen) < k:
            self.subset[random.randint(0, k - 1)] = packet

    def subset(self):
        return self.subset
