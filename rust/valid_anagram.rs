use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        fn increment_or_create(d: &mut HashMap<char, i32>, c: char) {
            match d.get_mut(&c) {
                Some(v) => { *v += 1 },
                _ => (),
            }
            
            if !d.contains_key(&c) {
                d.insert(c, 1);
            }
        }
        
        let mut d1 = HashMap::new();
        let mut d2 = HashMap::new();
        
        for c1 in s.chars() {
            increment_or_create(&mut d1, c1);
        }
        
        for c2 in t.chars() {
            increment_or_create(&mut d2, c2);
        }
        
        d1 == d2
    }
}