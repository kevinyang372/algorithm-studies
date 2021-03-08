impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        
        fn is_palindrome(st: &String) -> bool {
            let c: Vec<char> = st.chars().collect();
            let c_len = c.len();
            
            for i in 0..c_len/2 {
                if c[i] != c[c_len - i - 1] {
                    return false;
                }   
            }
            
            true
        }
        
        if is_palindrome(&s) {
            s.len().min(1) as i32
        } else {
            2
        }
    }
}