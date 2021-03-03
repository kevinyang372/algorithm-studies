impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut n = (1i32..=nums.len() as i32).fold(0, |t, x| t^x);
        
        for num in nums {
            n ^= num;
        }
        
        n
    }
}