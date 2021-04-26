impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let mut curr: Option<char> = None;
        let mut count = 0;
        let mut prev = 0;
        let mut res = 0;
        
        for c in s.chars() {
            if let Some(cr) = curr {
                if cr == c {
                    count += 1;
                    continue;
                }
            }
            
            curr = Some(c);
            res += count.min(prev);
            prev = count;
            count = 1;
        }
        
        if count > 0 {
            res += count.min(prev);
        }
        res
    }
}