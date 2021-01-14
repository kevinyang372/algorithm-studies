impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut p_count = Vec::new();
        for c in s.chars() {
            if c == '(' || c == '[' || c == '{' {
                p_count.push(c);
            } else if c == ')' {
                if p_count.len() == 0 || p_count[p_count.len() - 1] != '(' {return false;}
                p_count.pop();
            } else if c == ']' {
                if p_count.len() == 0 || p_count[p_count.len() - 1] != '[' {return false;}
                p_count.pop();
            } else if c == '}' {
                if p_count.len() == 0 || p_count[p_count.len() - 1] != '{' {return false;}
                p_count.pop();
            }
        }
        
        if p_count.len() > 0 {return false;}
        true
    }
}