# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def rotate(self, nums: List[int], k: int) -> None:
    if k == 0: return
    
    mod = -1
    count = 0
    for i in range(len(nums)):
        if i % k <= mod: break
            
        curr = nums[i]
        di = (i + k) % len(nums)
        
        while di != i:
            nums[di], curr = curr, nums[di]
            di = (di + k) % len(nums)
            count += 1
        
        nums[i] = curr
        mod = i % k
        count += 1
        
        if count == len(nums): break