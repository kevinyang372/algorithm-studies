use std::cmp::min;

impl Solution {
    pub fn shortest_to_char(s: String, c: char) -> Vec<i32> {
        let c_arr: Vec<char> = s.chars().collect();
        let mut last: i32 = -1;
        
        let mut res: Vec<i32> = vec![c_arr.len() as i32; c_arr.len()];
        
        for i in 0..c_arr.len() {
            if c_arr[i] == c {
                last = *&i as i32;
            }
            
            if last >= 0 {
                res[i] = i as i32 - last;   
            }
        }
        
        last = -1;
        for j in 1..=c_arr.len() {
            let ind = c_arr.len() as i32 - j as i32;
            
            if c_arr[ind as usize] == c {
                last = *&ind;
            }
            
            if last > 0 {
                res[ind as usize] = min(last - ind, res[ind as usize]);   
            }
        }
        
        res
    }
}