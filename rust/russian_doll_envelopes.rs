use std::cmp::Reverse;

impl Solution {
    pub fn max_envelopes(envelopes: Vec<Vec<i32>>) -> i32 {
        let mut env: Vec<_> = envelopes.iter().map(|e| (e[0], Reverse(e[1]))).collect();
        env.sort();
        
        let mut dp: Vec<i32> = vec![1; env.len()];
        let mut res = 1i32;
        
        for i in 1..env.len() {
            let mut max_val = 1i32;
            for j in 0..i {
                if env[j].1 > env[i].1 {
                    max_val = max_val.max(dp[j] + 1);
                }
            }
            
            dp[i] = max_val;
            res = res.max(max_val);
        }
        
        res
    }
}