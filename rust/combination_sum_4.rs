impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let mut dp: Vec<i32> = vec![0; target as usize + 1];
        dp[0] = 1;
        
        for i in 1..dp.len() {
            for num in &nums {
                if i as i32 - num >= 0 {
                    dp[i] += dp[i - *num as usize];
                }
            }
        }
        
        *dp.last().unwrap()
    }
}