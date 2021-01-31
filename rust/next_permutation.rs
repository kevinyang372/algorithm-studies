impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        if nums.len() == 1 { return; }
        let length = nums.len();
        
        for i in 1..length {
            if nums[length - i - 1] < nums[length - 1] {
                let mut j = length - 1;
                
                while j > length - i - 1 && nums[j] > nums[length - i - 1]{
                    j -= 1;
                }
                
                let temp = nums[length - i - 1];
                nums[length - i - 1] = nums[j + 1];
                nums[j + 1] = temp;
                return;
            }
            
            let mut j = length - i;
            
            while j < length {
                let temp = nums[j - 1];
                nums[j - 1] = nums[j];
                nums[j] = temp;
                j += 1;
            }
        }
    }
}