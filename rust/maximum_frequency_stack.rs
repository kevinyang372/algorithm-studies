use std::collections::HashMap;
use std::cmp::max;

struct FreqStack {
    max_freq: i32,
    freq: HashMap<i32, i32>,
    stack: Vec<Vec<i32>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FreqStack {

    fn new() -> Self {
        FreqStack {
            max_freq: 0,
            freq: HashMap::new(),
            stack: Vec::new(),
        }
    }
    
    fn push(&mut self, x: i32) {
        let mut curr = match self.freq.get(&x) {
            Some(val) => *val,
            _ => 0,
        };
        
        curr += 1;
        self.max_freq = max(self.max_freq, curr);
        self.freq.insert(x, curr);
        
        if self.stack.len() < curr as usize {
            self.stack.push(vec![x]);
        } else {
            self.stack[curr as usize - 1].push(x);
        }
    }
    
    fn pop(&mut self) -> i32 {
        let val = self.stack[self.max_freq as usize - 1].pop().unwrap();
        
        match self.freq.get_mut(&val) {
            Some(v) => *v -= 1,
            _ => (),
        };
        
        if self.stack[self.max_freq as usize - 1].len() == 0 {
            self.max_freq -= 1;
        }
        
        val
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 */