use std::collections::HashMap;

impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        let c1 = Self::build_counter(word1);
        let c2 = Self::build_counter(word2);
        
        let mut v1 = vec![];
        let mut v2 = vec![];
        
        for (c, count) in &c1 {
            if !c2.contains_key(c) {
                return false;
            }
            v1.push(count);
        }
        
        for (c, count) in &c2 {
            if !c1.contains_key(c) {
                return false;
            }
            v2.push(count);
        }
        
        v1.sort();
        v2.sort();
        
        v1 == v2  
    }
    
    fn build_counter(word: String) -> HashMap<char, usize> {
        let mut map = HashMap::new();
        
        for c in word.chars() {
            match map.get_mut(&c) {
                Some(v) => *v += 1,
                _ => ()
            }
            
            if !map.contains_key(&c) {
                map.insert(c, 1);  
            }
        }
        
        map
    }
}