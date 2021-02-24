impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        let mut stack: Vec<i32> = vec![];
        let mut res = 0;
        
        for c in s.chars() {
            let stack_len = stack.len();
            let prev = if stack.len() == 0 { 0 } else { stack[stack_len - 1] };
            
            if c == '(' {
                stack.push(0);
            } else {
                let mut num = stack.pop().unwrap();
                
                if num == 0 { num += 1; }
                
                if stack.len() > 0 {
                    stack[stack_len - 2] += num * 2;
                } else {
                    res += num;
                }
            }
        }
        
        res
    }
}