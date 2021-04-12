impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {
        let mut ans: Vec<i32> = (1..n - k).collect();
        
        for i in 0..k as usize + 1 {
            if i % 2 == 0 {
                ans.push(n - k + i as i32 / 2);
            } else {
                ans.push(n - i as i32 / 2);
            }
        }
        
        ans
    }
}