impl Solution {
    pub fn most_competitive(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut stack = Vec::new();
        
        for i in 0..nums.len() {
            let mut remaining = nums.len() - i;
            while stack.len() > 0 && stack[stack.len() - 1] > nums[i] && remaining + stack.len() > k as usize {
                stack.pop();
            }
            stack.push(nums[i]);
        }
        
        while stack.len() > k as usize {
            stack.pop();
        }
        
        stack
    }
}