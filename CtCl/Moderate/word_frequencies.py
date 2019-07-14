# Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?

def wordFrequency(book, word):
    return collections.Counter(book.split(' '))[word]