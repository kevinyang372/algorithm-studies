impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut s = vec![];
        let mut j = 0;
        
        for i in 0..popped.len() {
            let len_s = s.len();
            if len_s > 0 && s[len_s - 1] == popped[i] {
                s.pop();
                continue;
            } else if j >= pushed.len() {
                return false;
            }
            
            while j < pushed.len() && popped[i] != pushed[j] {
                s.push(pushed[j]);
                j += 1;
            }
            
            j += 1;
        }
        
        s.len() == 0
    }
}