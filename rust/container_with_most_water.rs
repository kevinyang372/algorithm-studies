use std::cmp::{max, min};

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = height.len() - 1;
        
        let mut mx = min(height[i], height[j]) * (j - i) as i32;
        
        while i < j {
            if height[i] < height[j] {
                let mut di = 1;
                while i + di < j && height[i + di] < height[i] {
                    di += 1;
                }
                i += di;
            } else {
                let mut dj = 1;
                while j - dj > i && height[j - dj] < height[j] {
                    dj += 1;
                }
                j -= dj;
            }
            
            if i < j {
                mx = max(mx, min(height[i], height[j]) * (j - i) as i32);
            }
        }
        
        mx
    }
}