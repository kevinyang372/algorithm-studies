use std::collections::HashMap;
use std::collections::HashSet;
use std::cmp::min;

impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut c = HashMap::new();
        let mut seen = HashSet::new();
        let mut total = 0;
        
        for num in nums {
            if num < k {
               match c.get_mut(&num) {
                   Some(v) => *v += 1,
                    _ => ()
                }

                if !c.contains_key(&num) {
                    c.insert(num, 1);
                } 
            }
        }
        
        
        for (key, value) in &c {
            if key.clone() * 2 == k {
                total += value / 2;
            } else if c.contains_key(&(k - key)) && !seen.contains(&(k - key)) {
                total += min(value, c.get(&(k - key)).unwrap());
            }
            seen.insert(key);
        }
        
        total
    }
}