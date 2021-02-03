use std::collections::{ HashMap, HashSet };

impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        
        fn create_and_insert(d: &mut HashMap<i32, Vec<i32>>, key: i32, val: i32) {
            match d.get_mut(&key) {
                Some(v) => { v.push(val) },
                _ => (),
            }
            
            if !d.contains_key(&key) {
                d.insert(key, vec![val]);
            }
        }
        
        let mut d: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut visited: HashSet<i32> = HashSet::new();
        
        for pair in adjacent_pairs {
            create_and_insert(&mut d, pair[0], pair[1]);
            create_and_insert(&mut d, pair[1], pair[0]);
        }
        
        let mut res = vec![];
        
        for (key, value) in &d {
            if value.len() == 1 {
                let mut start = key;
                loop {
                    res.push(*start);
                    visited.insert(*start);
                    
                    match d.get(&start) {
                        Some(val) => {
                            if val.len() == 1 {
                                if visited.contains(&val[0]) {
                                    return res;
                                } else {
                                    start = &val[0];
                                }
                            } else {
                                if visited.contains(&val[0]) {
                                    start = &val[1];
                                } else {
                                    start = &val[0];
                                }
                            }
                        },
                        _ => (),
                    }
                }
            }
        }
        
        vec![]
    }
}