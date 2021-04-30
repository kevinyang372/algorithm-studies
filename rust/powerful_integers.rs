use std::collections::HashSet;
impl Solution {
    pub fn powerful_integers(x: i32, y: i32, bound: i32) -> Vec<i32> {
        let mut s = HashSet::new();
        let mut dx = 0u32;
        
        while x.pow(dx) < bound {
            let mut dy = 0u32;
            
            while x.pow(dx) + y.pow(dy) <= bound {
                s.insert(x.pow(dx) + y.pow(dy));
                
                if y == 1 {
                    break;
                }
                
                dy += 1;
            }
            
            if x == 1 {
                break;
            }
            
            dx += 1;
        }
        
        s.into_iter().collect()
    }
}