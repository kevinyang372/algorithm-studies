use std::i32;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut dp = vec![None; amount as usize + 1];
        dp[0] = Some(0);
        
        for i in 0..dp.len() - 1 {
            if let Some(step) = dp[i] {
                for &c in &coins {
                    let next_ind = i + c as usize;
                    if next_ind <= amount as usize {
                        dp[next_ind] = Some(dp[next_ind].unwrap_or(i32::MAX).min(step + 1));
                    }
                }
            }
        }
        
        dp[dp.len() - 1].unwrap_or(-1)
    }
}