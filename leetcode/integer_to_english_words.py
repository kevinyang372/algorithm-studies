# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:

# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

# Constraints:

# 0 <= num <= 231 - 1

def numberToWords(self, num: int) -> str:
    if num == 0: return 'Zero'
    
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
       'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    
    if num >= 10 ** 9:
        pre = self.numberToWords(num // 10 ** 9)
        sub = num % 10 ** 9
        if sub == 0:
            return pre + ' Billion'
        return pre + ' Billion ' + self.numberToWords(sub)
    elif num >= 10 ** 6:
        pre = self.numberToWords(num // 10 ** 6)
        sub = num % 10 ** 6
        if sub == 0:
            return pre + ' Million'
        return pre + ' Million ' + self.numberToWords(sub)
    elif num >= 1000:
        pre = self.numberToWords(num // 1000)
        sub = num % 1000
        if sub == 0:
            return pre + ' Thousand'
        return pre + ' Thousand ' + self.numberToWords(sub)
    elif num >= 100:
        pre = self.numberToWords(num // 100)
        sub = num % 100
        if sub == 0:
            return pre + ' Hundred'
        return pre + ' Hundred ' + self.numberToWords(sub)
    elif num >= 20:
        pre = tens[num // 10 - 2]
        sub = num % 10
        if sub == 0:
            return pre
        return pre + ' ' + self.numberToWords(sub)
    else:
        return to19[num - 1]