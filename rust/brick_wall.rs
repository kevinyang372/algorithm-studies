use std::collections::HashMap;
impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        let mut bricklen: HashMap<i32, i32> = HashMap::new();
        let mut max_len = 0i32;
        
        for row in &wall {
            let mut length = 0i32;
            let mut row_len = row.len();
            
            for (idx, size) in row.iter().enumerate() {
                length += size;
                
                if idx != row_len - 1 {
                    match bricklen.get_mut(&length) {
                        Some(val) => { *val += 1 },
                        _ => (),
                    }
                    
                    if !bricklen.contains_key(&length) {
                        bricklen.insert(length, 1);
                    }
                    
                    max_len = max_len.max(*bricklen.get(&length).unwrap());
                }
            }
        }
        
        wall.len() as i32 - max_len
    }
}