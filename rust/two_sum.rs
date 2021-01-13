use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        
        for (ind, num) in nums.iter().enumerate() {
            if seen.contains_key(&(target - num)) {
                return vec![*seen.get(&(target - num)).unwrap() as i32, ind as i32];
            }
            seen.insert(num, ind);
        }
            
        vec![]
    }
}