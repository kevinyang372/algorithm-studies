impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let char_vec = s.chars().collect();
        Self::backtracking(char_vec, vec![String::from("")], 0)
    }
    
    fn backtracking(s: Vec<char>, prev: Vec<String>, ind: usize) -> Vec<String> {
        if ind < s.len() {
            let mut nxt = vec![];
            let c = s[ind];
            
            for k in prev {
                let mut st = k.clone();
                st.push(c);
                nxt.push(st);
                
                if c.is_uppercase() {
                    let mut st_2 = k.clone();
                    st_2.push(c.to_ascii_lowercase());
                    nxt.push(st_2);
                } else if c.is_lowercase() {
                    let mut st_2 = k.clone();
                    st_2.push(c.to_ascii_uppercase());
                    nxt.push(st_2);
                }
            }
            
            return Self::backtracking(s, nxt, ind + 1);
        }
        
        prev
    }
}