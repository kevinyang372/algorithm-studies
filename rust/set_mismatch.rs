use std::collections::HashSet;

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut m: HashSet<i32> = (1i32..=nums.len() as i32).collect();
        let mut n: HashSet<i32> = HashSet::new();
        
        for num in nums {
            if m.contains(&num) {
                m.remove(&num);
            } else {
                n.insert(num);
            }
        }
        
        n.into_iter().chain(m.into_iter()).collect::<Vec<i32>>()
    }
}