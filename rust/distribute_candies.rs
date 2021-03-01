use std::cmp::min;
use std::collections::HashSet;

impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let mut h = HashSet::new();
        let length = candy_type.len() as i32;
        
        for candy in &candy_type {
            h.insert(candy);
        }
        
        min(length/2, h.len() as i32)
    }
}