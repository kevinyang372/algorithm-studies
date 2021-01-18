use std::collections::HashMap;

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut c: HashMap<_, i32> = HashMap::new();
        let mut res: i32 = 0;
        
        for n1 in 0..nums.len() {
            let mut curr = &nums[n1];
            for n2 in n1 + 1..nums.len() {
                let mut sum = curr * &nums[n2];
                
                if let Some(v) = c.get_mut(&sum) {
                    res += v.clone();
                    *v += 1;
                } else {
                    c.insert(sum, 1);
                }
            }
        }
        
        res * 8
    }
}