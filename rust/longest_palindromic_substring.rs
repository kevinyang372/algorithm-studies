impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let mut c = Vec::new();
        let mut length = 0;
        
        for ch in s.chars() {
            c.push(ch);
            length += 1;
        }
        
        let mut dp = vec![vec![true; length]; length];
        let mut mx_len = 1;
        let mut res = &s[0..1];
        
        for l in 1..length {
            for i in 0..length - l {
                if c[i] != c[i + l] || (l > 1 && !dp[i + 1][i + l - 1]) {
                    dp[i][i + l] = false;
                } else if l + 1 > mx_len {
                    mx_len = l + 1;
                    res = &s[i..i + l + 1];
                }
            }
        }
        
        res.to_string()
    }
}