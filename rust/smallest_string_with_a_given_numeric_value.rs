use std::char;

impl Solution {
    pub fn get_smallest_string(n: i32, k: i32) -> String {
        let base: u32 = 96;
        let mut total = k.clone() as u32;
        let mut result = String::from("");
        
        for i in 0..n {
            if i == n - 1 {
                result.push(char::from_u32(total + base).unwrap());
            } else if total <= (n as u32 - i as u32 - 1) * 26 {
                result.push(char::from_u32(1 + base).unwrap());
                total -= 1;
            } else {
                let current = total - (n as u32 - i as u32 - 1) * 26;
                result.push(char::from_u32(base + current).unwrap());
                total -= current;
            }
        }
        
        result
    }
}