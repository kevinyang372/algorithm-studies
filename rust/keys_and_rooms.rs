use std::collections::HashSet;

impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut stack: Vec<i32> = vec![0];
        
        while stack.len() > 0 {
            let key = stack.pop().unwrap();
            visited.insert(key);
            
            for &rnum in &rooms[key as usize] {
                if !visited.contains(&rnum) {
                    stack.push(rnum);
                }
            }
        }
        
        visited.len() == rooms.len()
    }
}