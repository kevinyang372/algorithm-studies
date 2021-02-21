use std::collections::HashMap;
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let map: HashMap<char, i32> = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ].iter().cloned().collect();
        
        let r: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut res = 0;
        
        while i < r.len() {
            let curr = map.get(&r[i]).unwrap();
            
            if i + 1 == r.len() {
                res += curr;
                break;
            }
            
            let next = map.get(&r[i + 1]).unwrap();
            
            if next <= curr {
                res += curr;
                i += 1;
            } else {
                res += next - curr;
                i += 2;
            }
        }
        
        res
    }
}