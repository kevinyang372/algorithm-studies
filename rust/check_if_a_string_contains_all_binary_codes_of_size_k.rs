use std::collections::HashSet;
impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let k = k as usize;
        
        if k >= s.len() {
            return false;
        }
        
        let mut sh = HashSet::new();
        
        for i in 0..=s.len() - k {
            sh.insert(&s[i..i+k]);
        }
        
        sh.len() == 2usize.pow(k as u32)
    }
}