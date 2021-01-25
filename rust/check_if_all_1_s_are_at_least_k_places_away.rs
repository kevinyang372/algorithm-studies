impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut prev = -1;
        
        for i in 0..nums.len() {
            if nums[i] == 1 {
                if prev >= 0 && i as i32 - prev - 1 < k {
                    return false;
                }
                prev = i as i32;
            }
        }
        
        true
    }
}