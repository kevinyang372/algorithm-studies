impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut c: Vec<char> = s.chars().collect();
        let mut stack = 0;
        let mut i = 0;
        
        while i < c.len() {
            if c[i] == '(' {
                stack += 1;
            } else if c[i] == ')' {
                if stack <= 0 {
                    c.remove(i);
                    i -= 1;
                } else {
                    stack -= 1;
                }
            }
            i += 1;
        }
        
        stack = 0;
        i = c.len() - 1;
        
        while i >= 0 && i < c.len() {
            if c[i] == ')' {
                stack += 1;
            } else if c[i] == '(' {
                if stack <= 0 {
                    c.remove(i);
                } else {
                    stack -= 1;
                }
            }
            
            if i == 0 { break; }
            i -= 1;
        }
        
        c.iter().collect::<String>()
    }
}