use std::collections::HashMap;
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let m: HashMap<char, Vec<&str>> = [
            ('2', vec!["a", "b", "c"]),
            ('3', vec!["d", "e", "f"]),
            ('4', vec!["g", "h", "i"]),
            ('5', vec!["j", "k", "l"]),
            ('6', vec!["m", "n", "o"]),
            ('7', vec!["p", "q", "r", "s"]),
            ('8', vec!["t", "u", "v"]),
            ('9', vec!["w", "x", "y", "z"]),
        ].iter().cloned().collect();
        
        let mut s: Vec<char> = digits.chars().collect();
        s.reverse();
        
        fn iterate(d: &mut Vec<char>, m: &HashMap<char, Vec<&str>>) -> Vec<String> {
            if d.len() == 0 {
                return vec![];
            }
            
            let last_letter = d.pop().unwrap();
            let ds = m.get(&last_letter).unwrap();
            let later = iterate(d, m);
            let mut res = vec![];
            
            for l in ds {
                if later.len() == 0 {
                    res.push(l.to_string());
                }
                
                for s in &later {
                    let mut dc = l.clone().to_string();
                    dc.push_str(s);
                    
                    res.push(dc);
                }
            }
            
            res
        }
        
        iterate(&mut s, &m)
    }
}