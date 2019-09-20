# Given an integer n, return 1 - n in lexicographical order.

# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

def lexicalOrder(self, n):
        
    res = []
    
    def search(num):
        if num <= n:
            base, cur = num // 10, num % 10
            for i in range(cur, 10):
                if base * 10 + i > n:
                    break
                res.append(base * 10 + i)
                search((base * 10 + i) * 10)
        return
    
    search(1)
    return res