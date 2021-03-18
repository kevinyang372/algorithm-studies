impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let mut dp: Vec<(i32, i32)> = vec![(1, 1)];
        let mut res = 1i32;
        
        for i in 1..nums.len() {
            let mut mx = 1i32;
            let mut mn = 1i32;
            for j in 0..i {
                if nums[j] > nums[i] {
                    mn = mn.max(1 + dp[j].0);
                } else if nums[j] < nums[i] {
                    mx = mx.max(1 + dp[j].1);
                }
            }
            
            res = res.max(mn).max(mx);
            dp.push((mx, mn));
        }
        
        res
    }
}