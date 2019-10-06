def isPalindrome(x):
    if x < 0:
        return False
    
    num = 0
    copy = x
    
    while copy:
        num *= 10
        num += copy % 10
        copy /= 10
        
    return num == x
        