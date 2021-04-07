use std::collections::HashSet;
impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let h: HashSet<&char> = ['a', 'e', 'i', 'o', 'u'].iter().collect();
        
        let mut fi = 0;
        let mut se = 0;
        
        for (i, c) in s.chars().enumerate() {
            if i < s.len() / 2 && h.contains(&c.to_ascii_lowercase()) {
                fi += 1;
            } else if i >= s.len() / 2 && h.contains(&c.to_ascii_lowercase()) {
                se += 1;
            }
        }
        
        fi == se
    }
}