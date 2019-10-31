# Deisgn an API to get latest message id such that no previous messages are missing. It should have following methods:

# # this method should adds a message with id number as received message
# def ack(number)

# # this method should return the id of last message whose previous counts are not missing
# def latest()

# Eg. 
# ack(2)
# latest() => -1
# ack(1)
# latest() => 2
# ack(5)
# ack(4)
# latest() => 2
# ack(3)
# latest() => 5

class Message(object):

    def __init__(self):
        self.messages = set()
        self.head = 0

    def ack(self, ids):
        if ids == self.head + 1:
            self.head += 1

            while self.head + 1 in self.messages:
                self.head += 1
        else:
            self.messages.add(ids)


    def latest(self):
        return -1 if self.head == 0 else self.head