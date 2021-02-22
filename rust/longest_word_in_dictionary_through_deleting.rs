use std::cmp::Ordering;

impl Solution {
    pub fn find_longest_word(s: String, d: Vec<String>) -> String {
        let mut d = d;
        d.sort_by(|a, b| match b.len().cmp(&a.len()) {
            Ordering::Equal => a.cmp(b),
            other => other,
        });
        
        fn in_dictionary(sc: &Vec<char>, bc: &Vec<char>) -> bool {
            let mut i = 0;
            let mut j = 0;
            
            while i < sc.len() {
                if sc[i] == bc[j] {
                    j += 1;
                }
                
                if j == bc.len() { return true; }
                i += 1;
            }
            
            false
        }
        
        let s_d: Vec<char> = s.chars().collect();
        let mut res = "".to_string();
        
        for ds in d {
            let d_d: Vec<char> = ds.chars().collect();
            
            if ds.len() > res.len() && in_dictionary(&s_d, &d_d) {
                res = ds;               
            }
        }
        
        res
    }
}