use std::cmp::max;
use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        
        fn increase_or_create(d: &mut HashMap<i32, i32>, num: i32) {
            match d.get_mut(&num) {
                Some(v) => { *v += 1; },
                _ => (),
            }
            
            if !d.contains_key(&num) {
                d.insert(num, 1);
            }
        }
        let mut d = HashMap::new();
        let mut max_val = 0;
        
        for num in nums {
            increase_or_create(&mut d, num);
        }
        
        for (key, value) in &d {
            match d.get(&(key + 1)) {
                Some(v) => { max_val = max(max_val, *v + value); },
                _ => (),
            }
        }
        
        max_val
    }
}